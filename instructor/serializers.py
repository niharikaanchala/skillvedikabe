from rest_framework import serializers
from .models import (
    HeroSection,
    Feature,
    CTASection,
    FormSection,
    InstructorApplication,
)

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = "__all__"

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"

class CTASectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CTASection
        fields = "__all__"

class FormSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormSection
        fields = "__all__"


class InstructorApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorApplication
        fields = "__all__"
        read_only_fields = ["id", "created_at"]