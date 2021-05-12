from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=75)
    rating_system = models.CharField(max_length=15)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    friends = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model):
