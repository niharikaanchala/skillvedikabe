from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0004_categorypagecontent_seo_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="When False, the category is hidden from the public site.",
            ),
        ),
    ]
