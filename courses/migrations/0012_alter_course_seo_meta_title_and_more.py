from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0011_alter_course_slug_length"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="seo_meta_title",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="coursespagecontent",
            name="meta_title",
            field=models.TextField(blank=True, default=""),
        ),
    ]
