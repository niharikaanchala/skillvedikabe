from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("course_details", "0005_section_headings"),
    ]

    operations = [
        migrations.AddField(
            model_name="skill",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.CreateModel(
            name="CourseSectionMeta",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("about_heading", models.CharField(blank=True, default="", max_length=200)),
                ("skills_heading", models.CharField(blank=True, default="", max_length=200)),
                ("tools_heading", models.CharField(blank=True, default="", max_length=200)),
                ("curriculum_heading", models.CharField(blank=True, default="", max_length=200)),
                ("projects_heading", models.CharField(blank=True, default="", max_length=200)),
                ("salary_heading", models.CharField(blank=True, default="", max_length=200)),
                ("placement_support_heading", models.CharField(blank=True, default="", max_length=200)),
                ("corporate_training_heading", models.CharField(blank=True, default="", max_length=200)),
                ("trainers_heading", models.CharField(blank=True, default="", max_length=200)),
                ("batches_heading", models.CharField(blank=True, default="", max_length=200)),
                ("blogs_heading", models.CharField(blank=True, default="", max_length=200)),
                ("faqs_heading", models.CharField(blank=True, default="", max_length=200)),
                (
                    "course",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="section_meta",
                        to="courses.course",
                    ),
                ),
            ],
        ),
    ]

