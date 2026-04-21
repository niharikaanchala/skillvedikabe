from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_metatags_blogpost_meta_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="meta_keywords",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="meta_title",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="metatags",
            name="meta_keywords",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="metatags",
            name="meta_title",
            field=models.TextField(blank=True, default=""),
        ),
    ]
