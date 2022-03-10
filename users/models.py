from django.db import models
from django.contrib.auth.models import User
# from tasks.models import my_task


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



class Profile(models.Model):
    club_name = models.CharField(max_length=50,choices=CLUB_CHOICE,default='Not A Club Member')
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
