# Generated by Django 5.1.2 on 2024-11-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='picture',
            field=models.ImageField(default='', upload_to='customer/profile/img'),
            preserve_default=False,
        ),
    ]
