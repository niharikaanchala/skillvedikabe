from rest_framework import serializers
from .models import Hero, Feature, WhyChoose, JobProgram, FAQ, SectionCopy, SupportSection, SiteBranding

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"
        extra_kwargs = {
            "image": {"required": False, "allow_null": True},
            "subheading": {"required": False, "allow_blank": True},
            "cta_link": {"required": False, "allow_null": True, "allow_blank": True},
            "highlights": {"required": False, "allow_blank": True},
            "popular_tags": {"required": False, "allow_blank": True},
            "right_card_title": {"required": False, "allow_blank": True},
            "right_card_subtitle": {"required": False, "allow_blank": True},
            "search_placeholder": {"required": False, "allow_blank": True},
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        if instance.image and hasattr(instance.image, "url"):
            url = instance.image.url
            if request is not None and url.startswith("/"):
                data["image"] = request.build_absolute_uri(url)
            else:
                data["image"] = url
        else:
            data["image"] = None
        return data

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"
        extra_kwargs = {
            "description": {"allow_blank": True, "required": False},
            "icon": {"allow_blank": True, "required": False},
        }


class WhyChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChoose
        fields = "__all__"
        extra_kwargs = {
            "icon": {"allow_blank": True, "required": False},
        }


class JobProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobProgram
        fields = "__all__"
        extra_kwargs = {
            "description": {"allow_blank": True, "required": False},
        }

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


class SectionCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionCopy
        fields = "__all__"
        extra_kwargs = {
            "heading": {"allow_blank": True, "required": False},
            "intro": {"allow_blank": True, "required": False},
        }


class SupportSectionSerializer(serializers.ModelSerializer):
    tabs = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SupportSection
        fields = ("id", "heading", "plan_tabs", "cta_text", "cta_link", "tabs")
        extra_kwargs = {
            "plan_tabs": {"required": False, "allow_blank": True},
            "cta_text": {"required": False, "allow_blank": True},
            "cta_link": {"required": False, "allow_null": True, "allow_blank": True},
        }

    def get_tabs(self, obj):
        if not obj.plan_tabs:
            return []
        return [t.strip() for t in obj.plan_tabs.split(",") if t.strip()]


class SiteBrandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteBranding
        fields = "__all__"
        extra_kwargs = {
            "logo": {"required": False, "allow_null": True},
            "brand_name": {"required": False, "allow_blank": True},
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Always expose logo as a site-relative path (e.g. /media/branding/...).
        # Next.js (and admin) proxy /media/* to Django so the image loads on the same
        # origin as the app. build_absolute_uri() would often point at the wrong host
        # when the API is called through a reverse proxy.
        if instance.logo and hasattr(instance.logo, "url"):
            data["logo"] = instance.logo.url
        else:
            data["logo"] = None
        return data