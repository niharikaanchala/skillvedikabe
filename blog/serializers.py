from rest_framework import serializers
from .models import BlogPost, BlogParagraph, TableOfContent, MetaTags


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogParagraph
        fields = ["content"]


class TocSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableOfContent
        fields = ["title"]


class BlogPostSerializer(serializers.ModelSerializer):
    paragraphs = ParagraphSerializer(many=True, read_only=True)
    toc = TocSerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "slug",
            "category",
            "title",
            "author",
            "date",
            "read_time",
            "excerpt",
            "image",
            "image_url",
            "paragraphs",
            "toc",
            "meta_title",
            "meta_description",
            "meta_keywords",
        ]
        extra_kwargs = {
            "image": {"required": False, "allow_null": True},
            "image_url": {"required": False},
        }

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and hasattr(obj.image, "url"):
            url = obj.image.url
            if request is not None and url.startswith("/"):
                return request.build_absolute_uri(url)
            return url
        return obj.image_url or ""

class MetaTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTags
        fields = "__all__"