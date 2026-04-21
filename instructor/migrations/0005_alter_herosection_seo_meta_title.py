from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instructor", "0004_herosection_seo_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="herosection",
            name="seo_meta_title",
            field=models.TextField(blank=True, default=""),
        ),
    ]
