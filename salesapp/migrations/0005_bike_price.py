# Generated by Django 5.0.1 on 2024-03-30 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0004_remove_bike_tag_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='price',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
