# Generated by Django 5.0.2 on 2024-02-29 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
