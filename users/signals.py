from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save,sender = User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        w=instance.first_name
        x=instance.last_name
        y = x[0:4]
        z = x[4:6]
        DEP_CHOICE ={
            1:"Computer Science and Engineering",
            2:"Electronics and Communications Engineering",
            3:"Mechanical Engineering",
            4:"Chemical Engineering",
            5:"Design",
            6:"Biosciences and Bioengineering",
            7:"Civil Engineering",
            8:"Electronics and Electrical Engineering",
            21:"Engineering Physics",
            22:"Chemimal Science and Technology",
            23:"Mathematics and Computing",
            25:"Humanities and Social Sciences",
        }
        BAT_CHOICE = {
                2001: "B.Tech 20",
                1901: "B.Tech 19",
                1801: "B.Tech 18",
                1701: "B.Tech 17",
                1601: "B.Tech 16",
                2002: "B.Des 20",
                1902: "B.Des 19",
                1802: "B.Des 18",
                1702: "B.Des 17",
                1602: "B.Des 16",
                2041: "M.Tech 20",
                1941: "M.Tech 19",
                1841: "M.Tech 18",
                1741: "M.Tech 17",
                1641: "M.Tech 16",
                2061: "PhD 20",
                1961: "PhD 19",
                1861: "PhD 18",
                1761: "PhD 17",
                1661: "PhD 16",
        }
        Profile.objects.create(user = instance,name = str(w),roll = str(x),batch = BAT_CHOICE[int(y)],department = DEP_CHOICE[int(z)])


@receiver(post_save,sender = User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
