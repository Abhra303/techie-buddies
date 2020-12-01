# Generated by Django 3.1.2 on 2020-11-27 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_auto_20201120_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='front_img',
            field=models.ImageField(default='Techblog/featuredimage.jpg', upload_to='Blog/images'),
        ),
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(default='Techblog/guest-user.jpg', upload_to='Blog/images'),
        ),
    ]
