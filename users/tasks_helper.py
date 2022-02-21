import datetime
from tasks.models import my_task
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from tasks.models import my_task 

def helper_get_not_rsvp_tasks(obj):
    all_tasks = my_task.objects.all()
    subscribed_tasks = obj.get_rsvp_tasks()
    remained_tasks = all_tasks.difference(subscribed_tasks)
    return remained_tasks
    
def helper_get_subscribed_club_tasks(obj, club_name):
    all_tasks = my_task.objects.filter(club_name=club_name)
    subscribed_tasks = obj.get_rsvp_tasks()
    remained_tasks = all_tasks.intersection(subscribed_tasks)
    return remained_tasks

def helper_get_new_club_tasks(obj, club_name):
    all_tasks = my_task.objects.filter(club_name=club_name)
    subscribed_tasks = obj.get_rsvp_tasks()
    remained_tasks = all_tasks.difference(subscribed_tasks)
    return remained_tasks

def custom_remainder_apply(instance,task=None):
    date = str(instance.remainder_date.day)
    month = str(instance.remainder_date.month)
    hour = str(instance.remainder_time.hour)
    minute = str(instance.remainder_time.minute)
    cron = CrontabSchedule.objects.filter( minute=minute,hour=hour,day_of_month=date,month_of_year=month).first()
    if not cron:
        cron = CrontabSchedule.objects.create(
            minute=minute,
            hour=hour,
            day_of_month=date,
            month_of_year=month,
        )
    if task:
        print("updating custom......")
        task.crontab=cron
        task.save()
    else:
        print("creating custom......")
        PeriodicTask.objects.create(
            name=f'event-{instance.id}-remainder-Custom',
            task='send_remainder',
            crontab=cron,
            args=f'''[{instance.id}]''',
            one_off=True,
        )

def daily_remainder_apply(instance,task=None):
    hour = str(instance.time_from.hour)
    minute = str(instance.time_from.minute)
    end_date = instance.date
    start_date = instance.date - datetime.timedelta(7)
    cron = CrontabSchedule.objects.filter(minute=minute,hour=hour).first()
    if not cron:
        cron = CrontabSchedule.objects.create(
            minute=minute,
            hour=hour,
        )
    if task:
        print("updating daily......")
        task.crontab=cron
        task.start_time = datetime.datetime.combine(start_date,datetime.time())
        task.expires = datetime.datetime.combine(end_date,instance.time_from)
        task.save()
    else:
        print("creating daily......")
        PeriodicTask.objects.create(
            name=f'event-{instance.id}-remainder-Daily',
            task='send_remainder',
            crontab=cron,
            args=f'''[{instance.id}]''',
            start_time = datetime.datetime.combine(start_date,datetime.time()),
            expires = datetime.datetime.combine(end_date,instance.time_from),
        )

def weekly_remainder_apply(instance,task=None):
    hour = str(instance.time_from.hour)
    minute = str(instance.time_from.minute)
    end_date = instance.date
    start_date = instance.date - datetime.timedelta(31)
    day = instance.date.weekday()
    if day==6:
        day = 0
    else:
        day = day+1
    cron = CrontabSchedule.objects.filter(minute=minute,hour=hour,day_of_week=str(day)).first()
    if not cron:
        cron = CrontabSchedule.objects.create(
            minute=minute,
            hour=hour,
            day_of_week=str(day),
        )
    if task:
        print("updating weekly......")
        task.crontab=cron
        task.start_time = datetime.datetime.combine(start_date,datetime.time())
        task.expires = datetime.datetime.combine(end_date,instance.time_from)
        task.save()
    else:
        print("creating weekly......")
        PeriodicTask.objects.create(
            name=f'event-{instance.id}-remainder-Weekly',
            task='send_remainder',
            crontab=cron,
            args=f'''[{instance.id}]''',
            start_time = datetime.datetime.combine(start_date,datetime.time()),
            expires = datetime.datetime.combine(end_date,instance.time_from),
        )

def monthly_remainder_apply(instance,task=None):
    hour = str(instance.time_from.hour)
    minute = str(instance.time_from.minute)
    date = str(instance.date.day)
    end_date = instance.date
    start_date = instance.date - datetime.timedelta(93)
    cron = CrontabSchedule.objects.filter(minute=minute,hour=hour,day_of_month=date).first()
    if not cron:
        cron = CrontabSchedule.objects.create(
            minute=minute,
            hour=hour,
            day_of_month=date,
        )
    if task:
        print("updating monthly......")
        task.crontab=cron
        task.start_time = datetime.datetime.combine(start_date,datetime.time())
        task.expires = datetime.datetime.combine(end_date,instance.time_from)
        task.save()
    else:
        print("creating monthly......")
        PeriodicTask.objects.create(
            name=f'event-{instance.id}-remainder-Monthly',
            task='send_remainder',
            crontab=cron,
            args=f'''[{instance.id}]''',
            start_time = datetime.datetime.combine(start_date,datetime.time()),
            expires = datetime.datetime.combine(end_date,instance.time_from),
        )

def weekbefore_remainder_apply(instance,task=None):
    start_date = instance.date - datetime.timedelta(7)
    date = str(start_date.day)
    month = str(start_date.month)
    hour = str(instance.time_from.hour)
    minute = str(instance.time_from.minute)
    cron = CrontabSchedule.objects.filter(minute=minute,hour=hour,day_of_month=date,month_of_year=month).first()
    if not cron:
        cron = CrontabSchedule.objects.create(
            minute=minute,
            hour=hour,
            day_of_month=date,
            month_of_year=month,
        )
    if task:
        print("updating week before......")
        task.crontab=cron
        task.save()
    else:
        print("creating week before......")
        PeriodicTask.objects.create(
            name=f'event-{instance.id}-remainder-Week before',
            task='send_remainder',
            crontab=cron,
            args=f'''[{instance.id}]''',
            one_off=True,
        )
