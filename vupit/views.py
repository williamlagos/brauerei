from vupit.models import Message
from django.shortcuts import HttpResponseRedirect

def send(request):
    name = request.POST.get('name')
    text = request.POST.get('text')
    email = request.POST.get('email')
    m = Message(name=name, text=text, email=email)
    m.save()
    return HttpResponseRedirect('/')
