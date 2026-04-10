from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AboutHero, CtaSection, DemoSection, ValueItem, ValuesSection, MetaTags
from .serializers import (
    AboutHeroSerializer,
    CtaSectionSerializer,
    DemoSectionSerializer,
    ValueItemSerializer,
    ValuesSectionSerializer,
    MetaTagsSerializer,
)


class AboutContentAPIView(APIView):
    def get(self, request):
        hero_obj = AboutHero.objects.order_by("id").first()
        values_section_obj = ValuesSection.objects.order_by("id").first()
        cta_obj = CtaSection.objects.order_by("id").first()
        demo_obj = DemoSection.objects.order_by("id").first()
        meta_obj = MetaTags.objects.order_by("id").first()

        # Always return complete single-section objects so frontend can render
        # without changing UI structure, while still using DB values when present.
        hero_data = AboutHeroSerializer(hero_obj if hero_obj else AboutHero()).data
        values_section_data = ValuesSectionSerializer(
            values_section_obj if values_section_obj else ValuesSection()
        ).data
        cta_data = CtaSectionSerializer(
            cta_obj if cta_obj else CtaSection(heading="")
        ).data
        demo_data = DemoSectionSerializer(demo_obj if demo_obj else DemoSection()).data
        values_data = ValueItemSerializer(ValueItem.objects.all(), many=True).data

        return Response(
            {
                "meta": MetaTagsSerializer(meta_obj).data if meta_obj else {},
                "hero": hero_data,
                "values_section": values_section_data,
                "values": values_data,
                "cta": cta_data,
                "demo": demo_data,
            }
        )


# -----------------------------
# META TAGS (SEO)
# -----------------------------
class MetaTagsAPI(APIView):
    def get(self, request):
        meta_obj = MetaTags.objects.order_by("id").first()
        return Response(MetaTagsSerializer(meta_obj).data if meta_obj else {})

    def post(self, request):
        serializer = MetaTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        obj = MetaTags.objects.order_by("id").first()
        if not obj:
            serializer = MetaTagsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer = MetaTagsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        return self.put(request)


class MetaTagsDetailAPI(APIView):
    def get(self, request, pk):
        obj = MetaTags.objects.get(id=pk)
        return Response(MetaTagsSerializer(obj).data)

    def put(self, request, pk):
        obj = MetaTags.objects.get(id=pk)
        serializer = MetaTagsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        return self.put(request, pk)


class BaseSectionAPIView(APIView):
    model = None
    serializer_class = None
    not_found_message = "Not found"

    def get(self, request, pk=None):
        if pk is not None:
            try:
                obj = self.model.objects.get(pk=pk)
            except self.model.DoesNotExist:
                return Response({"error": self.not_found_message}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
            return Response(serializer.data)

        serializer = self.serializer_class(self.model.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            obj = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({"error": self.not_found_message}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            obj = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({"error": self.not_found_message}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            obj = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({"error": self.not_found_message}, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AboutHeroAPIView(BaseSectionAPIView):
    model = AboutHero
    serializer_class = AboutHeroSerializer
    not_found_message = "About hero not found"


class ValuesSectionAPIView(BaseSectionAPIView):
    model = ValuesSection
    serializer_class = ValuesSectionSerializer
    not_found_message = "Values section not found"


class ValueItemAPIView(BaseSectionAPIView):
    model = ValueItem
    serializer_class = ValueItemSerializer
    not_found_message = "Value item not found"


class CtaSectionAPIView(BaseSectionAPIView):
    model = CtaSection
    serializer_class = CtaSectionSerializer
    not_found_message = "CTA section not found"


class DemoSectionAPIView(BaseSectionAPIView):
    model = DemoSection
    serializer_class = DemoSectionSerializer
    not_found_message = "Demo section not found"
