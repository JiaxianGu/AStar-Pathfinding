from django.db import models
from users.models import Users
class Words(models.Model):
    class Meta:
        db_table = 'words'

    word = models.CharField(max_length=100)
    meaning = models.CharField(max_length=10000)
    user = models.ForeignKey(Users, to_field='user_name', on_delete=models.CASCADE, blank=True, null=True)
    pronunciation = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.word