# Generated by Django 2.2.12 on 2021-12-04 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20211203_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitems',
            old_name='products_id',
            new_name='products',
        ),
    ]
