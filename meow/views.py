from inertia import render
from random import randint

from .models import Message

def home(request):
    messages = Message.objects.order_by('created_at').all()
    return render(request, 'Home', props={
        'messages': messages
    })

def events(request):
    return render(request, 'Events/Index', props={
        'events': ['An event', 'another event', 'Yet another event']
    })


def contact(request):
    return render(request, 'Contact', props={
        'supportEmail': 'test@example.org'
    })
