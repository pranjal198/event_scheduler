
from django.contrib.auth.models import User
from django.conf import settings
from celery.utils.log import get_task_logger
from celery import Celery
from event_scheduler.celery import app
from datetime import date, datetime, timedelta
from django.core.mail import send_mail
from tasks.models import my_task
from users.models import Profile
# All the celery tasks


@app.task(bind=True)
def debug_task_custom(self):
    print('task started')

    email_from = settings.EMAIL_HOST_USER
    print(email_from)
    try:
        events = my_task.objects.filter(remainder_date=datetime.now().date())
        for event in events:
            rsvp_users = event.rsvp_users.all()
            subject = 'Remainder for the event- '+event.title
            message = 'Event description: '+event.description+'\nDate of event: '+event.date.strftime(
                "%m/%d/%Y")+'\nFrom: '+event.time_from.strftime("%H:%M")+'\nTo: '+event.time_to.strftime("%H:%M")
            for rsvp_user in rsvp_users:
                print(rsvp_user.user.email)
                app.send_task('tasks.tasks.task_email', args=(
                    email_from, rsvp_user.user.email, subject, message))

    except Exception as e:
        print(e)


# for sending daily tasks
def debug_task_daily(self):
    print('task started')

    email_from = settings.EMAIL_HOST_USER
    try:
        events = my_task.objects.filter(
            remainder="Daily", date__gte=datetime.now().date())
        for event in events:
            rsvp_users = event.rsvp_users.all()
            subject = 'Remainder for the event- '+event.title
            print(subject)
            message = 'Event description: '+event.description+'\nDate of event: '+event.date.strftime(
                "%m/%d/%Y")+'\nFrom: '+event.time_from.strftime("%H:%M")+'\nTo: '+event.time_to.strftime("%H:%M")
            for rsvp_user in rsvp_users:
                print(rsvp_user.user.email)
                app.send_task('tasks.tasks.task_email', args=(
                    email_from, rsvp_user.user.email, subject, message))

        events_2 = my_task.objects.filter(
            remainder="Week before", date=datetime.now().date()+timedelta(days=7))
        for event in events_2:
            rsvp_users = event.rsvp_users.all()
            subject = 'Remainder for the event- '+event.title
            message = 'Event description: '+event.description+'\nDate of event: '+event.date.strftime(
                "%m/%d/%Y")+'\nFrom: '+event.time_from.strftime("%H:%M")+'\nTo: '+event.time_to.strftime("%H:%M")
            for rsvp_user in rsvp_users:
                print(rsvp_user.user.email)
                app.send_task('tasks.tasks.task_email', args=(
                    email_from, rsvp_user.user.email, subject, message))

    except Exception as e:
        print(e)
# for sending weekly tasks


def debug_task_weekly(self):
    print('task started')

    email_from = settings.EMAIL_HOST_USER
    try:
        events = my_task.objects.filter(
            remainder="Weekly", date__gte=datetime.now().date())
        for event in events:
            rsvp_users = event.rsvp_users.all()
            subject = 'Remainder for the event- '+event.title
            print(subject)
            message = 'Event description: '+event.description+'\nDate of event: '+event.date.strftime(
                "%m/%d/%Y")+'\nFrom: '+event.time_from.strftime("%H:%M")+'\nTo: '+event.time_to.strftime("%H:%M")
            for rsvp_user in rsvp_users:
                print(rsvp_user.user.email)
                app.send_task('tasks.tasks.task_email', args=(
                    email_from, rsvp_user.user.email, subject, message))

    except Exception as e:
        print(e)
# for sending monthly tasks


def debug_task_monthly(self):
    print('task started')

    email_from = settings.EMAIL_HOST_USER
    try:
        events = my_task.objects.filter(
            remainder="Monthly", date__gte=datetime.now().date())
        for event in events:
            rsvp_users = event.rsvp_users.all()
            subject = 'Remainder for the event- '+event.title
            print(subject)
            message = 'Event description: '+event.description+'\nDate of event: '+event.date.strftime(
                "%m/%d/%Y")+'\nFrom: '+event.time_from.strftime("%H:%M")+'\nTo: '+event.time_to.strftime("%H:%M")
            for rsvp_user in rsvp_users:
                print(rsvp_user.user.email)
                app.send_task('tasks.tasks.task_email', args=(
                    email_from, rsvp_user.user.email, subject, message))

    except Exception as e:
        print(e)


@app.task()
def task_email(email_from, email_to, subject, message):
    send_mail(subject, message, email_from, [email_to])
