from django.db import models

class Hero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=200, default="#", blank=True)
    image = models.ImageField(upload_to="hero/", blank=True, null=True)

class RealTimeHelp(models.Model):
    title_main = models.CharField(max_length=200)
    title_sub = models.CharField(max_length=200)
    description = models.TextField()
    icon_1_title = models.CharField(max_length=100)
    icon_1_desc = models.CharField(max_length=200)
    icon_2_title = models.CharField(max_length=100)
    icon_2_desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to="help/", blank=True, null=True)

# We already have these:
class Audience(models.Model):
    tag = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    desc = models.TextField()

class Help(models.Model):
    icon = models.CharField(max_length=100, blank=True, default="")
    title = models.CharField(max_length=200)
    desc = models.TextField()

class Step(models.Model):
    order = models.PositiveIntegerField()
    desc = models.CharField(max_length=500)

    class Meta:
        ordering = ['order']

class WhyChoose(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    points = models.JSONField(default=list)  # store list of reasons
    image = models.ImageField(upload_to="why/", blank=True, null=True)

class Demo(models.Model):
    badge = models.CharField(max_length=100, blank=True, null=True)
    title_main = models.CharField(max_length=255)
    title_highlight = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    features = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.title_main

class DemoRequest(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    agree_terms = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


# 🔷 META TAGS (SEO)
class MetaTags(models.Model):
    meta_title = models.CharField(max_length=255, blank=True, default="")
    meta_description = models.TextField(blank=True, default="")
    meta_keywords = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return self.meta_title or "MetaTags"


class SectionContent(models.Model):
    audience_eyebrow = models.CharField(max_length=120, blank=True, default="")
    audience_title = models.CharField(max_length=255, blank=True, default="")
    audience_description = models.TextField(blank=True, default="")
    help_title = models.CharField(max_length=255, blank=True, default="")
    process_title = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return "On Job Support Section Content"