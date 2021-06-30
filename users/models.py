from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    DEP_CHOICE =(
    ("0", "select"),
    ("Computer Science and Engineering","Computer Science and Engineering"),
    ("Biosciences and Bioengineering","Biosciences and Bioengineering"),
    ("Chemical Engineering","Chemical Engineering"),
    ("Civil Engineering","Civil Engineering"),
    ("Chemistry","Chemistry"),
    ("Design","Design"),
    ("Electronics and Electrical Engineering","Electronics and Electrical Engineering"),
    ("Mechanical Engineering","Mechanical Engineering"),
    ("Electronics and Communications Engineering","Electronics and Communications Engineering"),
    ("Mathematics and Computing","Mathematics and Computing"),
    ("Engineering Physics","Engineering Physics"),
    ("Humanities and Social Sciences","Humanities and Social Sciences"),
    )

    SEM_CHOICE = (
    ("0", "select"),
    ("1st", "1st"),
    ("2nd", "2nd"),
    ("3rd", "3rd"),
    ("4th", "4th"),
    ("5th", "5th"),
    ("6th", "6th"),
    ("7th", "7th"),
    ("8th", "8th"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default="Name")
    roll = models.IntegerField(default=0)
    semester = models.CharField(max_length=3,choices = SEM_CHOICE,default="0")
    department = models.CharField(max_length=50,choices = DEP_CHOICE,default="0")

    def __str__(self):
        return f'{self.user.username} profile'
    