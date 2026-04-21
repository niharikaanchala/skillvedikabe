from django.db import models


class AboutHero(models.Model):
    heading = models.CharField(max_length=255, default="About Us")
    paragraph_one = models.TextField(blank=True)
    paragraph_two = models.TextField(blank=True)
    hero_image = models.ImageField(upload_to="about/hero/", blank=True, null=True)

    def __str__(self):
        return self.heading


class ValuesSection(models.Model):
    heading = models.CharField(max_length=255, default="Our Values")
    subtitle = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Values section"

    def __str__(self):
        return self.heading


class ValueItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class CtaSection(models.Model):
    heading = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True)
    primary_button_text = models.CharField(max_length=100, default="Get Started")
    primary_button_link = models.URLField(blank=True, null=True)
    secondary_button_text = models.CharField(max_length=100, default="Contact Us")
    secondary_button_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "CTA section"

    def __str__(self):
        return self.heading


class DemoSection(models.Model):
    heading = models.CharField(max_length=255, default="Get a Live Free demo")
    features = models.JSONField(default=list, blank=True)
    tag_lines = models.JSONField(default=list, blank=True)
    form_title = models.CharField(max_length=255, default="Book Your Free Demo")
    form_subtitle = models.CharField(max_length=255, blank=True)
    courses = models.JSONField(default=list, blank=True)
    submit_button_text = models.CharField(max_length=100, default="Submit Your Details")

    class Meta:
        verbose_name_plural = "Demo section"

    def __str__(self):
        return self.heading


# 🔷 META TAGS (SEO)
class MetaTags(models.Model):
    meta_title = models.TextField(blank=True, default="")
    meta_description = models.TextField(blank=True, default="")
    meta_keywords = models.TextField(blank=True, default="")

    def __str__(self):
        return self.meta_title or "MetaTags"
