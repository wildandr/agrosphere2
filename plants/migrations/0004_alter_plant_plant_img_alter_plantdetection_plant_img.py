# Generated by Django 4.2.6 on 2023-10-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("plants", "0003_disease_alter_plant_plant_img_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plant",
            name="plant_img",
            field=models.ImageField(upload_to="image/"),
        ),
        migrations.AlterField(
            model_name="plantdetection",
            name="plant_img",
            field=models.ImageField(upload_to="image/"),
        ),
    ]