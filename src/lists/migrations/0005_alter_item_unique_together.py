# Generated by Django 5.1.1 on 2024-09-11 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0004_item_list"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="item",
            unique_together={("list", "text")},
        ),
    ]
