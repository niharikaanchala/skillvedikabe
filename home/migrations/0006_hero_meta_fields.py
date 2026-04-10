from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_sitebranding"),
    ]

    operations = [
        migrations.AddField(
            model_name="hero",
            name="meta_description",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="hero",
            name="meta_keywords",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Comma-separated SEO keywords for home page.",
            ),
        ),
        migrations.AddField(
            model_name="hero",
            name="meta_title",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]

