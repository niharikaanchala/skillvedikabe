import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from .models import BlogPost, BlogParagraph, TableOfContent, MetaTags
from .serializers import (
    BlogPostSerializer,
    ParagraphSerializer,
    TocSerializer,
    MetaTagsSerializer,
)

# ----------------------------
# GET ALL + CREATE BLOG (with paragraphs & TOC)
# ----------------------------
class BlogListView(APIView):
    parser_classes = [JSONParser, FormParser, MultiPartParser]

    def _coerce_items(self, value):
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            try:
                parsed = json.loads(value)
                return parsed if isinstance(parsed, list) else []
            except Exception:
                return []
        return []

    def get(self, request):
        blogs = BlogPost.objects.all().order_by('-date')
        serializer = BlogPostSerializer(blogs, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        # Expect JSON with optional paragraphs and toc
        serializer = BlogPostSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            blog = serializer.save()

            # Save paragraphs if provided
            paragraphs_data = self._coerce_items(request.data.get('paragraphs', []))
            for p in paragraphs_data:
                BlogParagraph.objects.create(post=blog, **p)

            # Save table of contents if provided
            toc_data = self._coerce_items(request.data.get('toc', []))
            for t in toc_data:
                TableOfContent.objects.create(post=blog, **t)

            # Return full blog with nested paragraphs & toc
            full_blog = BlogPostSerializer(blog, context={"request": request})
            return Response(full_blog.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ----------------------------
# GET ONE + UPDATE + DELETE SINGLE BLOG
# ----------------------------
class BlogDetailView(APIView):
    parser_classes = [JSONParser, FormParser, MultiPartParser]

    def _coerce_items(self, value):
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            try:
                parsed = json.loads(value)
                return parsed if isinstance(parsed, list) else []
            except Exception:
                return []
        return []

    def get_object(self, slug):
        try:
            return BlogPost.objects.get(slug=slug)
        except BlogPost.DoesNotExist:
            return None

    def get(self, request, slug):
        blog = self.get_object(slug)
        if not blog:
            return Response({"error": "Blog not found"}, status=404)
        serializer = BlogPostSerializer(blog, context={"request": request})
        return Response(serializer.data)

    def put(self, request, slug):
        blog = self.get_object(slug)
        if not blog:
            return Response({"error": "Blog not found"}, status=404)

        serializer = BlogPostSerializer(blog, data=request.data, context={"request": request})
        if serializer.is_valid():
            blog = serializer.save()

            # Update paragraphs if provided
            paragraphs_data = self._coerce_items(request.data.get('paragraphs', []))
            blog.paragraphs.all().delete()  # delete old paragraphs
            for p in paragraphs_data:
                BlogParagraph.objects.create(post=blog, **p)

            # Update TOC if provided
            toc_data = self._coerce_items(request.data.get('toc', []))
            blog.toc.all().delete()  # delete old TOC
            for t in toc_data:
                TableOfContent.objects.create(post=blog, **t)

            full_blog = BlogPostSerializer(blog, context={"request": request})
            return Response(full_blog.data)

        return Response(serializer.errors, status=400)

    def patch(self, request, slug):
        blog = self.get_object(slug)
        if not blog:
            return Response({"error": "Blog not found"}, status=404)

        serializer = BlogPostSerializer(blog, data=request.data, partial=True, context={"request": request})
        if serializer.is_valid():
            blog = serializer.save()

            # Optional partial update for paragraphs
            if 'paragraphs' in request.data:
                blog.paragraphs.all().delete()
                for p in self._coerce_items(request.data['paragraphs']):
                    BlogParagraph.objects.create(post=blog, **p)

            # Optional partial update for TOC
            if 'toc' in request.data:
                blog.toc.all().delete()
                for t in self._coerce_items(request.data['toc']):
                    TableOfContent.objects.create(post=blog, **t)

            full_blog = BlogPostSerializer(blog, context={"request": request})
            return Response(full_blog.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, slug):
        blog = self.get_object(slug)
        if not blog:
            return Response({"error": "Blog not found"}, status=404)
        blog.delete()
        return Response({"message": "Blog deleted successfully"}, status=204)


# ----------------------------
# BULK DELETE BLOGS
# ----------------------------
class BlogBulkDeleteView(APIView):

    def delete(self, request):
        ids = request.data.get("ids", [])
        if not ids:
            return Response({"error": "No IDs provided"}, status=400)

        deleted_count, _ = BlogPost.objects.filter(id__in=ids).delete()
        return Response({
            "message": f"{deleted_count} blogs deleted successfully"
        })

# ----------------------------
# META TAGS (SEO)
# ----------------------------
class MetaTagsAPI(APIView):
    def get(self, request):
        meta_obj = MetaTags.objects.order_by("id").first()
        return Response(MetaTagsSerializer(meta_obj).data if meta_obj else {})

    def post(self, request):
        serializer = MetaTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    def put(self, request):
        obj = MetaTags.objects.order_by("id").first()
        if not obj:
            serializer = MetaTagsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        serializer = MetaTagsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

# ----------------------------
# META TAGS DETAIL
# ----------------------------
class MetaTagsDetailAPI(APIView):
    def get(self, request, pk):
        obj = MetaTags.objects.get(id=pk)
        return Response(MetaTagsSerializer(obj).data)
    def put(self, request, pk):
        obj = MetaTags.objects.get(id=pk)
        serializer = MetaTagsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    def delete(self, request, pk):
        obj = MetaTags.objects.get(id=pk)
        obj.delete()
        return Response({"message": "MetaTags deleted successfully"}, status=204)
    