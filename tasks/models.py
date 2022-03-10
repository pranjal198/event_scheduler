import datetime
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
    return 'events/event-{}/event_logo.{}'.format(instance.id,ext)


class my_task(models.Model):
    club_name = models.CharField(max_length=50,choices=CLUB_CHOICE)
    
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=50,default="",blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to=event_image_path,blank=True,null=True)
    
    date = models.DateField(default=timezone.localdate)
    deadline = models.DateField(default=timezone.localdate,blank=True,null=True)
    time_from = models.TimeField(default=datetime.time)
    time_to = models.TimeField(default=datetime.time)
    remainder = models.CharField(max_length=12, choices=REM_CHOICE, default="None")
    remainder_date = models.DateField(default=timezone.localdate, blank=True, null=True, help_text="add date only if remainder type is custom")
    remainder_time = models.TimeField(default=datetime.time)
    
    host = models.ManyToManyField(Profile,related_name="event_host",blank=True)
    speaker = models.ManyToManyField(Profile,related_name="event_speaker",blank=True)
    guests = models.JSONField(default=list,null=True, blank=True)
    location = models.JSONField(default=dict,null=True, blank=True)
    
    announcement = models.JSONField(default=dict,null=True, blank=True)
    resources_upload = models.JSONField(default=list,null=True, blank=True)
    drive_links = models.JSONField(default=list,null=True, blank=True)
    payment = models.JSONField(default=dict,null=True, blank=True)

    rsvp_users = models.ManyToManyField(Profile,related_name="rsvp_tasks",blank=True)
    emails = models.JSONField(default=dict,null=True, blank=True)
    
    page_view = models.JSONField(default=dict,null=True, blank=True)
    feedback = models.JSONField(default=dict,null=True, blank=True)
    all_ids = models.JSONField(default=dict,null=True, blank=True)

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

class Notification(models.Model):
    task = models.ForeignKey(my_task, on_delete=models.CASCADE)
    message = models.TextField()
    sent = models.BooleanField(default=False)

    

demo = {
    "club_name":"SWC",
    
    "title":"demo event",
    "subtitle":"demo",
    "image":"https://swc.iitg.ac.in/event-scheduler/media/images/img1.jpg",

    "date":"2022-02-12",
    "deadline":"2022-02-14",
    "time_from": "00:12:00",
    "time_to": "12:12:00",
    "remainder": "Custom",
    "remainder_date": "2022-02-11",
    "remainder_time": "04:44:00",
    
    "host":[1,2,3], # host profile id
    "speaker":[1,2,3], # speaker profile id
    "guests":[
            {
                "id":1,
                "name":"guest 1",
                "email":"abc@gmail.com",
                "designation":"SDE at Microsoft",
                "batch":2014,
            },
            {
                "id":2,
                "name":"guest 2",
                "email":"efg@gmail.com",
                "designation":"Product Manager at Apple",
                "batch":2015,
            }
        ], # guests
    "location":{
        "offline":{
            "latitude":"27.2046° N",
            "longitude":"77.4977° E"
        },
        "online":{
            "meet_url":"meet/google.com/abd-efg-hij",
            "room_id":"abc123",
            "password":"abc@123"
        }
        # for online event offline value will be null and vice versa
    },
    "announcement":{
        "fixed":[
            {
                "announcement":"all participants must fill the google form"
            },
            {
                "announcement":"share the links to your friends"
            }
        ],
        "dynamic":[
            {
                "date":"2022-02-12",
                "time":"21:30:00",
                "announcement":"we will be starting at 10:00 pm"
            },
            {
                "date":"2022-02-12",
                "time":"23:00:00",
                "announcement":"please fill the feedback form"
            },
        ],
    },
    "resources_upload":"https://swc.iitg.ac.in/event-scheduler/media/reources/info.pdf",
    "drive_links":[
        {
            "filename":"guidelines.pdf",
            "link":"drive.google.com/askddhswe/suiojsdoijsddsd"
        },
        {
            "filename":"results.pdf",
            "link":"drive.google.com/askddhswe/suiojsdoijsddsd"
        },
    ],
    "payment":{
        "paid":True,
        "metadata":{
            "price":499,
            "link":"https://abcd.payment/com/?pay=499"
        }
    },
    
    "rsvp_users":[1,2,3,4,8,9], # users profile id
    "emails":{
        "registration":{
            "to":["a@gmail.com","b@yahoo.com"],
            "sub":"register now for abc event",
            "body":"abcd",
        },
        "scheduled":[
            {
                "to":["a@gmail.com","b@yahoo.com"],
                "sub":"hurry up register now for abc event",
                "body":"abcd",
                "date":"2022-02-15",
                "time":"09:00:00",
            },
            {
                "to":["a@gmail.com","b@yahoo.com"],
                "sub":"join fast",
                "body":"abcd",
                "date":"2022-02-15",
                "time":"10:00:00",
            },
        ]
    },
    
    "page_view":{
        "2022-02-12": [1],
        "2022-02-13": [2],
        "2022-02-14": [3],
        "2022-02-15": [4],
        "2022-02-16": [5],
        "2022-02-17": [7],
    },
    "feedback":{
        "1":[1,2],
        "2":[3],
        "3":[4],
        "4":[5,6],
        "5":[7,8,9,10],
    }
}