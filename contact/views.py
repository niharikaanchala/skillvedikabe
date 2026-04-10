from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# -------- HERO --------
class ContactHeroAPI(APIView):
    def get(self, request):
        return Response(ContactHeroSerializer(ContactHero.objects.all(), many=True).data)

    def post(self, request):
        serializer = ContactHeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ContactHeroDetailAPI(APIView):
    def get(self, request, pk):
        obj = ContactHero.objects.get(id=pk)
        return Response(ContactHeroSerializer(obj).data)

    def put(self, request, pk):
        obj = ContactHero.objects.get(id=pk)
        serializer = ContactHeroSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        ContactHero.objects.get(id=pk).delete()
        return Response({"message": "Deleted"})


# -------- CONTACT INFO --------
class ContactInfoAPI(APIView):
    def get(self, request):
        return Response(ContactInfoSerializer(ContactInfo.objects.all(), many=True).data)

    def post(self, request):
        serializer = ContactInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ContactInfoDetailAPI(APIView):
    def get(self, request, pk):
        obj = ContactInfo.objects.get(id=pk)
        return Response(ContactInfoSerializer(obj).data)

    def put(self, request, pk):
        obj = ContactInfo.objects.get(id=pk)
        serializer = ContactInfoSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        ContactInfo.objects.get(id=pk).delete()
        return Response({"message": "Deleted"})


# ✅ BULK CREATE
class ContactInfoBulkCreateAPI(APIView):
    def post(self, request):
        serializer = ContactInfoSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


# ✅ BULK DELETE
class ContactInfoBulkDeleteAPI(APIView):
    def delete(self, request):
        ids = request.data.get("ids", [])
        ContactInfo.objects.filter(id__in=ids).delete()
        return Response({"message": "Bulk deleted successfully"})


# -------- DEMO --------
class DemoAPI(APIView):
    def get(self, request):
        return Response(DemoSectionSerializer(DemoSection.objects.all(), many=True).data)

    def post(self, request):
        serializer = DemoSectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class DemoDetailAPI(APIView):
    def get(self, request, pk):
        obj = DemoSection.objects.get(id=pk)
        return Response(DemoSectionSerializer(obj).data)

    def put(self, request, pk):
        obj = DemoSection.objects.get(id=pk)
        serializer = DemoSectionSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        DemoSection.objects.get(id=pk).delete()
        return Response({"message": "Deleted"})


# -------- FORM --------
class ContactFormAPI(APIView):
    def get(self, request):
        return Response(ContactFormSectionSerializer(ContactFormSection.objects.all(), many=True).data)

    def post(self, request):
        serializer = ContactFormSectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ContactFormDetailAPI(APIView):
    def get(self, request, pk):
        obj = ContactFormSection.objects.get(id=pk)
        return Response(ContactFormSectionSerializer(obj).data)

    def put(self, request, pk):
        obj = ContactFormSection.objects.get(id=pk)
        serializer = ContactFormSectionSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        ContactFormSection.objects.get(id=pk).delete()
        return Response({"message": "Deleted"})


# -------- FULL PAGE API --------
class ContactPageAPI(APIView):
    def get(self, request):
        return Response(
            {
                "meta": MetaTagsSerializer(MetaTags.objects.first()).data
                if MetaTags.objects.exists()
                else {},
                "hero": ContactHeroSerializer(ContactHero.objects.first()).data
                if ContactHero.objects.exists()
                else {},
                "contact_info": ContactInfoSerializer(
                    ContactInfo.objects.all(), many=True
                ).data,
                "demo": DemoSectionSerializer(DemoSection.objects.first()).data
                if DemoSection.objects.exists()
                else {},
                "form": ContactFormSectionSerializer(
                    ContactFormSection.objects.first()
                ).data
                if ContactFormSection.objects.exists()
                else {},
            }
        )

# -------- META TAGS --------
class MetaTagsAPI(APIView):
    def get(self, request):
        return Response(MetaTagsSerializer(MetaTags.objects.first()).data)

    def post(self, request):
        serializer = MetaTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def put(self, request):
        obj = MetaTags.objects.first()
        serializer = MetaTagsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        MetaTags.objects.all().delete()
        return Response({"message": "Deleted"})

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
    
    def delete(self, request, pk):
        MetaTags.objects.get(id=pk).delete()
        return Response({"message": "Deleted"})

class MetaTagsBulkDeleteAPI(APIView):
    def delete(self, request):
        ids = request.data.get("ids", [])
        MetaTags.objects.filter(id__in=ids).delete()
        return Response({"message": "Bulk deleted successfully"})

class MetaTagsDeleteAPI(APIView):
    def delete(self, request):
        MetaTags.objects.all().delete()
        return Response({"message": "Deleted"})