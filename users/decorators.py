from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# Custom Decorator
def club(function):
    def _function(request, *args, **kwargs):
        if not request.user.profile.club_status:
            messages.info(request, 'You Are Not A Club Member')
            return HttpResponseRedirect(reverse('tasks-home'))
        return function(request, *args, **kwargs)

    return _function


def swagger(function):
    def _function(request, *args, **kwargs):
        if not request.user.profile.club_status:
            messages.info(request, 'You Are Not A Club Member')
            return HttpResponseRedirect(reverse('tasks-home'))
        return function(request, *args, **kwargs)

    return _function