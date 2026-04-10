from django.db import models

# HERO
class ContactHero(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    button_text = models.CharField(max_length=100)
    background_color = models.CharField(max_length=7, default="#EAF2FC")
    image = models.ImageField(
        upload_to="contact/hero/",
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.title


# CONTACT INFO CARDS
class ContactInfo(models.Model):
    TYPE_CHOICES = (
        ("email", "Email"),
        ("phone", "Phone"),
        ("address", "Address"),
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    label = models.CharField(max_length=100)   # Email us / Call us
    value = models.CharField(max_length=255)   # actual data
    link = models.CharField(max_length=255, blank=True)  # mailto / tel
    icon = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.label


# DEMO SECTION
class DemoSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    points = models.JSONField()  # list of bullet points

    def __str__(self):
        return self.title


# FORM SECTION
class ContactFormSection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    button_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class MetaTags(models.Model):
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.CharField(max_length=255)

    def __str__(self):
        return self.meta_title
