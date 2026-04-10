"""JWT token issue for admin SPA (email or username + password)."""

from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework.permissions import AllowAny
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
