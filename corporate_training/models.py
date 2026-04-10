from django.db import models

class Hero(models.Model):
    title = models.CharField(max_length=255)
    highlight = models.CharField(max_length=255, blank=True, default="")
    subtitle = models.TextField(blank=True, null=True)
    button_text = models.CharField(max_length=100)
    button_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="corporate/hero/", blank=True, null=True)

class EmpowerSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="corporate/empower/", blank=True, null=True)

class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class AdvantageItem(models.Model):
    icon = models.CharField(max_length=100, blank=True, default="")
    title = models.CharField(max_length=255)
    description = models.TextField()

class ProcessStep(models.Model):
    icon = models.CharField(max_length=100, blank=True, default="")
    title = models.CharField(max_length=255)
    description = models.TextField()

class DemoFormContent(models.Model):
    title = models.CharField(max_length=255)
    points = models.JSONField(default=list)  # store bullet points
    button_text = models.CharField(max_length=100)


# 🔷 META TAGS (SEO)
class MetaTags(models.Model):
    meta_title = models.CharField(max_length=255, blank=True, default="")
    meta_description = models.TextField(blank=True, default="")
    meta_keywords = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return self.meta_title or "MetaTags"


class SectionContent(models.Model):
    empower_title = models.CharField(max_length=255, blank=True, default="")
    empower_subtitle = models.TextField(blank=True, default="")
    portfolio_title = models.CharField(max_length=255, blank=True, default="")
    portfolio_subtitle = models.TextField(blank=True, default="")
    advantage_title = models.CharField(max_length=255, blank=True, default="")
    advantage_subtitle = models.TextField(blank=True, default="")
    process_title = models.CharField(max_length=255, blank=True, default="")
    process_subtitle = models.TextField(blank=True, default="")
    demo_title = models.CharField(max_length=255, blank=True, default="")
    demo_subtitle = models.TextField(blank=True, default="")

    def __str__(self):
        return "Corporate Training Section Content"