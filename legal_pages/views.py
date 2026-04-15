from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import LegalPage
from .serializers import LegalPageSerializer


class LegalPageTypeAPIView(APIView):
    page_type = ""

    def get(self, request):
        obj = LegalPage.objects.filter(page_type=self.page_type).first()
        if not obj:
            return Response([])
        return Response([LegalPageSerializer(obj).data])

    def post(self, request):
        obj = LegalPage.objects.filter(page_type=self.page_type).first()
        payload = dict(request.data)
        payload["page_type"] = self.page_type
        if obj:
            serializer = LegalPageSerializer(obj, data=payload, partial=True)
        else:
            serializer = LegalPageSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LegalPageTypeDetailAPIView(APIView):
    page_type = ""

    def put(self, request, pk):
        try:
            obj = LegalPage.objects.get(pk=pk, page_type=self.page_type)
        except LegalPage.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        payload = dict(request.data)
        payload["page_type"] = self.page_type
        serializer = LegalPageSerializer(obj, data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TermsPageAPIView(LegalPageTypeAPIView):
    page_type = "terms"


class TermsPageDetailAPIView(LegalPageTypeDetailAPIView):
    page_type = "terms"


class PrivacyPageAPIView(LegalPageTypeAPIView):
    page_type = "privacy"


class PrivacyPageDetailAPIView(LegalPageTypeDetailAPIView):
    page_type = "privacy"


class DisclaimerPageAPIView(LegalPageTypeAPIView):
    page_type = "disclaimer"


class DisclaimerPageDetailAPIView(LegalPageTypeDetailAPIView):
    page_type = "disclaimer"


class EditorialPolicyPageAPIView(LegalPageTypeAPIView):
    page_type = "editorial-policy"


class EditorialPolicyPageDetailAPIView(LegalPageTypeDetailAPIView):
    page_type = "editorial-policy"

