# Generated by Django 5.1.2 on 2024-10-18 04:21

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='images/brand/logo')),
                ('name', models.CharField(max_length=20)),
                ('tagline', models.CharField(max_length=50)),
                ('since', models.DateField()),
                ('types', models.CharField(choices=[('CPB', 'Corporate branding'), ('PSB', 'Personal branding'), ('PB', ' Product branding'), ('RB', 'Retail branding'), ('GPB', 'Geographic branding'), ('SB', 'Service branding')], max_length=20)),
                ('origin', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='HsnCode',
            fields=[
                ('index', models.BigAutoField(primary_key=True, serialize=False)),
                ('item_code', models.BigIntegerField(null=True, verbose_name='Item Code')),
                ('item_name', models.TextField(null=True, verbose_name='Item Name')),
                ('item_type', models.TextField(null=True, verbose_name='Item Type')),
                ('GSTe', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='GST %e')),
                ('hsn_code', models.BigIntegerField(null=True, verbose_name='HSN Code')),
                ('GST', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='GST %')),
            ],
            options={
                'db_table': 'HSN_CODE',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('price_inclusive', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(default='default Description')),
                ('gst_rate', models.DecimalField(decimal_places=2, default=5.0, max_digits=5)),
                ('hsn_code', models.CharField(default=None, max_length=10)),
                ('quantity', models.IntegerField(default=1)),
                ('features', models.JSONField(blank=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=70)),
                ('product', models.ManyToManyField(to='product.product')),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/product/images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'Product_Images',
            },
        ),
    ]