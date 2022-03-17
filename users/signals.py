from django.db.models.signals import post_save,post_delete,pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver,Signal
from club.models import Club
from users.decorators import club
from users.tasks_helper import *
from .models import Profile
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from tasks.models import my_task 
from django.core.files.storage import default_storage
import shutil
import tasks.tasks

schedule_add = Signal(providing_args=['instance','field','id','data'])
schedule_update = Signal(providing_args=['instance','field','id','data'])
schedule_delete = Signal(providing_args=['instance','field','id'])

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

@receiver(pre_save, sender=Club)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = Club.objects.get(id=instance.id).image
        try:
            new_img = instance.image
        except:
            new_img = None
        if new_img != old_img:
            default_storage.delete(old_img.name)
    except:
        pass

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
    old_event = my_task.objects.filter(id=instance.id).first()
    try:

        if old_event.remainder == instance.remainder:
            task = PeriodicTask.objects.filter(name=f'event-{old_event.id}-remainder-{old_event.remainder}').first()
            if instance.remainder == 'Custom':
                custom_remainder_apply(instance,task)
            if instance.remainder == 'Daily':
                daily_remainder_apply(instance,task)
            if instance.remainder == 'Weekly':
                weekly_remainder_apply(instance,task)
            if instance.remainder == 'Monthly':
                monthly_remainder_apply(instance,task)
            if instance.remainder == 'Week before':
                weekbefore_remainder_apply(instance,task)
        else:
            task = PeriodicTask.objects.filter(name=f'event-{old_event.id}-remainder-{old_event.remainder}').first()
            if task:
                task.delete()
            if instance.remainder == 'Custom':
                print("custom......")
                custom_remainder_apply(instance)
                
            if instance.remainder == 'Daily':
                print("daily......")
                daily_remainder_apply(instance)
                
            if instance.remainder == 'Weekly':
                print("weekly......")
                weekly_remainder_apply(instance)
                
            if instance.remainder == 'Monthly':
                print("monthly......")
                monthly_remainder_apply(instance)
                
            if instance.remainder == 'Week before':
                print("week before......")
                weekbefore_remainder_apply(instance)
    except:
        pass
    
@receiver(schedule_add)
def add_schedule(sender, **kwargs):
    event = kwargs['instance']
    id = kwargs['id']
    data = kwargs['data']
    if data['time'][3]!='0':
        minute=  data['time'][3]+data['time'][4] 
    else:
        minute = data['time'][4]
    if data['time'][0]!='0':
        hour=  data['time'][0]+data['time'][1] 
    else:
        hour = data['time'][1]
        
    if data['date'][8]!='0':
        date=  data['date'][8]+data['date'][9] 
    else:
        date = data['date'][9]
    if data['date'][5]!='0':
        month=  data['date'][5]+data['date'][6] 
    else:
        month = data['date'][6]
    cron,created = CrontabSchedule.objects.get_or_create(
        minute=minute,
        hour=hour,
        day_of_month=date,
        month_of_year=month,
    )
    if kwargs['field'] == 'announcement':
        PeriodicTask.objects.create(
            name=f'event-{event.id}-announcement-{id}',
            task='add_announcement',
            crontab=cron,
            args=f'''[{event.id},{id}]''',
            one_off=True,
        )
    if kwargs['field'] == 'emails':
        PeriodicTask.objects.create(
            name=f'event-{event.id}-emails-{id}',
            task='add_emails',
            crontab=cron,
            args=f'''[{event.id},{id}]''',
            one_off=True,
        )
    
@receiver(schedule_update)
def update_schedule(sender, **kwargs):
    event = kwargs['instance']
    id = kwargs['id']
    data = kwargs['data']
    if data['time'][3]!='0':
        minute=  data['time'][3]+data['time'][4] 
    else:
        minute = data['time'][4]
    if data['time'][0]!='0':
        hour=  data['time'][0]+data['time'][1] 
    else:
        hour = data['time'][1]
        
    if data['date'][8]!='0':
        date=  data['date'][8]+data['date'][9] 
    else:
        date = data['date'][9]
    if data['date'][5]!='0':
        month=  data['date'][5]+data['date'][6] 
    else:
        month = data['date'][6]
    cron,created = CrontabSchedule.objects.get_or_create(
        minute=minute,
        hour=hour,
        day_of_month=date,
        month_of_year=month,
    )
    if kwargs['field'] == 'announcement':
        task = PeriodicTask.objects.get(name=f'event-{event.id}-announcement-{id}')
        task.crontab = cron
        task.save()
    if kwargs['field'] == 'emails':
        task = PeriodicTask.objects.get(name=f'event-{event.id}-emails-{id}')
        task.crontab = cron
        task.save()
    
@receiver(schedule_delete)
def delete_schedule(sender, **kwargs):
    event = kwargs['instance']
    id = kwargs['id']
    if kwargs['field'] == 'announcement':
        task = PeriodicTask.objects.get(name=f'event-{event.id}-announcement-{id}')
        task.delete()
    if kwargs['field'] == 'emails':
        task = PeriodicTask.objects.get(name=f'event-{event.id}-emails-{id}')
        task.delete()