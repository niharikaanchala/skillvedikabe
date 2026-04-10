from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    icon = models.CharField(max_length=50, blank=True, null=True)  # optional

    def __str__(self):
        return self.name


class CategoryPageContent(models.Model):
    """
    CMS content that is unique per category page (/courses/<category-slug>/).

    Kept in `categories` app so it can be keyed by Category.
    """

    category = models.OneToOneField(
        Category, on_delete=models.CASCADE, related_name="page_content"
    )

    # Hero
    hero_title = models.CharField(max_length=255, blank=True, default="")
    hero_subtitle = models.TextField(blank=True, default="")
    hero_cta_text = models.CharField(max_length=255, blank=True, default="")
    hero_cta_link = models.CharField(max_length=500, blank=True, default="")

    # SEO (per category page)
    seo_title = models.CharField(max_length=255, blank=True, default="")
    seo_description = models.TextField(blank=True, default="")
    seo_keywords = models.TextField(
        blank=True,
        default="",
        help_text="Comma-separated SEO keywords for the category page",
    )

    # Why Learn
    why_title = models.CharField(max_length=255, blank=True, default="")
    why_points = models.JSONField(default=list, blank=True)

    # CTA
    cta_title = models.CharField(max_length=255, blank=True, default="")
    cta_subtitle = models.TextField(blank=True, default="")
    cta_buttons = models.JSONField(default=list, blank=True)

    # FAQ
    faq_heading = models.CharField(max_length=255, blank=True, default="")
    faq_intro = models.TextField(blank=True, default="")
    faq_items = models.JSONField(default=list, blank=True)

    class Meta:
        verbose_name = "Category Page Content"
        verbose_name_plural = "Category Page Contents"

    def __str__(self):
        return f"CategoryPageContent({self.category_id})"