from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_section_copy_faq_choice"),
    ]

    operations = [
        migrations.CreateModel(
            name="SiteBranding",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand_name", models.CharField(default="SkillVedika", max_length=120)),
                ("logo", models.ImageField(blank=True, null=True, upload_to="branding/")),
            ],
            options={"verbose_name_plural": "Site branding"},
        ),
    ]
