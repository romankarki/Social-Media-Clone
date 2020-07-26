from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):

    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, related_name="profiles", on_delete=models.CASCADE, null=True, unique=True)

    def __str__(self):
        return self.name
