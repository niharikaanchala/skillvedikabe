from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_remove_sectioncopy_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hero",
            name="meta_title",
            field=models.TextField(blank=True, default=""),
        ),
    ]
