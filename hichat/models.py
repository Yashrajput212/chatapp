from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['username']



class Room(models.Model):
    name = models.CharField(max_length=200)
    users = models.ManyToManyField("User", related_name="RoomUsers")
    read = models.BooleanField(default=False)
    modified = models.DateTimeField()
    last_modifier = models.IntegerField(blank=True, null=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "users": [user.id for user in self.users.all()],
            "username": [user.username for user in self.users.all()],
            "read": self.read,
            "modified": self.modified.strftime("%b %d %Y, %I:%M %p"),
            "last_modifier": self.last_modifier
        }

class Message(models.Model):
    room = models.ForeignKey("Room", on_delete=models.CASCADE, related_name="messageRoom")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="MessageUser")
    text = models.TextField(max_length=1000, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    

class Contacts(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey("User", on_delete=models.CASCADE, related_name="contactOwner")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="contactUser")

    def __str__(self):
        return self.name