# Generated by Django 2.2 on 2022-04-18 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0008_auto_20220413_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='img',
            field=models.ImageField(upload_to='product'),
        ),
    ]
