# Generated by Django 5.0.2 on 2024-02-29 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_words_pronunciation'),
        ('users', '0002_alter_users_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words',
            name='pronunciation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='words',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.users', to_field='user_name'),
        ),
    ]