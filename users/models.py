from django.db import models
from django.contrib.auth.models import User  # 200101017


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='0')
    roll = models.CharField(max_length=9,default='0')
    batch = models.CharField(max_length=13,default='0')
    department = models.CharField(max_length=50,default='0')

    def __str__(self):
        return f'{self.user.first_name} profile'
    