from rest_framework import serializers
from .models import (
    CareerHero,
    CareerService,
    CareerSupport,
    CareerCTA,
    FAQ,
    CareerServicesHeading,
    MetaTags,
)


class CareerHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerHero
        fields = "__all__"


class CareerServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerService
        fields = "__all__"


class CareerSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerSupport
        fields = "__all__"


class CareerCTASerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerCTA
        fields = "__all__"


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


class MetaTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTags
        fields = "__all__"


class CareerServicesHeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerServicesHeading
        fields = "__all__"