from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("course_details", "0003_alter_tool_course_alter_batch_course_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="About",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("content", models.TextField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="about_sections",
                        to="courses.course",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PlacementSupport",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("content", models.TextField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="placement_support_sections",
                        to="courses.course",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CorporateTraining",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("content", models.TextField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="corporate_training_sections",
                        to="courses.course",
                    ),
                ),
            ],
        ),
    ]

