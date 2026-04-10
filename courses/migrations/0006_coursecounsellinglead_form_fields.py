from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0005_coursecounsellinglead"),
    ]

    operations = [
        migrations.AddField(
            model_name="coursecounsellinglead",
            name="agreed_to_terms",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="coursecounsellinglead",
            name="first_name",
            field=models.CharField(blank=True, default="", max_length=120),
        ),
        migrations.AddField(
            model_name="coursecounsellinglead",
            name="last_name",
            field=models.CharField(blank=True, default="", max_length=120),
        ),
        migrations.AddField(
            model_name="coursecounsellinglead",
            name="skills",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="coursecounsellinglead",
            name="years_of_experience",
            field=models.CharField(blank=True, default="", max_length=60),
        ),
    ]
