from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instructor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="InstructorApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=120)),
                ("last_name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=30)),
                ("years_of_experience", models.CharField(max_length=60)),
                ("skills", models.TextField(help_text="Comma-separated skills")),
                ("message", models.TextField(blank=True)),
                ("agreed_to_terms", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
