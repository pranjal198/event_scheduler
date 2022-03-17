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
    ("ACADEMIC INITIATIVE CLUB","ACADEMIC INITIATIVE CLUB"),
    ("ACUMEN CLUB","ACUMEN CLUB"),
    ("AEROMODELLING CLUB","AEROMODELLING CLUB"),
    ("AI CLUB","AI CLUB"),
    ("ALCHER","ALCHER"),
    ("ANCHORENZA CLUB","ANCHORENZA CLUB"),
    ("ASTRO CLUB","ASTRO CLUB"),
    ("ATHLETICS CLUB","ATHLETICS CLUB"),
    ("AQUATICS CLUB","AQUATICS CLUB"),
    ("AUTOMOBILE CLUB","AUTOMOBILE CLUB"),   
    ("BADMINTON CLUB","BADMINTON CLUB"), 
    ("BASKETBALL CLUB","BASKETBALL CLUB"),
    ("CODING CLUB", "CODING CLUB"),
    ("CA CLUB", "CA CLUB"),
    ("CCD CLUB", "CCD CLUB"),
    ("CRICKET CLUB","CRICKET CLUB"),
    ("DANCE CLUB","DANCE CLUB"),
    ("DRAMA CLUB","DRAMA CLUB"),
    ("EE CLUB", "EE CLUB"),
    ("ED CLUB", "ED CLUB"),
    ("FNC CLUB", "FNC CLUB"),
    ("FINE ARTS CLUB","FINE ARTS CLUB"),
    ("FOOTBALL CLUB","FOOTBALL CLUB"),
    ("HOCKEY CLUB","HOCKEY CLUB"),
    ("LITERARY CLUB","LITERARY CLUB"),
    ("MOVIE CLUB","MOVIE CLUB"),
    ("MUSIC CLUB","MUSIC CLUB"),
    ("PHOTOGRAPHY CLUB","PHOTOGRAPHY CLUB"),
    ("PRAKRITI CLUB", "PRAKRITI CLUB"),
    ("RADIOG CLUB","RADIOG CLUB"),
    ("RED RIBBON CLUB","RED RIBBON CLUB"),
    ("RIGHTS AND RESPONSIBILITIES CLUB","RIGHTS AND RESPONSIBILITIES CLUB"),
    ("ROBOTICS CLUB", "ROBOTICS CLUB"),
    ("SAATHI COUNSELLING CLUB","SAATHI COUNSELLING CLUB"),
    ("SAIL", "SAIL"),
    ("SOCIAL SERVICE CLUB","SOCIAL SERVICE CLUB"),
    ("SQUASH CLUB","SQUASH CLUB"),
    ("TABLE TENNIS CLUB","TABLE TENNIS CLUB"),
    ("TECHNICHE", "TECHNICHE"),
    ("TENNIS CLUB","TENNIS CLUB"),
    ("UG CLUB", "UG CLUB"),
    ("VOLLEYBALL CLUB","VOLLEY BALL CLUB"),
    ("WEIGHTLIFTING CLUB","WEIGHTLIFTING CLUB"),
    ("YOUTH EMPOWERMENT CLUB","YOUTH EMPOWERMENT CLUB")
)


def event_image_path(instance, filename):
    ext = filename.split('.')[-1]
    return 'clubs/{}.{}'.format(instance.id,ext)


class Club(models.Model):
    club_name = models.CharField(max_length=50,choices=CLUB_CHOICE)
    title = models.CharField(max_length=50,default="None",null=False)
    description = models.TextField()
    image = models.ImageField(upload_to=event_image_path,blank=True,null=True)
    
    date = models.DateField(default=timezone.localdate)    
    def __str__(self):
        return str(self.club_name)


