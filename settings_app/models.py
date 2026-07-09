from django.db import models

class SiteSetting(models.Model):
    google_analytics_id = models.CharField(max_length=50, blank=True, null=True)
    whatsapp_number = models.CharField(
        max_length=20,
        blank=True,
        default="",
        help_text="Country code + number without + or spaces, e.g. 919381193375",
    )
    whatsapp_message = models.TextField(
        blank=True,
        default="",
        help_text="Pre-filled WhatsApp message (plain text; will be URL-encoded on the site)",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.google_analytics_id or "Settings"