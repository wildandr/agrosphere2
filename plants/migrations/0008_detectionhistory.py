# Generated by Django 4.2.6 on 2023-10-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("plants", "0007_notification"),
    ]

    operations = [
        migrations.CreateModel(
            name="DetectionHistory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("source", models.CharField(max_length=255)),
                ("plant_img", models.CharField(max_length=255)),
                ("plant_name", models.CharField(max_length=255)),
                ("condition", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]