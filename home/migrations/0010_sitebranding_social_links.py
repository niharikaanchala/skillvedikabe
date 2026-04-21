from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_alter_hero_meta_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitebranding",
            name="facebook_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="sitebranding",
            name="instagram_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="sitebranding",
            name="linkedin_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="sitebranding",
            name="youtube_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
