from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings_app", "0003_sitesetting_whatsapp_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitesetting",
            name="google_ads_tag_id",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Google Ads tag ID, e.g. AW-123456789",
                max_length=50,
            ),
        ),
    ]
