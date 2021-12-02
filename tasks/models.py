from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile


REM_CHOICE = (
    ("0", "Select"),
    ("Daily", "Daily"),
    ("Weekly", "Weekly"),
    ("Monthly", "Monthly"),
    ("Week before", "Week before"),
    ("Custom", "Custom"),
)
CLUB_CHOICE = (
    ("0", "Select"),
    ("SWC", "SWC"),
    ("CODING CLUB", "CODING CLUB"),
    ("AERO CLUB", "AERO CLUB"),
    ("ASTRO CLUB", "ASTRO CLUB"),
    ("CA CLUB", "CA CLUB"),
    ("EE CLUB", "EE CLUB"),
    ("PRAKRITI CLUB", "PRAKRITI CLUB"),
    ("FNC CLUB", "FNC CLUB"),
    ("ROBOTICS CLUB", "ROBOTICS CLUB"),
    ("ED CLUB", "ED CLUB"),
    ("UG CLUB", "UG CLUB"),
    ("ALCHER CLUB", "ALCHER CLUB"),
    ("TECHNICHE CLUB", "TECHNICHE CLUB"),
    ("SAIL CLUB", "SAIL CLUB"),
    ("AI CLUB", "AI CLUB"),
    ("CCD CLUB", "CCD CLUB"),
    ("OTHER CLUB", "OTHER CLUB"),
)


class my_task(models.Model):
    club_name = models.CharField(max_length=20,choices=CLUB_CHOICE)
    title = models.CharField(max_length=20)
    description = models.TextField()
    # target_batch = models.CharField(max_length=13, choices=BAT_CHOICE, default="Self")
    # target_branch = models.CharField(max_length=45, choices=DEP_CHOICE, default="Self")
    date = models.DateField(default=timezone.localtime(timezone.now()))
    deadline = models.DateField(default=timezone.localtime(timezone.now()),blank=True,null=True)
    time_from = models.TimeField(default=timezone.localtime(timezone.now()))
    time_to = models.TimeField(default=timezone.localtime(timezone.now()))

    remainder_date = models.DateField(default=timezone.localtime(timezone.now()))
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()))
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # notifications=models.CharField(max_length=500,default="")
    announcements=models.TextField(default="",null=True,blank=True,help_text="announcements should be seperated by comma, so that we can list them as points")
    resources_upload = models.FileField(upload_to='media/',blank=True,null=True)

    rsvp_users = models.ManyToManyField(Profile,related_name="rsvp_tasks")
    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})

    def get_all_rsvp_users(self):
        return self.rsvp_users.all()


# rename to old_models.py
# make a new models.py
# expain why to do this
# do this for all files