# Generated by Django 2.2.12 on 2021-11-23 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0009_auto_20211123_1350'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0010_orderproduct_tax'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=50)),
                ('user_address', models.CharField(max_length=2500, null=True)),
                ('payment_mode', models.CharField(max_length=100, null=True)),
                ('order_number', models.CharField(max_length=20)),
                ('order_total', models.FloatField()),
                ('tax', models.FloatField()),
                ('status', models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='New', max_length=10)),
                ('is_orderd', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('anonymous_user', models.CharField(blank=True, max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('grand_total', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('products_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Products')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='user',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.DeleteModel(
            name='OrderProduct',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
