# Generated manually for optional category description

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0005_add_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
    ]
