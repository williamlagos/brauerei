from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    text = models.TextField()
