from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0003_contacthero_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="metatags",
            name="meta_keywords",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="metatags",
            name="meta_title",
            field=models.TextField(),
        ),
    ]
