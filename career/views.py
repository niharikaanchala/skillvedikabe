from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

from .models import (
    CareerHero,
    CareerService,
    CareerSupport,
    CareerCTA,
    FAQ,
    MetaTags,
    CareerServicesHeading,
)
from .serializers import (
    CareerHeroSerializer,
    CareerServiceSerializer,
    CareerSupportSerializer,
    CareerCTASerializer,
    FAQSerializer,
    CareerServicesHeadingSerializer,
    MetaTagsSerializer,
)


class CareerPageView(APIView):
    """
    Returns the entire career page data in one request:
    hero (single row or {}), services, support, CTA, and FAQs.
    """

    permission_classes = [AllowAny]

    def get(self, request):
        hero = CareerHero.objects.order_by("id").first()
        support = CareerSupport.objects.order_by("id").first()
        cta = CareerCTA.objects.order_by("id").first()
        meta = MetaTags.objects.order_by("id").first()
        services_heading = (
            CareerServicesHeading.objects.order_by("id").first()
        )

        data = {
            "meta": MetaTagsSerializer(meta).data if meta else {},
            "hero": CareerHeroSerializer(hero).data if hero else {},
            "services": CareerServiceSerializer(
                CareerService.objects.all().order_by("id"), many=True
            ).data,
            "services_heading": CareerServicesHeadingSerializer(services_heading).data
            if services_heading
            else {},
            "support": CareerSupportSerializer(support).data if support else {},
            "cta": CareerCTASerializer(cta).data if cta else {},
            "faqs": FAQSerializer(FAQ.objects.all().order_by("id"), many=True).data,
        }
        return Response(data)


# -------- META TAGS --------
class MetaTagsAPI(APIView):
    def get(self, request):
        meta = MetaTags.objects.order_by("id").first()
        return Response(MetaTagsSerializer(meta).data if meta else {})

    def post(self, request):
        serializer = MetaTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def put(self, request):
        obj = MetaTags.objects.order_by("id").first()
        if not obj:
            serializer = MetaTagsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        serializer = MetaTagsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


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
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        obj = MetaTags.objects.get(id=pk)
        serializer = MetaTagsSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

# Individual section views
class CareerHeroView(APIView):
    def get(self, request, pk=None):
        if pk:
            hero = get_object_or_404(CareerHero, pk=pk)
            return Response(CareerHeroSerializer(hero).data)
        heroes = CareerHero.objects.all()
        return Response(CareerHeroSerializer(heroes, many=True).data)

    def post(self, request):
        serializer = CareerHeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        hero = get_object_or_404(CareerHero, pk=pk)
        serializer = CareerHeroSerializer(hero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        hero = get_object_or_404(CareerHero, pk=pk)
        serializer = CareerHeroSerializer(hero, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        hero = get_object_or_404(CareerHero, pk=pk)
        hero.delete()
        return Response({"message": "Deleted successfully"})


class CareerServiceView(APIView):
    def get(self, request, pk=None):
        if pk:
            service = get_object_or_404(CareerService, pk=pk)
            return Response(CareerServiceSerializer(service).data)
        services = CareerService.objects.all()
        return Response(CareerServiceSerializer(services, many=True).data)

    def post(self, request):
        serializer = CareerServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        service = get_object_or_404(CareerService, pk=pk)
        serializer = CareerServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        service = get_object_or_404(CareerService, pk=pk)
        serializer = CareerServiceSerializer(service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        if pk:
            service = get_object_or_404(CareerService, pk=pk)
            service.delete()
            return Response({"message": "Deleted successfully"})
        ids = request.data.get("ids", [])
        if not ids:
            return Response({"error": "No IDs provided"}, status=400)
        CareerService.objects.filter(id__in=ids).delete()
        return Response({"message": "Bulk delete successful"})


class CareerSupportView(APIView):
    def get(self, request):
        support = CareerSupport.objects.first()
        return Response(CareerSupportSerializer(support).data if support else {})

    def post(self, request):
        serializer = CareerSupportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        support = get_object_or_404(CareerSupport, pk=pk)
        serializer = CareerSupportSerializer(support, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        support = get_object_or_404(CareerSupport, pk=pk)
        support.delete()
        return Response({"message": "Deleted"})


class CareerCTAView(APIView):
    def get(self, request):
        cta = CareerCTA.objects.first()
        return Response(CareerCTASerializer(cta).data if cta else {})

    def post(self, request):
        serializer = CareerCTASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        cta = get_object_or_404(CareerCTA, pk=pk)
        serializer = CareerCTASerializer(cta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        cta = get_object_or_404(CareerCTA, pk=pk)
        cta.delete()
        return Response({"message": "Deleted"})


class FAQView(APIView):
    def get(self, request, pk=None):
        if pk:
            faq = get_object_or_404(FAQ, pk=pk)
            return Response(FAQSerializer(faq).data)
        faqs = FAQ.objects.all()
        return Response(FAQSerializer(faqs, many=True).data)

    def post(self, request):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        faq = get_object_or_404(FAQ, pk=pk)
        serializer = FAQSerializer(faq, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        faq = get_object_or_404(FAQ, pk=pk)
        serializer = FAQSerializer(faq, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        if pk:
            faq = get_object_or_404(FAQ, pk=pk)
            faq.delete()
            return Response({"message": "Deleted"})
        ids = request.data.get("ids", [])
        if not ids:
            return Response({"error": "No IDs provided"}, status=400)
        FAQ.objects.filter(id__in=ids).delete()
        return Response({"message": "Bulk delete successful"})


class CareerServicesHeadingView(APIView):
    """
    Singleton CRUD for the Services section heading shown on /career-services.
    """

    def get(self, request):
        services_heading = CareerServicesHeading.objects.order_by("id").first()
        return (
            CareerServicesHeadingSerializer(services_heading).data
            if services_heading
            else {}
        )

    def post(self, request):
        serializer = CareerServicesHeadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        services_heading = get_object_or_404(CareerServicesHeading, pk=pk)
        serializer = CareerServicesHeadingSerializer(
            services_heading, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)