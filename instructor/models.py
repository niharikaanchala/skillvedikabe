from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True)
    button_primary_text = models.CharField(max_length=100, default="Apply Now")
    button_secondary_text = models.CharField(max_length=100, default="Learn More")
    background_color = models.CharField(max_length=7, default="#EAF0F8")
    text_color = models.CharField(max_length=7, default="#0C1A35")
    seo_meta_title = models.CharField(max_length=255, blank=True, default="")
    seo_meta_description = models.TextField(blank=True, default="")
    seo_meta_keywords = models.TextField(blank=True, default="")

    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=10)  # e.g. emoji or symbol

    def __str__(self):
        return self.title

class CTASection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True)
    button_text = models.CharField(max_length=100)
    background_color = models.CharField(max_length=7, default="#EAF0F8")
    text_color = models.CharField(max_length=7, default="#1E3A68")

    def __str__(self):
        return self.title

class FormSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True)
    submit_button_text = models.CharField(max_length=100, default="Submit Application")

    def __str__(self):
        return self.title


class InstructorApplication(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    years_of_experience = models.CharField(max_length=60)
    skills = models.TextField(help_text="Comma-separated skills")
    message = models.TextField(blank=True)
    agreed_to_terms = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"