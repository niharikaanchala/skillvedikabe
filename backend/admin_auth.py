"""JWT token issue for admin SPA (email or username + password)."""

from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class AdminTokenSerializer(serializers.Serializer):
    email = serializers.CharField(required=False, allow_blank=True)
    username = serializers.CharField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True, trim_whitespace=False)

    def validate(self, attrs):
        User = get_user_model()
        password = attrs["password"]
        email = (attrs.get("email") or "").strip()
        username = (attrs.get("username") or "").strip()

        if not email and not username:
            raise serializers.ValidationError("Email or username is required.")

        user = None
        if email:
            found = User.objects.filter(email__iexact=email).first()
            if found and found.check_password(password):
                user = found
            else:
                # Fallback: some admin users sign in with username even if UI field says "email".
                user = authenticate(username=email, password=password)
        elif username:
            user = authenticate(username=username, password=password)

        if user is None or not user.is_active:
            raise AuthenticationFailed("Invalid email or password.")
        if not user.is_staff:
            raise PermissionDenied("Admin access only. Use a staff account.")

        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class AdminObtainTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = AdminTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


def _serialize_admin_user(user):
    return {
        "id": user.pk,
        "username": user.get_username(),
        "email": getattr(user, "email", "") or "",
        "first_name": getattr(user, "first_name", "") or "",
        "last_name": getattr(user, "last_name", "") or "",
        "is_staff": bool(getattr(user, "is_staff", False)),
        "is_superuser": bool(getattr(user, "is_superuser", False)),
    }


class AdminProfileSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=False, max_length=150)
    email = serializers.EmailField(required=False, allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=150)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=150)
    current_password = serializers.CharField(
        required=False, allow_blank=True, write_only=True, trim_whitespace=False
    )
    new_password = serializers.CharField(
        required=False, allow_blank=True, write_only=True, trim_whitespace=False, min_length=8
    )

    def validate_username(self, value):
        username = (value or "").strip()
        if not username:
            raise serializers.ValidationError("Username is required.")
        User = get_user_model()
        user = self.context["request"].user
        qs = User.objects.filter(username__iexact=username).exclude(pk=user.pk)
        if qs.exists():
            raise serializers.ValidationError("This username is already taken.")
        return username

    def validate_email(self, value):
        email = (value or "").strip()
        if not email:
            return ""
        User = get_user_model()
        user = self.context["request"].user
        qs = User.objects.filter(email__iexact=email).exclude(pk=user.pk)
        if qs.exists():
            raise serializers.ValidationError("This email is already in use.")
        return email

    def validate(self, attrs):
        new_password = attrs.get("new_password") or ""
        current_password = attrs.get("current_password") or ""
        if new_password and not current_password:
            raise serializers.ValidationError(
                {"current_password": "Current password is required to set a new password."}
            )
        if new_password:
            user = self.context["request"].user
            if not user.check_password(current_password):
                raise serializers.ValidationError(
                    {"current_password": "Current password is incorrect."}
                )
        return attrs

    def update(self, instance, validated_data):
        if "username" in validated_data:
            instance.username = validated_data["username"]
        if "email" in validated_data:
            instance.email = validated_data["email"]
        if "first_name" in validated_data:
            instance.first_name = validated_data["first_name"].strip()
        if "last_name" in validated_data:
            instance.last_name = validated_data["last_name"].strip()
        new_password = validated_data.get("new_password") or ""
        if new_password:
            instance.set_password(new_password)
        instance.save()
        return instance


class AdminProfileView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        return Response(_serialize_admin_user(request.user))

    def patch(self, request, *args, **kwargs):
        serializer = AdminProfileSerializer(
            data=request.data, partial=True, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.update(request.user, serializer.validated_data)
        return Response(_serialize_admin_user(user))

    def put(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)
