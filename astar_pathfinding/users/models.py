from django.db import models

class Users(models.Model):
    class Meta:
        db_table = 'users'

    user_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
