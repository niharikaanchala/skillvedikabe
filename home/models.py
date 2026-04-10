from django.db import models

# ✅ Hero Section (fields aligned with migration 0002 — all editable from admin API)
class Hero(models.Model):
    heading = models.TextField(
        help_text="Use two lines: line 1 plain, line 2 is shown in brand blue.",
    )
    subheading = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="hero/", blank=True, null=True)
    cta_text = models.CharField(max_length=50, default="Get Started")
    cta_link = models.URLField(blank=True, null=True)
    highlights = models.TextField(
        blank=True,
        help_text="One highlight per line (shown with ✔). E.g. Upskill in SAP",
    )
    popular_tags = models.CharField(
        max_length=500,
        blank=True,
        help_text="Comma-separated tags under search.",
    )
    right_card_title = models.CharField(max_length=200, blank=True)
    right_card_subtitle = models.TextField(blank=True)
    search_placeholder = models.CharField(
        max_length=120,
        blank=True,
        default="Search by skill",
    )
    meta_title = models.CharField(max_length=255, blank=True, default="")
    meta_description = models.TextField(blank=True, default="")
    meta_keywords = models.TextField(
        blank=True,
        default="",
        help_text="Comma-separated SEO keywords for home page.",
    )

    def __str__(self):
        return self.heading[:80]


# ✅ Features Section
class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, blank=True)  # optional icon name

    def __str__(self):
        return self.title


# ✅ Why Choose Section
class WhyChoose(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)  # optional icon

    def __str__(self):
        return self.title


# ✅ Job Program Section
class JobProgram(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


# ✅ FAQ Section
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class SectionCopy(models.Model):
    SECTION_CHOICES = [
        ("features", "Features section"),
        ("why_choose", "Why choose section"),
        ("job_program", "Job program section"),
        ("faq", "FAQ section"),
    ]
    section = models.CharField(max_length=32, choices=SECTION_CHOICES, unique=True)
    heading = models.CharField(max_length=255, blank=True)
    intro = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Section copy"

    def __str__(self):
        return self.get_section_display()


class SupportSection(models.Model):
    heading = models.CharField(max_length=255)
    plan_tabs = models.CharField(
        max_length=255,
        blank=True,
        help_text="Comma-separated labels for tabs, e.g. hourly, weekly, monthly",
    )
    cta_text = models.CharField(max_length=80, default="Get Started", blank=True)
    cta_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Support section"

    def __str__(self):
        return self.heading


class SiteBranding(models.Model):
    brand_name = models.CharField(max_length=120, default="SkillVedika")
    logo = models.ImageField(upload_to="branding/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Site branding"

    def __str__(self):
        return self.brand_name