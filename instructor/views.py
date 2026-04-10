from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import HeroSection, Feature, CTASection, FormSection, InstructorApplication
from .serializers import (
    HeroSectionSerializer,
    FeatureSerializer,
    CTASectionSerializer,
    FormSectionSerializer,
    InstructorApplicationSerializer,
)

# ---------------- HERO ----------------
class HeroAPI(APIView):

    def get(self, request):
        heroes = HeroSection.objects.all()
        serializer = HeroSectionSerializer(heroes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HeroSectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class HeroDetailAPI(APIView):

    def get(self, request, pk):
        hero = HeroSection.objects.get(id=pk)
        return Response(HeroSectionSerializer(hero).data)

    def put(self, request, pk):
        hero = HeroSection.objects.get(id=pk)
        serializer = HeroSectionSerializer(hero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        hero = HeroSection.objects.get(id=pk)
        hero.delete()
        return Response({"message": "Deleted successfully"})


# ---------------- FEATURES ----------------
class FeatureAPI(APIView):

    def get(self, request):
        features = Feature.objects.all()
        return Response(FeatureSerializer(features, many=True).data)

    def post(self, request):
        serializer = FeatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class FeatureDetailAPI(APIView):

    def get(self, request, pk):
        feature = Feature.objects.get(id=pk)
        return Response(FeatureSerializer(feature).data)

    def put(self, request, pk):
        feature = Feature.objects.get(id=pk)
        serializer = FeatureSerializer(feature, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        feature = Feature.objects.get(id=pk)
        feature.delete()
        return Response({"message": "Deleted successfully"})


# ✅ BULK CREATE FEATURES
class FeatureBulkCreateAPI(APIView):

    def post(self, request):
        serializer = FeatureSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


# ✅ BULK DELETE FEATURES
class FeatureBulkDeleteAPI(APIView):

    def delete(self, request):
        ids = request.data.get("ids", [])
        Feature.objects.filter(id__in=ids).delete()
        return Response({"message": "Bulk deleted successfully"})


# ---------------- CTA ----------------
class CTAAPI(APIView):

    def get(self, request):
        data = CTASection.objects.all()
        return Response(CTASectionSerializer(data, many=True).data)

    def post(self, request):
        serializer = CTASectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class CTADetailAPI(APIView):

    def put(self, request, pk):
        obj = CTASection.objects.get(id=pk)
        serializer = CTASectionSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        obj = CTASection.objects.get(id=pk)
        obj.delete()
        return Response({"message": "Deleted"})


# ---------------- FORM ----------------
class FormAPI(APIView):

    def get(self, request):
        data = FormSection.objects.all()
        return Response(FormSectionSerializer(data, many=True).data)

    def post(self, request):
        serializer = FormSectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class FormDetailAPI(APIView):

    def put(self, request, pk):
        obj = FormSection.objects.get(id=pk)
        serializer = FormSectionSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        obj = FormSection.objects.get(id=pk)
        obj.delete()
        return Response({"message": "Deleted"})


# ---------------- INSTRUCTOR FULL PAGE ----------------
class InstructorPageAPI(APIView):

    def get(self, request):
        hero = HeroSection.objects.first()
        features = Feature.objects.all()
        cta = CTASection.objects.first()
        form = FormSection.objects.first()

        return Response({
            "hero": HeroSectionSerializer(hero).data if hero else {},
            "features": FeatureSerializer(features, many=True).data,
            "cta": CTASectionSerializer(cta).data if cta else {},
            "form": FormSectionSerializer(form).data if form else {},
        })


class InstructorApplicationSubmitAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = InstructorApplicationSerializer(data=request.data)
        if serializer.is_valid():
            if not serializer.validated_data.get("agreed_to_terms", False):
                return Response(
                    {"agreed_to_terms": ["You must agree to terms and privacy policy."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InstructorApplicationListAPI(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        applications = InstructorApplication.objects.all().order_by("-created_at")
        serializer = InstructorApplicationSerializer(applications, many=True)
        return Response(serializer.data)


class InstructorApplicationDetailAPI(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, pk):
        try:
            app = InstructorApplication.objects.get(id=pk)
        except InstructorApplication.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = InstructorApplicationSerializer(app, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            app = InstructorApplication.objects.get(id=pk)
        except InstructorApplication.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)