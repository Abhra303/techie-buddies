# Generated by Django 3.1.2 on 2020-12-17 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0018_sub_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.comment'),
        ),
        migrations.DeleteModel(
            name='sub_comment',
        ),
    ]
