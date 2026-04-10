from django.db import models
from categories.models import Category

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    rating = models.FloatField(default=0)
    seo_meta_title = models.CharField(max_length=255, blank=True, default="")
    seo_meta_description = models.TextField(blank=True, default="")
    seo_meta_keywords = models.TextField(blank=True, default="")

    # 🔥 Relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return self.title


class CoursesPageContent(models.Model):
    # Hero
    hero_title = models.CharField(max_length=255)
    hero_subtitle = models.TextField()
    hero_cta_buttons = models.JSONField(
        default=list,
        blank=True,
        help_text='List of CTA buttons for hero: [{"text": "...", "link": "..."}]',
    )
    meta_title = models.CharField(max_length=255, blank=True, default="")
    meta_description = models.TextField(blank=True, default="")
    meta_keywords = models.TextField(
        blank=True,
        default="",
        help_text="Comma-separated SEO keywords for /courses page",
    )

    # Why Learn / Why Invest
    why_title = models.CharField(max_length=255)
    why_points = models.JSONField(default=list, help_text="List of points")

    # CTA
    cta_title = models.CharField(max_length=255)
    cta_subtitle = models.TextField()
    cta_buttons = models.JSONField(
        default=list,
        blank=True,
        help_text='List of CTA buttons: [{"text": "...", "link": "...", "variant": "primary|secondary"}]',
    )

    # FAQ
    faq_heading = models.CharField(max_length=255)
    faq_intro = models.TextField()
    faq_items = models.TextField(
        help_text="JSON format: [{\"question\": \"...\", \"answer\": \"...\"}]",
        default="[]"
    )

    def __str__(self):
        return "Courses Page Content"


class CourseCounsellingLead(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="counselling_leads",
    )
    first_name = models.CharField(max_length=120, blank=True, default="")
    last_name = models.CharField(max_length=120, blank=True, default="")
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    years_of_experience = models.CharField(max_length=60, blank=True, default="")
    skills = models.TextField(blank=True, default="")
    message = models.TextField(blank=True)
    agreed_to_terms = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.course.title if self.course else 'General'}"