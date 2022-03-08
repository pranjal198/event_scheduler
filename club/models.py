import datetime
from operator import truediv
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile

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
def event_image_path(instance, filename):
    ext = filename.split('.')[-1]
    return 'events/event-{}/event_logo.{}'.format(instance.id,ext)


class club(models.Model):
    club_name = models.CharField(max_length=20,choices=CLUB_CHOICE)
    title = models.CharField(max_length=50,default=False,null=False)
    description = models.TextField()
    image = models.ImageField(upload_to=event_image_path,blank=True,null=True)
    
    date = models.DateField(default=timezone.localdate)    
    def __str__(self):
        return str(self.club_name)


