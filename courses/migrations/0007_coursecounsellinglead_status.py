from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0006_coursecounsellinglead_form_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="coursecounsellinglead",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("approved", "Approved"),
                    ("rejected", "Rejected"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
    ]
