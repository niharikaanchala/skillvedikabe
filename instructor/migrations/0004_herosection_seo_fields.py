from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instructor", "0003_instructorapplication_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="herosection",
            name="seo_meta_description",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="herosection",
            name="seo_meta_keywords",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="herosection",
            name="seo_meta_title",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]

