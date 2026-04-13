from django.contrib import admin
from .models import SiteSetting

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("id", "google_analytics_id")
    list_editable = ("google_analytics_id",)
    search_fields = ("google_analytics_id",)