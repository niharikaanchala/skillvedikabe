from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import SiteSetting
from .serializers import SiteSettingSerializer


# ✅ GET ALL SETTINGS
@api_view(["GET"])
def get_settings(request):
    settings = SiteSetting.objects.all()
    serializer = SiteSettingSerializer(settings, many=True)
    return Response(serializer.data)


# ✅ GET SINGLE SETTING
@api_view(["GET"])
def get_setting(request, pk):
    try:
        setting = SiteSetting.objects.get(pk=pk)
        serializer = SiteSettingSerializer(setting)
        return Response(serializer.data)
    except SiteSetting.DoesNotExist:
        return Response({"error": "Not found"}, status=404)


# ✅ CREATE
@api_view(["POST"])
def create_setting(request):
    serializer = SiteSettingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# ✅ UPDATE (PUT)
@api_view(["PUT"])
def update_setting(request, pk):
    try:
        print(pk)
        setting = SiteSetting.objects.get(pk=pk)
    except SiteSetting.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    serializer = SiteSettingSerializer(setting, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# ✅ DELETE
@api_view(["DELETE"])
def delete_setting(request, pk):
    try:
        setting = SiteSetting.objects.get(pk=pk)
        setting.delete()
        return Response({"message": "Deleted successfully"})
    except SiteSetting.DoesNotExist:
        return Response({"error": "Not found"}, status=404)