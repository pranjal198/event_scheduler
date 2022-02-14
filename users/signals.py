from django.db.models.signals import post_save,post_delete,pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from users import models as user_model
from tasks.models import my_task 
from django.core.files.storage import default_storage
import shutil


@receiver(post_save,sender = User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        try:
            w = instance.first_name
            x = instance.last_name
            u = x[2:4]
            y = x[0:4]
            z = x[4:6]
            DEP_CHOICE ={
                1:"Computer Science and Engineering",
                2:"Electronics and Communications Engineering",
                3:"Mechanical Engineering",
                4:"Civil Engineering",
                5:"Design",
                6:"Biosciences and Bioengineering",
                7:"Chemical Engineering",
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
            PRG_CHOICE = {
                1: "B.Tech",
                2: "B.Des",
                41: "M.Tech",
                61: "PhD",
            }
            Profile.objects.create(user = instance,name = str(w),roll = str(x),batch = BAT_CHOICE[int(y)],programme = PRG_CHOICE[int(u)],department = DEP_CHOICE[int(z)])
        except:
            Profile.objects.create(user = instance,name = "superuser",roll = "0",batch = "superuser",programme = "superuser",department = "superuser")


@receiver(post_save,sender = User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
    

@receiver(post_delete, sender=my_task)
def delete_associated_files(sender, instance, **kwargs):
    """Remove all files of an image after deletion."""
    path = instance.image.name
    if path:
        arr = path.split('/');
        folder = 'media/'+arr[0]+'/'+arr[1]
        shutil.rmtree(folder)
        
@receiver(pre_save, sender=my_task)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = my_task.objects.get(id=instance.id).image
        try:
            new_img = instance.image
        except:
            new_img = None
        if new_img != old_img:
            default_storage.delete(old_img.name)
    except:
        pass