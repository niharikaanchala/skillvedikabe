from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0010_coursespagecontent_cta_buttons"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="slug",
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]

