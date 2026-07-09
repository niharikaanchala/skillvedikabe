from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0012_alter_course_seo_meta_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="duration",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="course",
            name="price",
            field=models.CharField(blank=True, default="", max_length=20),
        ),
    ]
