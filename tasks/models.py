from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    CAT_CHOICE = (
    ("0", "select"),
    ("Academic Activities", "Academic Activities"),
    ("Branch related Activities", "Branch related Activities"),
    ("Club Related Activities", "Club Related Activities"),
    ("Organisation Related Activities", "Organisation Related Activities"),
    ("Seasonal Activities", "Seasonal Activities"),
    ("Personal Tasks", "Personal Tasks"),
    ("Other Activities", "Other Activities"),
    )
    DEP_CHOICE =(
    ("0", "self"),
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
    title = models.CharField(max_length=20)
    description = models.TextField()
    event_type = models.CharField(max_length=40,choices = CAT_CHOICE,default="0")
    target_branch = models.CharField(max_length=45,choices = DEP_CHOICE,default="0")
    date = models.DateField(default=timezone.now)
    time_from = models.TimeField()
    time_to = models.TimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})
    