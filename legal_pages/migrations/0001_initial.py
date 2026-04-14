from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LegalPage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("page_type", models.CharField(choices=[("terms", "Terms & Conditions"), ("privacy", "Privacy Policy")], max_length=20, unique=True)),
                ("title", models.CharField(blank=True, default="", max_length=255)),
                ("content", models.TextField(blank=True, default="")),
                ("seo_meta_title", models.CharField(blank=True, default="", max_length=255)),
                ("seo_meta_description", models.TextField(blank=True, default="")),
                ("seo_meta_keywords", models.TextField(blank=True, default="")),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Legal Page",
                "verbose_name_plural": "Legal Pages",
            },
        ),
    ]

