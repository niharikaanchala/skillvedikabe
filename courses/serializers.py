import json
from rest_framework import serializers
from .models import Course, CoursesPageContent, CourseCounsellingLead

class CourseSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class CoursesPageContentSerializer(serializers.ModelSerializer):
    whyItems = serializers.SerializerMethodField()
    faqItems = serializers.SerializerMethodField()

    class Meta:
        model = CoursesPageContent
        fields = "__all__"

    def get_whyItems(self, obj):
        # JSONField is already a list, return as-is
        return obj.why_points if obj.why_points else []

    def get_faqItems(self, obj):
        try:
            return json.loads(obj.faq_items)
        except Exception:
            return []


class CourseCounsellingLeadSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source="course.title", read_only=True)
    course_slug = serializers.CharField(source="course.slug", read_only=True)

    class Meta:
        model = CourseCounsellingLead
        fields = "__all__"
        read_only_fields = ["id", "created_at", "course_title", "course_slug"]