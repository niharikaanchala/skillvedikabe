from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0008_coursespagecontent_seo_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="seo_meta_description",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="course",
            name="seo_meta_keywords",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="course",
            name="seo_meta_title",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]
