# Generated by Django 2.2.12 on 2021-11-17 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_products_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='products',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='products',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
    ]