from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_hero_meta_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="sectioncopy",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="section_copy/"),
        ),
    ]
