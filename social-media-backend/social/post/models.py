from django.db import models
from django.contrib.auth.models import User
from user_profile.models import UserProfile
# Create your models here.


class Post(models.Model):

    name = models.CharField(max_length=200)
    content = models.CharField(max_length=400)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, related_name="posts",
                             on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=200,  null=True)

    def __str__(self):
        return self.name
