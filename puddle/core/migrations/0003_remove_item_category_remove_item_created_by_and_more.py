# Generated by Django 5.1 on 2024-08-27 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_category_options_item"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="category",
        ),
        migrations.RemoveField(
            model_name="item",
            name="created_by",
        ),
        migrations.DeleteModel(
            name="Category",
        ),
        migrations.DeleteModel(
            name="Item",
        ),
    ]
