# Generated by Django 3.1.2 on 2020-11-20 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_auto_20201119_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tag',
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(related_name='blogs', to='Blog.Tag'),
        ),
    ]