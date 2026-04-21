from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0006_alter_contactformsection_map_embed_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactformsection",
            name="map_embed_url",
            field=models.TextField(blank=True, default=""),
        ),
    ]
