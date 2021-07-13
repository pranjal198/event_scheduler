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
    BAT_CHOICE = (
        ("0", "self"),
        ("All Batches", "All Batches"),
        ("Whole B.Tech", "Whole B.Tech"),
        ("Whole B.Des", "Whole B.Des"),
        ("Whole M.Tech", "Whole M.Tech"),
        ("Whole PhD", "Whole PhD"),
        ("B.Tech 20", "B.Tech 20"),
        ("B.Tech 19", "B.Tech 19"),
        ("B.Tech 18", "B.Tech 18"),
        ("B.Tech 17", "B.Tech 17"),
        ("B.Tech 16", "B.Tech 16"),
        ("B.Des 20", "B.Des 20"),
        ("B.Des 19", "B.Des 19"),
        ("B.Des 18", "B.Des 18"),
        ("B.Des 17", "B.Des 17"),
        ("B.Des 16", "B.Des 16"),
        ("M.Tech 20", "M.Tech 20"),
        ("M.Tech 19", "M.Tech 19"),
        ("M.Tech 18", "M.Tech 18"),
        ("M.Tech 17", "M.Tech 17"),
        ("M.Tech 16", "M.Tech 16"),
        ("PhD 20", "PhD 20"),
        ("PhD 19", "PhD 19"),
        ("PhD 18", "PhD 18"),
        ("PhD 17", "PhD 17"),
        ("PhD 16", "PhD 16"),
    )
    DEP_CHOICE =(
        ("self", "self"),
        ("All Branches", "All Branches"),
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
    target_batch = models.CharField(max_length=13,choices = BAT_CHOICE,default="0")
    target_branch = models.CharField(max_length=45,choices = DEP_CHOICE,default="0")
    date = models.DateField(default=timezone.now)
    time_from = models.TimeField()
    time_to = models.TimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})
    