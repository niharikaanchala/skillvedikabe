from rest_framework import serializers
from .models import Hero, RealTimeHelp, Audience, Help, Step, WhyChoose, Demo, DemoRequest, MetaTags, SectionContent

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"

class RealTimeHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealTimeHelp
        fields = "__all__"

class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience
        fields = "__all__"

class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = "__all__"

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = "__all__"

class WhyChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChoose
        fields = "__all__"

class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = "__all__"

class DemoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoRequest
        fields = "__all__"


class MetaTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTags
        fields = "__all__"


class SectionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionContent
        fields = "__all__"