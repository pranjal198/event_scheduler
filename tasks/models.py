from operator import truediv
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
    subtitle = models.CharField(max_length=50,default="",blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media/images',blank=True,null=True)
    
    date = models.DateField(default=timezone.localtime(timezone.now()).date())
    deadline = models.DateField(default=timezone.localtime(timezone.now()).date(),blank=True,null=True)
    time_from = models.TimeField(default=timezone.localtime(timezone.now()).time())
    time_to = models.TimeField(default=timezone.localtime(timezone.now()).time())
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    remainder_date = models.DateField(default=timezone.localtime(timezone.now(
    )).date(), blank=True, null=True, help_text="add date only if remainder type is custom")
    remainder_time = models.TimeField(default=timezone.localtime(timezone.now()).time(),)
    
    host = models.ManyToManyField(Profile,related_name="event_host",blank=True,null=True)
    speaker = models.ManyToManyField(Profile,related_name="event_speaker",blank=True,null=True)
    guests = models.JSONField(default=list,null=True, blank=True)
    location = models.JSONField(default=dict,null=True, blank=True)
    
    announcement = models.JSONField(default=dict,null=True, blank=True)
    resources_upload = models.FileField(upload_to='media/resources',blank=True,null=True)
    drive_links = models.JSONField(default=list,null=True, blank=True)
    payment = models.JSONField(default=dict,null=True, blank=True)

    rsvp_users = models.ManyToManyField(Profile,related_name="rsvp_tasks",blank=True,null=True)
    emails = models.JSONField(default=dict,null=True, blank=True)
    
    page_view = models.JSONField(default=dict,null=True, blank=True)
    feedback = models.JSONField(default=dict,null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})

    def get_all_rsvp_users(self):
        return self.rsvp_users.all()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('tasks-detail', kwargs={"pk": self.pk})

    def get_all_rsvp_users(self):
        return self.rsvp_users.all()


# rename to old_models.py
# make a new models.py
# expain why to do this
# do this for all files