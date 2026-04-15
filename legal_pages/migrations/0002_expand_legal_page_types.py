from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("legal_pages", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="legalpage",
            name="page_type",
            field=models.CharField(
                choices=[
                    ("terms", "Terms & Conditions"),
                    ("privacy", "Privacy Policy"),
                    ("disclaimer", "Disclaimer"),
                    ("editorial-policy", "Editorial Policy"),
                ],
                max_length=20,
                unique=True,
            ),
        ),
    ]
