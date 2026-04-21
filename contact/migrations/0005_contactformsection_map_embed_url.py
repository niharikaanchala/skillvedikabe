from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0004_alter_metatags_meta_keywords_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactformsection",
            name="map_embed_url",
            field=models.URLField(blank=True, default=""),
        ),
    ]
