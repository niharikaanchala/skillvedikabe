from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0007_sectioncopy_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sectioncopy",
            name="image",
        ),
    ]
