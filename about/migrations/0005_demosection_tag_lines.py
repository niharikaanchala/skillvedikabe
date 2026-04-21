from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0004_abouthero_hero_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="demosection",
            name="tag_lines",
            field=models.JSONField(blank=True, default=list),
        ),
    ]
