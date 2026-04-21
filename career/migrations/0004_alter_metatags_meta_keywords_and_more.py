from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("career", "0003_careerservicesheading"),
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
