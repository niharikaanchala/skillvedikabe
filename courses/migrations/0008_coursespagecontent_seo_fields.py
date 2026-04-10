from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0007_coursecounsellinglead_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="coursespagecontent",
            name="meta_description",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="coursespagecontent",
            name="meta_keywords",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Comma-separated SEO keywords for /courses page",
            ),
        ),
        migrations.AddField(
            model_name="coursespagecontent",
            name="meta_title",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]

