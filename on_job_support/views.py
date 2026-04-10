from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Hero, RealTimeHelp, Audience, Help, Step, WhyChoose, Demo, DemoRequest
from .serializers import (
    HeroSerializer, RealTimeHelpSerializer, AudienceSerializer,
    HelpSerializer, StepSerializer, WhyChooseSerializer, DemoSerializer, DemoRequestSerializer,
    MetaTagsSerializer, SectionContentSerializer,
)

from .models import MetaTags, SectionContent

# ----------------------------
# Hero CRUD
# ----------------------------
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    # Bulk Delete
    @action(detail=False, methods=["post"])
    def bulk_delete(self, request):
        ids = request.data.get("ids", [])
        if not ids:
            return Response({"error": "No IDs provided"}, status=status.HTTP_400_BAD_REQUEST)
        deleted_count, _ = Hero.objects.filter(id__in=ids).delete()
        return Response({"message": f"{deleted_count} hero items deleted."}, status=status.HTTP_200_OK)


# ----------------------------
# RealTimeHelp CRUD
# ----------------------------
class RealTimeHelpViewSet(viewsets.ModelViewSet):
    queryset = RealTimeHelp.objects.all()
    serializer_class = RealTimeHelpSerializer

    @action(detail=False, methods=["post"])
    def bulk_delete(self, request):
        ids = request.data.get("ids", [])
        deleted_count, _ = RealTimeHelp.objects.filter(id__in=ids).delete()
        return Response({"message": f"{deleted_count} real-time help items deleted."}, status=status.HTTP_200_OK)


# ----------------------------
# Audience CRUD
# ----------------------------
class AudienceViewSet(viewsets.ModelViewSet):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer

    @action(detail=False, methods=["post"])
    def bulk_delete(self, request):
        ids = request.data.get("ids", [])
        deleted_count, _ = Audience.objects.filter(id__in=ids).delete()
        return Response({"message": f"{deleted_count} audience items deleted."}, status=status.HTTP_200_OK)


# ----------------------------
# Help CRUD
# ----------------------------
class HelpViewSet(viewsets.ModelViewSet):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer

    @action(detail=False, methods=["post"])
    def bulk_delete(self, request):
        ids = request.data.get("ids", [])
        deleted_count, _ = Help.objects.filter(id__in=ids).delete()
        return Response({"message": f"{deleted_count} help items deleted."}, status=status.HTTP_200_OK)


# ----------------------------
# Step CRUD
# ----------------------------
class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

    @action(detail=False, methods=["post"])
    def bulk_delete(self, request):
        ids = request.data.get("ids", [])
        deleted_count, _ = Step.objects.filter(id__in=ids).delete()
        return Response({"message": f"{deleted_count} steps deleted."}, status=status.HTTP_200_OK)


# ----------------------------
# WhyChoose CRUD
# ----------------------------
class WhyChooseViewSet(viewsets.ModelViewSet):
    queryset = WhyChoose.objects.all()
    serializer_class = WhyChooseSerializer

    @action(detail=False, methods=["post"])
    def bulk_delete(self, request):
        ids = request.data.get("ids", [])
        deleted_count, _ = WhyChoose.objects.filter(id__in=ids).delete()
        return Response({"message": f"{deleted_count} WhyChoose items deleted."}, status=status.HTTP_200_OK)

# ----------------------------
# Demo CRUD
# ----------------------------
class DemoViewSet(viewsets.ModelViewSet):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer

    @action(detail=False, methods=["post"])
    def bulk_delete(self, request):
        ids = request.data.get("ids", [])
        deleted_count, _ = Demo.objects.filter(id__in=ids).delete()
        return Response(
            {"message": f"{deleted_count} demo items deleted."},
            status=status.HTTP_200_OK
        )


# DemoRequest CRUD
# ----------------------------
class DemoRequestViewSet(viewsets.ModelViewSet):
    queryset = DemoRequest.objects.all()
    serializer_class = DemoRequestSerializer

    @action(detail=False, methods=["post"])
    def bulk_delete(self, request):
        ids = request.data.get("ids", [])
        deleted_count, _ = DemoRequest.objects.filter(id__in=ids).delete()
        return Response({"message": f"{deleted_count} demo requests deleted."}, status=status.HTTP_200_OK)


# ----------------------------
# META TAGS (SEO)
# ----------------------------
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
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        return self.put(request, pk)

    def delete(self, request, pk):
        MetaTags.objects.get(id=pk).delete()
        return Response({"message": "Deleted"})


class SectionContentAPI(APIView):
    def get(self, request):
        obj = SectionContent.objects.order_by("id").first()
        return Response(SectionContentSerializer(obj).data if obj else {})

    def post(self, request):
        serializer = SectionContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def put(self, request):
        obj = SectionContent.objects.order_by("id").first()
        if not obj:
            serializer = SectionContentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

        serializer = SectionContentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def patch(self, request):
        return self.put(request)