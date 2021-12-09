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