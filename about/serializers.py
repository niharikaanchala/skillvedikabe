from rest_framework import serializers

from .models import AboutHero, CtaSection, DemoSection, ValueItem, ValuesSection, MetaTags


class AboutHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHero
        fields = "__all__"


class ValuesSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValuesSection
        fields = "__all__"


class ValueItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueItem
        fields = "__all__"


class CtaSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CtaSection
        fields = "__all__"


class DemoSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoSection
        fields = "__all__"


class MetaTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTags
        fields = "__all__"
