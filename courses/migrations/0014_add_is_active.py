from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0013_alter_course_duration_price_optional"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="When False, the course is hidden from the public site.",
            ),
        ),
    ]
