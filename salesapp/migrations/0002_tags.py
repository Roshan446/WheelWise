# Generated by Django 5.0.1 on 2024-03-25 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
