from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instructor", "0002_instructorapplication"),
    ]

    operations = [
        migrations.AddField(
            model_name="instructorapplication",
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
