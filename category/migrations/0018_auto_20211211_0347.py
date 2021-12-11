# Generated by Django 2.2.12 on 2021-12-11 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0017_auto_20211209_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='offer',
        ),
        migrations.AddField(
            model_name='categories',
            name='offer_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
