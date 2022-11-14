# Generated by Django 3.2.13 on 2022-11-14 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=250)),
                ('model_name', models.CharField(blank=True, max_length=250)),
                ('color', models.CharField(blank=True, max_length=250)),
                ('fixed_price', models.IntegerField()),
                ('special_price', models.IntegerField()),
                ('os', models.CharField(blank=True, max_length=250)),
                ('processor', models.CharField(blank=True, max_length=250)),
                ('security_function', models.CharField(blank=True, max_length=250)),
                ('input_device', models.CharField(blank=True, max_length=250)),
                ('network', models.CharField(blank=True, max_length=250)),
                ('multimedia', models.CharField(blank=True, max_length=250)),
                ('power_consumption', models.IntegerField()),
                ('rated_voltage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('content', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Graphics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integrated_graphics', models.CharField(blank=True, max_length=250)),
                ('external_graphics', models.CharField(blank=True, max_length=250)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
    ]