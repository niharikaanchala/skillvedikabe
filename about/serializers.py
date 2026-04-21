from rest_framework import serializers

from .models import AboutHero, CtaSection, DemoSection, ValueItem, ValuesSection, MetaTags


class AboutHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHero
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.hero_image and hasattr(instance.hero_image, "url"):
            data["hero_image"] = instance.hero_image.url
        else:
            data["hero_image"] = None
        return data


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
