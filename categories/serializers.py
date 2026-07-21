from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {
            "is_active": {"required": False},
            "description": {"required": False, "allow_blank": True},
            "icon": {"required": False, "allow_blank": True, "allow_null": True},
        }