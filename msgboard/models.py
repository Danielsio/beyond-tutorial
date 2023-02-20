from django.db import models
from django.utils import timezone

# To describe the structure of our application’s database. the Message-Table
class Message(models.Model):
    author = models.CharField(max_length=200)         # author field
    text = models.TextField()                         # text field
    date = models.DateTimeField(default=timezone.now) # date field
    