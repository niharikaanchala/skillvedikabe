from django.db import models


# 🔷 1. HERO SECTION
class CareerHero(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()

    primary_button_text = models.CharField(max_length=100)
    primary_button_link = models.CharField(max_length=255, blank=True)

    secondary_button_text = models.CharField(max_length=100)
    secondary_button_link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


# 🔷 2. CAREER SERVICES SECTION
class CareerService(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


# 🔷 3. WHY CAREER SUPPORT MATTERS SECTION
class CareerSupport(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


# 🔷 4. CTA SECTION (CALL TO ACTION)
class CareerCTA(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()

    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


# 🔷 5. FAQ SECTION
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


# 🔷 META TAGS (SEO)
class MetaTags(models.Model):
    meta_title = models.TextField(blank=True, default="")
    meta_description = models.TextField(blank=True, default="")
    meta_keywords = models.TextField(blank=True, default="")

    def __str__(self):
        return self.meta_title or "MetaTags"


# 🔷 SERVICES SECTION HEADING (Singleton)
class CareerServicesHeading(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


