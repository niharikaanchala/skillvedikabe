from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blogpost_image_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="blog/"),
        ),
    ]
