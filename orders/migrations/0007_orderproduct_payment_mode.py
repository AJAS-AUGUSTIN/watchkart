# Generated by Django 2.2.12 on 2021-11-23 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20211123_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='payment_mode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
