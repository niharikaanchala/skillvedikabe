from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course_details", "0004_about_placement_corporate_sections"),
    ]

    operations = [
        migrations.AddField(
            model_name="about",
            name="heading",
            field=models.CharField(blank=True, default="", max_length=200),
        ),
        migrations.AddField(
            model_name="placementsupport",
            name="heading",
            field=models.CharField(blank=True, default="", max_length=200),
        ),
        migrations.AddField(
            model_name="corporatetraining",
            name="heading",
            field=models.CharField(blank=True, default="", max_length=200),
        ),
    ]

