from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from courses.models import Course
from courses.serializers import CourseSerializer

from .models import Category, CategoryPageContent
from .serializers import CategorySerializer


# ✅ GET (all) + POST (create)
class CategoryListView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ GET courses for a category (/api/categories/<id>/courses/)
class CategoryCoursesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        if not Category.objects.filter(pk=id).exists():
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        courses = Course.objects.filter(category_id=id).order_by("-rating", "title")
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


# ✅ GET (single) + PUT (update) + DELETE (single)
class CategoryDetailView(APIView):

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            return None

    def get(self, request, id):
        category = self.get_object(id)
        if not category:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, id):
        category = self.get_object(id)
        if not category:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        category = self.get_object(id)
        if not category:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        category.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# ✅ BULK DELETE
class CategoryBulkDeleteView(APIView):

    def delete(self, request):
        ids = request.data.get("ids", [])

        if not ids:
            return Response({"error": "No IDs provided"}, status=status.HTTP_400_BAD_REQUEST)

        categories = Category.objects.filter(id__in=ids)
        deleted_count = categories.count()
        categories.delete()

        return Response({
            "message": f"{deleted_count} categories deleted successfully"
        })


class CategoryPageContentView(APIView):
    """
    Per-category CMS content for public category pages.

    GET  /api/categories/<id>/page-content/
    POST /api/categories/<id>/page-content/   (create/update)
    """

    permission_classes = [AllowAny]

    def _serialize(self, obj: CategoryPageContent):
        return {
            "category": obj.category_id,
            "hero_title": obj.hero_title,
            "hero_subtitle": obj.hero_subtitle,
            "hero_cta_text": obj.hero_cta_text,
            "hero_cta_link": obj.hero_cta_link,
            "seo_title": obj.seo_title,
            "seo_description": obj.seo_description,
            "seo_keywords": obj.seo_keywords,
            "why_title": obj.why_title,
            "why_points": obj.why_points if isinstance(obj.why_points, list) else [],
            "cta_title": obj.cta_title,
            "cta_subtitle": obj.cta_subtitle,
            "cta_buttons": obj.cta_buttons if isinstance(obj.cta_buttons, list) else [],
            "faq_heading": obj.faq_heading,
            "faq_intro": obj.faq_intro,
            "faq_items": obj.faq_items if isinstance(obj.faq_items, list) else [],
        }

    def get(self, request, id: int):
        if not Category.objects.filter(pk=id).exists():
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        obj = CategoryPageContent.objects.filter(category_id=id).first()
        if not obj:
            return Response({"error": "Category page content not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(self._serialize(obj))

    def post(self, request, id: int):
        try:
            category = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

        obj, _ = CategoryPageContent.objects.get_or_create(category=category)
        d = request.data

        def pick(*keys, default=""):
            for k in keys:
                if k in d and d[k] is not None:
                    return d[k]
            return default

        obj.hero_title = str(pick("hero_title", default=obj.hero_title or ""))
        obj.hero_subtitle = str(pick("hero_subtitle", default=obj.hero_subtitle or ""))
        obj.hero_cta_text = str(pick("hero_cta_text", default=obj.hero_cta_text or ""))
        obj.hero_cta_link = str(pick("hero_cta_link", default=obj.hero_cta_link or ""))
        obj.seo_title = str(pick("seo_title", "seoTitle", default=obj.seo_title or ""))
        obj.seo_description = str(pick("seo_description", "seoDescription", default=obj.seo_description or ""))
        obj.seo_keywords = str(pick("seo_keywords", "seoKeywords", default=obj.seo_keywords or ""))
        obj.why_title = str(pick("why_title", default=obj.why_title or ""))
        why_points = pick("why_points", default=obj.why_points)
        if isinstance(why_points, list):
            obj.why_points = why_points
        else:
            obj.why_points = []
        obj.cta_title = str(pick("cta_title", default=obj.cta_title or ""))
        obj.cta_subtitle = str(pick("cta_subtitle", default=obj.cta_subtitle or ""))
        cta_buttons = pick("cta_buttons", default=obj.cta_buttons)
        if isinstance(cta_buttons, list):
            obj.cta_buttons = cta_buttons
        else:
            obj.cta_buttons = []
        obj.faq_heading = str(pick("faq_heading", default=obj.faq_heading or ""))
        obj.faq_intro = str(pick("faq_intro", default=obj.faq_intro or ""))

        faq_items = pick("faq_items", default=obj.faq_items)
        if isinstance(faq_items, list):
            obj.faq_items = faq_items
        else:
            obj.faq_items = []

        obj.save()
        return Response(self._serialize(obj), status=status.HTTP_200_OK)