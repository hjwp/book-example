# Generated by Django 4.1.5 on 2023-03-10 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lists", "0002_item_text"),
    ]

    operations = [
        migrations.CreateModel(
            name="List",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
    ]
