from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("on_job_support", "0009_sectioncontent_audience_eyebrow"),
    ]

    operations = [
        migrations.AlterField(
            model_name="metatags",
            name="meta_keywords",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="metatags",
            name="meta_title",
            field=models.TextField(blank=True, default=""),
        ),
    ]
