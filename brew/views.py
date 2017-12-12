from brew.models import Message
from brew.serializers import UserSerializer, GroupSerializer
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

def send(request):
    name = request.POST.get('name')
    text = request.POST.get('text')
    email = request.POST.get('email')
    m = Message(name=name, text=text, email=email)
    m.save()
    return HttpResponseRedirect('/')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
