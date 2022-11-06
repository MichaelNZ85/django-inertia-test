from inertia import render
from random import randint

def home(request):
    return render(request, 'Home', props={
        'test': randint(1,100)
    })

def events(request):
    return render(request, 'Events/Index', props={
        'events': ['An event', 'another event', 'Yet another event']
    })


def contact(request):
    return render(request, 'Contact', props={
        'supportEmail': 'test@example.org'
    })
