from django.db import models


class LegalPage(models.Model):
    PAGE_CHOICES = [
        ("terms", "Terms & Conditions"),
        ("privacy", "Privacy Policy"),
        ("disclaimer", "Disclaimer"),
        ("editorial-policy", "Editorial Policy"),
    ]

    page_type = models.CharField(max_length=20, choices=PAGE_CHOICES, unique=True)
    title = models.CharField(max_length=255, blank=True, default="")
    content = models.TextField(blank=True, default="")
    seo_meta_title = models.TextField(blank=True, default="")
    seo_meta_description = models.TextField(blank=True, default="")
    seo_meta_keywords = models.TextField(blank=True, default="")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Legal Page"
        verbose_name_plural = "Legal Pages"

    def __str__(self):
        return f"{self.page_type} page"

