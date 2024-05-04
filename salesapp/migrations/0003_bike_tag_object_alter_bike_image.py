# Generated by Django 5.0.1 on 2024-03-25 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0002_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='tag_object',
            field=models.ManyToManyField(to='salesapp.tags'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='image',
            field=models.ImageField(default='default.jpeg', null=True, upload_to='images'),
        ),
    ]