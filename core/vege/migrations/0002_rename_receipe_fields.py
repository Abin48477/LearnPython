from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vege", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="receipe",
            old_name="receipe_name",
            new_name="recipe_name",
        ),
        migrations.RenameField(
            model_name="receipe",
            old_name="receipe_description",
            new_name="recipe_description",
        ),
        migrations.RenameField(
            model_name="receipe",
            old_name="receipe_image",
            new_name="recipe_image",
        ),
        migrations.AlterField(
            model_name="receipe",
            name="recipe_image",
            field=models.ImageField(blank=True, upload_to="recipe"),
        ),
    ]
