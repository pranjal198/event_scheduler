from __future__ import absolute_import, unicode_literals
import os
import django

from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_scheduler.settings')
app = Celery('event_scheduler', broker='redis://localhost:6379')

app.config_from_object('django.conf:settings', namespace='CELERY')
django.setup()


app.conf.timezone = 'Asia/Kolkata'

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-mail-custom': {
        'task': 'tasks.tasks.debug_task_custom',
        'schedule': crontab(hour=5, minute=30,),
        'args': (),
    },
    'send-mail-daily': {
        'task': 'tasks.tasks.debug_task_daily',
        'schedule': crontab(hour=6, minute=00,),
        'args': (),
    },
    'send-mail-weekly': {
        'task': 'tasks.tasks.debug_task_weekly',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (),
    },
    'send-mail-monthly': {
        'task': 'tasks.tasks.debug_task_monthly',
        'schedule': crontab(hour=7, minute=00, day_of_month=1),
        'args': (),
    },
}
# to run celery
# celery -A event_scheduler worker --pool=solo -l info

# to run celery beat
# celery -A event_scheduler beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
