from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0007_alter_contactformsection_map_embed_url_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactinfo",
            name="map_embed_url",
            field=models.TextField(blank=True, default=""),
        ),
    ]
