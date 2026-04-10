from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hero, EmpowerSection, PortfolioItem, AdvantageItem, ProcessStep, DemoFormContent, MetaTags, SectionContent
from .serializers import HeroSerializer, EmpowerSerializer, PortfolioSerializer, AdvantageSerializer, ProcessSerializer, DemoSerializer, MetaTagsSerializer, SectionContentSerializer

class CorporateTrainingContentAPIView(APIView):
    def get(self, request):
        hero_obj = Hero.objects.order_by("id").first()
        empower_obj = EmpowerSection.objects.order_by("id").first()
        demo_obj = DemoFormContent.objects.order_by("id").first()
        meta_obj = MetaTags.objects.order_by("id").first()
        section_content_obj = SectionContent.objects.order_by("id").first()

        hero_data = HeroSerializer(hero_obj, context={"request": request}).data if hero_obj else None
        empower_data = EmpowerSerializer(empower_obj, context={"request": request}).data if empower_obj else None
        demo_raw = DemoSerializer(demo_obj, context={"request": request}).data if demo_obj else None

        portfolio_data = PortfolioSerializer(PortfolioItem.objects.all(), many=True).data
        advantage_data = AdvantageSerializer(AdvantageItem.objects.all(), many=True).data
        process_data = ProcessSerializer(ProcessStep.objects.all(), many=True).data

        # Keep response compatible with the current frontend contract.
        demo_data = None
        if demo_raw:
            points = demo_raw.get("points", [])
            if not isinstance(points, list):
                points = []
            demo_data = {
                "title": demo_raw.get("title", ""),
                "features": points,
                "form_title": "Request a Demo",
                "form_subtitle": "Talk to our experts and build your custom training plan.",
                "courses": [],
                "button_text": demo_raw.get("button_text", "Book Demo"),
            }

        return Response(
            {
                "meta": MetaTagsSerializer(meta_obj).data if meta_obj else {},
                "hero": hero_data,
                "empower": empower_data,
                "portfolio": portfolio_data,
                "advantage": advantage_data,
                "section_titles": {
                    "empower": (
                        section_content_obj.empower_title
                        if section_content_obj and section_content_obj.empower_title
                        else ""
                    ),
                    "empowerSubtitle": (
                        section_content_obj.empower_subtitle
                        if section_content_obj and section_content_obj.empower_subtitle
                        else ""
                    ),
                    "portfolio": (
                        section_content_obj.portfolio_title
                        if section_content_obj and section_content_obj.portfolio_title
                        else ""
                    ),
                    "portfolioSubtitle": (
                        section_content_obj.portfolio_subtitle
                        if section_content_obj and section_content_obj.portfolio_subtitle
                        else ""
                    ),
                    "advantage": (
                        section_content_obj.advantage_title
                        if section_content_obj and section_content_obj.advantage_title
                        else ""
                    ),
                    "advantageSubtitle": (
                        section_content_obj.advantage_subtitle
                        if section_content_obj and section_content_obj.advantage_subtitle
                        else ""
                    ),
                    "process": (
                        section_content_obj.process_title
                        if section_content_obj and section_content_obj.process_title
                        else ""
                    ),
                    "processSubtitle": (
                        section_content_obj.process_subtitle
                        if section_content_obj and section_content_obj.process_subtitle
                        else ""
                    ),
                    "demo": (
                        section_content_obj.demo_title
                        if section_content_obj and section_content_obj.demo_title
                        else ""
                    ),
                    "demoSubtitle": (
                        section_content_obj.demo_subtitle
                        if section_content_obj and section_content_obj.demo_subtitle
                        else ""
                    ),
                },
                "process": process_data,
                "demo": demo_data,
            }
        )


# -----------------------------
# META TAGS (SEO)
# -----------------------------
class MetaTagsAPI(APIView):
    def _normalize_payload(self, data):
        # Admin editors sometimes send `null`/missing values; normalize to strings.
        def to_str(v: object) -> str:
            if v is None:
                return ""
            return v if isinstance(v, str) else str(v)

        meta_title = to_str(data.get("meta_title"))
        meta_description = to_str(data.get("meta_description"))
        meta_keywords = to_str(data.get("meta_keywords"))

        # Truncate keywords/title to model max_length (prevents serializer 400).
        max_len = 255
        meta_title = meta_title[:max_len]
        meta_keywords = meta_keywords[:max_len]
        meta_description = meta_description or ""

        return {
            "meta_title": meta_title,
            "meta_description": meta_description,
            "meta_keywords": meta_keywords,
        }

    def get(self, request):
        meta_obj = MetaTags.objects.order_by("id").first()
        return Response(MetaTagsSerializer(meta_obj).data if meta_obj else {})

    def post(self, request):
        serializer = MetaTagsSerializer(data=self._normalize_payload(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def put(self, request):
        obj = MetaTags.objects.order_by("id").first()
        if not obj:
            serializer = MetaTagsSerializer(data=self._normalize_payload(request.data))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

        serializer = MetaTagsSerializer(obj, data=self._normalize_payload(request.data))
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
        serializer = MetaTagsSerializer(
            obj,
            data=MetaTagsAPI()._normalize_payload(request.data),
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        # Allow PATCH from singleton editors.
        return self.put(request, pk)


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

# ---------------------------------------
# HERO SECTION
# ---------------------------------------
class HeroAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                hero = Hero.objects.get(pk=pk)
                serializer = HeroSerializer(hero)
                return Response(serializer.data)
            except Hero.DoesNotExist:
                return Response({"error": "Hero not found"}, status=status.HTTP_404_NOT_FOUND)
        heroes = Hero.objects.all()
        serializer = HeroSerializer(heroes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            hero = Hero.objects.get(pk=pk)
        except Hero.DoesNotExist:
            return Response({"error": "Hero not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = HeroSerializer(hero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            hero = Hero.objects.get(pk=pk)
        except Hero.DoesNotExist:
            return Response({"error": "Hero not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = HeroSerializer(hero, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            hero = Hero.objects.get(pk=pk)
        except Hero.DoesNotExist:
            return Response({"error": "Hero not found"}, status=status.HTTP_404_NOT_FOUND)
        hero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------------------------------
# EMPOWER SECTION
# ---------------------------------------
class EmpowerAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                obj = EmpowerSection.objects.get(pk=pk)
                serializer = EmpowerSerializer(obj)
                return Response(serializer.data)
            except EmpowerSection.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        objs = EmpowerSection.objects.all()
        serializer = EmpowerSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            obj = EmpowerSection.objects.get(pk=pk)
        except EmpowerSection.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpowerSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            obj = EmpowerSection.objects.get(pk=pk)
        except EmpowerSection.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpowerSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            obj = EmpowerSection.objects.get(pk=pk)
        except EmpowerSection.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------------------------------
# PORTFOLIO SECTION
# ---------------------------------------
class PortfolioAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                obj = PortfolioItem.objects.get(pk=pk)
                serializer = PortfolioSerializer(obj)
                return Response(serializer.data)
            except PortfolioItem.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        objs = PortfolioItem.objects.all()
        serializer = PortfolioSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            obj = PortfolioItem.objects.get(pk=pk)
        except PortfolioItem.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PortfolioSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            obj = PortfolioItem.objects.get(pk=pk)
        except PortfolioItem.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PortfolioSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            obj = PortfolioItem.objects.get(pk=pk)
        except PortfolioItem.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# ---------------------------------------
# ADVANTAGE SECTION
# ---------------------------------------
class AdvantageAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                obj = AdvantageItem.objects.get(pk=pk)
                serializer = AdvantageSerializer(obj)
                return Response(serializer.data)
            except AdvantageItem.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        objs = AdvantageItem.objects.all()
        serializer = AdvantageSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvantageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            obj = AdvantageItem.objects.get(pk=pk)
        except AdvantageItem.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AdvantageSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            obj = AdvantageItem.objects.get(pk=pk)
        except AdvantageItem.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AdvantageSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            obj = AdvantageItem.objects.get(pk=pk)
        except AdvantageItem.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------------------------------
# PROCESS SECTION
# ---------------------------------------
class ProcessAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                obj = ProcessStep.objects.get(pk=pk)
                serializer = ProcessSerializer(obj)
                return Response(serializer.data)
            except ProcessStep.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        objs = ProcessStep.objects.all()
        serializer = ProcessSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProcessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            obj = ProcessStep.objects.get(pk=pk)
        except ProcessStep.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProcessSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            obj = ProcessStep.objects.get(pk=pk)
        except ProcessStep.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProcessSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            obj = ProcessStep.objects.get(pk=pk)
        except ProcessStep.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------------------------------
# DEMO FORM SECTION
# ---------------------------------------
class DemoAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                obj = DemoFormContent.objects.get(pk=pk)
                serializer = DemoSerializer(obj)
                return Response(serializer.data)
            except DemoFormContent.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        objs = DemoFormContent.objects.all()
        serializer = DemoSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DemoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            obj = DemoFormContent.objects.get(pk=pk)
        except DemoFormContent.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DemoSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            obj = DemoFormContent.objects.get(pk=pk)
        except DemoFormContent.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DemoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            obj = DemoFormContent.objects.get(pk=pk)
        except DemoFormContent.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)