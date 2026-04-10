import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Course, CoursesPageContent, CourseCounsellingLead
from .serializers import CourseSerializer, CourseCounsellingLeadSerializer

# -----------------------------
# Courses CRUD
# -----------------------------
class CourseListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        is_bulk = isinstance(request.data, list)
        serializer = CourseSerializer(data=request.data, many=is_bulk)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)


class CourseDetailView(APIView):
    permission_classes = [AllowAny]

    def get_object(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            return None

    def get(self, request, id):
        course = self.get_object(id)
        if not course:
            return Response({"error": "Course not found"}, status=404)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, id):
        course = self.get_object(id)
        if not course:
            return Response({"error": "Course not found"}, status=404)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def patch(self, request, id):
        course = self.get_object(id)
        if not course:
            return Response({"error": "Course not found"}, status=404)
        serializer = CourseSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        course = self.get_object(id)
        if not course:
            return Response({"error": "Course not found"}, status=404)
        course.delete()
        return Response({"message": "Course deleted successfully"}, status=204)


class CourseBulkDeleteView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request):
        ids = request.data.get("ids", [])
        if not ids:
            return Response({"error": "No IDs provided"}, status=400)
        courses = Course.objects.filter(id__in=ids)
        deleted_count = courses.count()
        courses.delete()
        return Response({"message": f"{deleted_count} courses deleted successfully"})


class CourseByCategoryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, category_id):
        courses = Course.objects.filter(category_id=category_id)
        if not courses.exists():
            return Response({"message": "No courses found"}, status=404)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


# -----------------------------
# Courses Page Content Sections (Admin CRUD + Public)
# -----------------------------

# HERO
class CoursesHeroView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        obj = CoursesPageContent.objects.first()
        if not obj:
            return Response({"error": "Hero content not found"}, status=404)
        return Response({
            "hero_title": obj.hero_title,
            "hero_subtitle": obj.hero_subtitle
        })

    def post(self, request):
        # Admin create/update
        obj, _ = CoursesPageContent.objects.get_or_create(id=1)
        obj.hero_title = request.data.get("hero_title", obj.hero_title)
        obj.hero_subtitle = request.data.get("hero_subtitle", obj.hero_subtitle)
        obj.save()
        return Response({
            "hero_title": obj.hero_title,
            "hero_subtitle": obj.hero_subtitle
        })


# WHY LEARN / INVEST


class CoursesWhyLearnView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        obj = CoursesPageContent.objects.first()
        if not obj:
            return Response({"error": "Why Learn content not found"}, status=404)
        
        why_points = obj.why_points if obj.why_points else []
        
        return Response({
            "why_title": obj.why_title,
            "why_points": why_points
        })

    def post(self, request):
        obj, _ = CoursesPageContent.objects.get_or_create(id=1)
        obj.why_title = request.data.get("why_title", obj.why_title)
        
        # Make sure why_points is a list
        why_points = request.data.get("why_points", obj.why_points)
        if not isinstance(why_points, list):
            # If someone sends string, convert it to list by splitting
            why_points = [p.strip() for p in why_points.split(",")]
        
        obj.why_points = why_points
        obj.save()
        
        return Response({
            "why_title": obj.why_title,
            "why_points": obj.why_points  # already a list
        })
# CTA
class CoursesCTAView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        obj = CoursesPageContent.objects.first()
        if not obj:
            return Response({"error": "CTA content not found"}, status=404)
        return Response({
            "cta_title": obj.cta_title,
            "cta_subtitle": obj.cta_subtitle
        })

    def post(self, request):
        obj, _ = CoursesPageContent.objects.get_or_create(id=1)
        obj.cta_title = request.data.get("cta_title", obj.cta_title)
        obj.cta_subtitle = request.data.get("cta_subtitle", obj.cta_subtitle)
        obj.save()
        return Response({
            "cta_title": obj.cta_title,
            "cta_subtitle": obj.cta_subtitle
        })


# FAQ
class CoursesFAQView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        obj = CoursesPageContent.objects.first()
        if not obj:
            return Response({"error": "FAQ content not found"}, status=404)
        try:
            faq_items = json.loads(obj.faq_items)
        except:
            faq_items = []
        return Response({
            "faq_heading": obj.faq_heading,
            "faq_intro": obj.faq_intro,
            "faq_items": faq_items
        })

    def post(self, request):
        obj, _ = CoursesPageContent.objects.get_or_create(id=1)
        obj.faq_heading = request.data.get("faq_heading", obj.faq_heading)
        obj.faq_intro = request.data.get("faq_intro", obj.faq_intro)
        obj.faq_items = json.dumps(request.data.get("faq_items", json.loads(obj.faq_items)))
        obj.save()
        return Response({
            "faq_heading": obj.faq_heading,
            "faq_intro": obj.faq_intro,
            "faq_items": json.loads(obj.faq_items)
        })


class CoursesPageContentView(APIView):
    permission_classes = [AllowAny]

    def _parse_buttons(self, raw, fallback_list):
        if raw is None:
            return fallback_list
        if isinstance(raw, list):
            cleaned = []
            for item in raw:
                if not isinstance(item, dict):
                    continue
                text = str(item.get("text", "")).strip()
                link = str(item.get("link", "")).strip()
                variant = str(item.get("variant", "")).strip()
                if not text or not link:
                    continue
                cleaned.append(
                    {"text": text, "link": link, **({"variant": variant} if variant else {})}
                )
            return cleaned
        if isinstance(raw, str):
            s = raw.strip()
            if not s:
                return []
            try:
                parsed = json.loads(s)
                if isinstance(parsed, list):
                    return self._parse_buttons(parsed, fallback_list)
            except Exception:
                return fallback_list
        return fallback_list

    def _serialize(self, obj):
        try:
            faq_items = json.loads(obj.faq_items)
        except Exception:
            faq_items = []
        return {
            "heroTitle": obj.hero_title,
            "heroSubtitle": obj.hero_subtitle,
            "heroCtaButtons": obj.hero_cta_buttons if isinstance(obj.hero_cta_buttons, list) else [],
            "metaTitle": obj.meta_title,
            "metaDescription": obj.meta_description,
            "metaKeywords": obj.meta_keywords,
            "whyTitle": obj.why_title,
            "whyPoints": obj.why_points if isinstance(obj.why_points, list) else [],
            "ctaTitle": obj.cta_title,
            "ctaSubtitle": obj.cta_subtitle,
            "ctaButtons": obj.cta_buttons if isinstance(obj.cta_buttons, list) else [],
            "faqHeading": obj.faq_heading,
            "faqIntro": obj.faq_intro,
            "faqItems": faq_items,
        }

    def get(self, request):
        obj = CoursesPageContent.objects.first()
        if not obj:
            return Response({"error": "Courses page content not found"}, status=404)
        return Response(self._serialize(obj))

    def _pick(self, data, *keys, default=None):
        for k in keys:
            if k in data and data[k] is not None:
                return data[k]
        return default

    def _parse_why_points(self, raw, fallback_list):
        if raw is None:
            return fallback_list
        if isinstance(raw, list):
            return [str(x).strip() for x in raw if str(x).strip()]
        if isinstance(raw, str):
            s = raw.strip()
            if not s:
                return []
            if s.startswith("["):
                try:
                    parsed = json.loads(s)
                    if isinstance(parsed, list):
                        return [str(x).strip() for x in parsed if str(x).strip()]
                except Exception:
                    pass
            return [line.strip() for line in s.splitlines() if line.strip()]
        return fallback_list

    def _parse_faq_items(self, raw, fallback_json_str):
        if raw is None:
            try:
                return json.loads(fallback_json_str)
            except Exception:
                return []
        if isinstance(raw, list):
            return raw
        if isinstance(raw, str):
            try:
                return json.loads(raw)
            except Exception:
                return []
        return []

    def post(self, request):
        """Create or replace the single courses-page content row (admin / public CMS)."""
        d = request.data
        obj = CoursesPageContent.objects.first()
        why_fallback = obj.why_points if obj else []
        faq_fallback = obj.faq_items if obj else "[]"
        hero_btn_fallback = obj.hero_cta_buttons if obj else []
        cta_btn_fallback = obj.cta_buttons if obj else []

        hero_title = self._pick(d, "hero_title", "heroTitle", default=(obj.hero_title if obj else ""))
        hero_subtitle = self._pick(d, "hero_subtitle", "heroSubtitle", default=(obj.hero_subtitle if obj else ""))
        hero_cta_buttons = self._parse_buttons(
            self._pick(d, "hero_cta_buttons", "heroCtaButtons"),
            hero_btn_fallback,
        )
        meta_title = self._pick(d, "meta_title", "metaTitle", default=(obj.meta_title if obj else ""))
        meta_description = self._pick(d, "meta_description", "metaDescription", default=(obj.meta_description if obj else ""))
        meta_keywords = self._pick(d, "meta_keywords", "metaKeywords", default=(obj.meta_keywords if obj else ""))
        why_title = self._pick(d, "why_title", "whyTitle", default=(obj.why_title if obj else ""))
        why_points = self._parse_why_points(
            self._pick(d, "why_points", "whyPoints"), why_fallback
        )
        cta_title = self._pick(d, "cta_title", "ctaTitle", default=(obj.cta_title if obj else ""))
        cta_subtitle = self._pick(d, "cta_subtitle", "ctaSubtitle", default=(obj.cta_subtitle if obj else ""))
        cta_buttons = self._parse_buttons(
            self._pick(d, "cta_buttons", "ctaButtons"),
            cta_btn_fallback,
        )
        faq_heading = self._pick(d, "faq_heading", "faqHeading", default=(obj.faq_heading if obj else ""))
        faq_intro = self._pick(d, "faq_intro", "faqIntro", default=(obj.faq_intro if obj else ""))
        faq_items_list = self._parse_faq_items(
            self._pick(d, "faq_items", "faqItems"), faq_fallback
        )
        faq_items_str = json.dumps(faq_items_list)

        if obj:
            obj.hero_title = hero_title
            obj.hero_subtitle = hero_subtitle
            obj.hero_cta_buttons = hero_cta_buttons
            obj.meta_title = meta_title
            obj.meta_description = meta_description
            obj.meta_keywords = meta_keywords
            obj.why_title = why_title
            obj.why_points = why_points
            obj.cta_title = cta_title
            obj.cta_subtitle = cta_subtitle
            obj.cta_buttons = cta_buttons
            obj.faq_heading = faq_heading
            obj.faq_intro = faq_intro
            obj.faq_items = faq_items_str
            obj.save()
        else:
            obj = CoursesPageContent.objects.create(
                hero_title=hero_title,
                hero_subtitle=hero_subtitle,
                hero_cta_buttons=hero_cta_buttons,
                meta_title=meta_title,
                meta_description=meta_description,
                meta_keywords=meta_keywords,
                why_title=why_title,
                why_points=why_points,
                cta_title=cta_title,
                cta_subtitle=cta_subtitle,
                cta_buttons=cta_buttons,
                faq_heading=faq_heading,
                faq_intro=faq_intro,
                faq_items=faq_items_str,
            )
        return Response(self._serialize(obj), status=status.HTTP_200_OK)


class CourseCounsellingSubmitView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CourseCounsellingLeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseCounsellingListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        leads = CourseCounsellingLead.objects.all().order_by("-created_at")
        serializer = CourseCounsellingLeadSerializer(leads, many=True)
        return Response(serializer.data)


class CourseCounsellingDetailView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, pk):
        try:
            lead = CourseCounsellingLead.objects.get(id=pk)
        except CourseCounsellingLead.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseCounsellingLeadSerializer(lead, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            lead = CourseCounsellingLead.objects.get(id=pk)
        except CourseCounsellingLead.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        lead.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
