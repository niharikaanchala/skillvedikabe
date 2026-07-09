from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings_app", "0002_sitesetting_created_at_sitesetting_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitesetting",
            name="whatsapp_number",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Country code + number without + or spaces, e.g. 919381193375",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="sitesetting",
            name="whatsapp_message",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Pre-filled WhatsApp message (plain text; will be URL-encoded on the site)",
            ),
        ),
    ]
