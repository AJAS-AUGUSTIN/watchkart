# Generated by Django 2.2.12 on 2021-11-19 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_auto_20211118_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_discount_price',
            field=models.IntegerField(),
        ),
    ]