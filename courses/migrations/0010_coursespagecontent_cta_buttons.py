from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0009_course_seo_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="coursespagecontent",
            name="hero_cta_buttons",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text='List of CTA buttons for hero: [{"text": "...", "link": "..."}]',
            ),
        ),
        migrations.AddField(
            model_name="coursespagecontent",
            name="cta_buttons",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text='List of CTA buttons: [{"text": "...", "link": "...", "variant": "primary|secondary"}]',
            ),
        ),
    ]

