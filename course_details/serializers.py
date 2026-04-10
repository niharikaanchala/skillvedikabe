# courses/serializers.py
from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
        read_only_fields = ['course'] 

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = "__all__"
        read_only_fields = ['course'] 

class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = "__all__"
        read_only_fields = ['course'] 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ['course'] 

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = "__all__"
        read_only_fields = ['course'] 

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"
        read_only_fields = ['course'] 

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"
        read_only_fields = ['course'] 

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        read_only_fields = ['course'] 

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"
        read_only_fields = ['course'] 


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"
        read_only_fields = ["course"]


class PlacementSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementSupport
        fields = "__all__"
        read_only_fields = ["course"]


class CorporateTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorporateTraining
        fields = "__all__"
        read_only_fields = ["course"]


class CourseSectionMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSectionMeta
        fields = "__all__"
        read_only_fields = ["course"]