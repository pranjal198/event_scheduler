from django.db import models
from django.contrib.auth.models import User
# from tasks.models import my_task


CLUB_CHOICE = (
    ("Select", "Select"),
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



class Profile(models.Model):
    club_name = models.CharField(max_length=20,choices=CLUB_CHOICE,default='Not A Club Member')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='0')
    roll = models.CharField(max_length=9,default='0')
    batch = models.CharField(max_length=13,default='0')
    programme = models.CharField(max_length=13,default='0')
    department = models.CharField(max_length=50,default='0')
    club_status = models.BooleanField(default=0)
    def __str__(self):
        return f'{self.user.first_name} profile'

    def get_rsvp_tasks(self):
        # return the tasks which are related to this user (using the m2m relation my_task.rsvp_users)
        return self.rsvp_tasks.all()
