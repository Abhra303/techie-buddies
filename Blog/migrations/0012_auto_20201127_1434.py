# Generated by Django 3.1.2 on 2020-11-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0011_auto_20201127_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, upload_to='Blog/images'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='front_img',
            field=models.ImageField(blank=True, upload_to='Blog/images'),
        ),
    ]
