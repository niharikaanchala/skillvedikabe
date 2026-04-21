from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0003_alter_metatags_meta_keywords_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="abouthero",
            name="hero_image",
            field=models.ImageField(blank=True, null=True, upload_to="about/hero/"),
        ),
    ]
