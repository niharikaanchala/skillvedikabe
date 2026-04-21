from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("legal_pages", "0002_expand_legal_page_types"),
    ]

    operations = [
        migrations.AlterField(
            model_name="legalpage",
            name="seo_meta_title",
            field=models.TextField(blank=True, default=""),
        ),
    ]
