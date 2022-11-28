from inertia import render
from random import randint
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Message

@ensure_csrf_cookie
def home(request):
    messages = Message.objects.order_by('created_at').all()
    return render(request, 'Home', props={
        'messages': messages,
    })

def send_msg(request):
    if request.method == 'POST':
        message = request.POST['message']
        return render(request, 'Meow', props={'message': message})

def events(request):
    return render(request, 'Events/Index', props={
        'events': ['An event', 'another event', 'Yet another event']
    })


def contact(request):
    return render(request, 'Contact', props={
        'supportEmail': 'test@example.org'
    })
