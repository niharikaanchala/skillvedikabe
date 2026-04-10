from rest_framework import serializers
from .models import Hero, EmpowerSection, PortfolioItem, AdvantageItem, ProcessStep, DemoFormContent, MetaTags, SectionContent

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"

class EmpowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpowerSection
        fields = "__all__"

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioItem
        fields = "__all__"

class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvantageItem
        fields = "__all__"

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessStep
        fields = "__all__"

class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoFormContent
        fields = "__all__"


class MetaTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTags
        fields = "__all__"


class SectionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionContent
        fields = "__all__"