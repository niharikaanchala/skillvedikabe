from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corporate_training", "0007_sectioncontent_demo_subtitle_and_more"),
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
