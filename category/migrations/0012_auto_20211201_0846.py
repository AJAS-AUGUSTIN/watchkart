# Generated by Django 2.2.12 on 2021-12-01 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0011_remove_categories_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='category_name',
            new_name='title',
        ),
    ]
