from rest_framework import serializers
from .models import *

class ContactHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactHero
        fields = "__all__"


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"


class DemoSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoSection
        fields = "__all__"


class ContactFormSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormSection
        fields = "__all__"

class MetaTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTags
        fields = "__all__"