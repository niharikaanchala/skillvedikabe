from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

from .models import Hero, Feature, WhyChoose, JobProgram, FAQ, SectionCopy, SupportSection, SiteBranding
from .permissions import IsStaffOrReadOnly
from .serializers import (
    HeroSerializer,
    FeatureSerializer,
    WhyChooseSerializer,
    JobProgramSerializer,
    FAQSerializer,
    SectionCopySerializer,
    SupportSectionSerializer,
    SiteBrandingSerializer,
)


class HeroView(APIView):
    permission_classes = [IsStaffOrReadOnly]
    parser_classes = [JSONParser, FormParser, MultiPartParser]

    def get(self, request):
        hero = Hero.objects.first()
        if not hero:
            return Response({})
        serializer = HeroSerializer(hero, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        if Hero.objects.exists():
            return Response(
                {"detail": "Hero already exists. Use PATCH to update."},
                status=status.HTTP_409_CONFLICT,
            )
        serializer = HeroSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        hero = Hero.objects.first()
        if not hero:
            return Response(
                {"detail": "No hero yet. Use POST to create one."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = HeroSerializer(
            hero,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        hero = Hero.objects.first()
        if hero:
            hero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FeatureView(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        features = Feature.objects.all()
        serializer = FeatureSerializer(features, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeatureDetailView(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request, pk):
        obj = get_object_or_404(Feature, pk=pk)
        return Response(FeatureSerializer(obj).data)

    def patch(self, request, pk):
        obj = get_object_or_404(Feature, pk=pk)
        serializer = FeatureSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        get_object_or_404(Feature, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WhyChooseView(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        data = WhyChoose.objects.all()
        serializer = WhyChooseSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WhyChooseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WhyChooseDetailView(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request, pk):
        obj = get_object_or_404(WhyChoose, pk=pk)
        return Response(WhyChooseSerializer(obj).data)

    def patch(self, request, pk):
        obj = get_object_or_404(WhyChoose, pk=pk)
        serializer = WhyChooseSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        get_object_or_404(WhyChoose, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JobProgramView(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        data = JobProgram.objects.all()
        serializer = JobProgramSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobProgramDetailView(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request, pk):
        obj = get_object_or_404(JobProgram, pk=pk)
        return Response(JobProgramSerializer(obj).data)

    def patch(self, request, pk):
        obj = get_object_or_404(JobProgram, pk=pk)
        serializer = JobProgramSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        get_object_or_404(JobProgram, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FAQView(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        data = FAQ.objects.all()
        serializer = FAQSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FAQDetailView(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request, pk):
        obj = get_object_or_404(FAQ, pk=pk)
        return Response(FAQSerializer(obj).data)

    def patch(self, request, pk):
        obj = get_object_or_404(FAQ, pk=pk)
        serializer = FAQSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        get_object_or_404(FAQ, pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SectionCopyView(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        rows = SectionCopy.objects.all()
        serializer = SectionCopySerializer(rows, many=True)
        return Response(serializer.data)


class SectionCopyDetailView(APIView):
    """GET/PATCH one section block: features | why_choose | job_program | faq (staff + JWT)."""

    permission_classes = [IsAdminUser]
    SECTIONS = frozenset({"features", "why_choose", "job_program", "faq"})

    def get(self, request, section):
        if section not in self.SECTIONS:
            return Response(status=status.HTTP_404_NOT_FOUND)
        row, _ = SectionCopy.objects.get_or_create(
            section=section,
            defaults={"heading": "", "intro": ""},
        )
        return Response(SectionCopySerializer(row).data)

    def patch(self, request, section):
        if section not in self.SECTIONS:
            return Response(status=status.HTTP_404_NOT_FOUND)
        row, _ = SectionCopy.objects.get_or_create(
            section=section,
            defaults={"heading": "", "intro": ""},
        )
        serializer = SectionCopySerializer(row, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupportSectionView(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        row = SupportSection.objects.order_by("id").first()
        if not row:
            return Response({})
        serializer = SupportSectionSerializer(row)
        return Response(serializer.data)

    def post(self, request):
        if SupportSection.objects.exists():
            return Response(
                {"detail": "Support block already exists. Use PATCH to update."},
                status=status.HTTP_409_CONFLICT,
            )
        serializer = SupportSectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        row = SupportSection.objects.order_by("id").first()
        if not row:
            return Response(
                {"detail": "No support block yet. Use POST to create one."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = SupportSectionSerializer(row, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        row = SupportSection.objects.order_by("id").first()
        if row:
            row.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HomePageBundleView(APIView):
    """Single response for public home page (Next.js)."""

    def get(self, request):
        hero = Hero.objects.first()
        hero_data = HeroSerializer(hero, context={"request": request}).data if hero else None

        support = SupportSection.objects.order_by("id").first()
        support_data = SupportSectionSerializer(support).data if support else None

        section_map = {
            row.section: {"heading": row.heading, "intro": row.intro}
            for row in SectionCopy.objects.all()
        }

        return Response(
            {
                "hero": hero_data,
                "features": FeatureSerializer(Feature.objects.all(), many=True).data,
                "why_choose": WhyChooseSerializer(WhyChoose.objects.all(), many=True).data,
                "job_program": JobProgramSerializer(JobProgram.objects.all(), many=True).data,
                "section_copy": section_map,
                "support": support_data,
                "faq": FAQSerializer(FAQ.objects.all(), many=True).data,
            }
        )


class SiteBrandingView(APIView):
    permission_classes = [IsStaffOrReadOnly]
    parser_classes = [JSONParser, FormParser, MultiPartParser]

    def get(self, request):
        row = SiteBranding.objects.order_by("id").first()
        if not row:
            return Response({})
        return Response(SiteBrandingSerializer(row, context={"request": request}).data)

    def post(self, request):
        if SiteBranding.objects.exists():
            return Response(
                {"detail": "Branding already exists. Use PATCH to update."},
                status=status.HTTP_409_CONFLICT,
            )
        serializer = SiteBrandingSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        row = SiteBranding.objects.order_by("id").first()
        if not row:
            return Response(
                {"detail": "No branding yet. Use POST to create one."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = SiteBrandingSerializer(
            row, data=request.data, partial=True, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
