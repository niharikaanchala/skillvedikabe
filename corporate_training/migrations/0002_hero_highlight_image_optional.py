from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corporate_training", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="hero",
            name="highlight",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="hero",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="corporate/hero/"),
        ),
    ]
