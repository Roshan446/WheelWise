# Generated by Django 5.0.1 on 2024-04-18 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0013_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='image',
            field=models.ImageField(blank=True, default='default.jpeg', null=True, upload_to='images'),
        ),
    ]
