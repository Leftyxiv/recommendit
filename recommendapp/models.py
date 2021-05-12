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
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    website = models.CharField(max_length=250)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    rating = models.IntegerField(min=0, max=5)
    like = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_words = models.CharField(max_length=100)
    description = models.TextField()
    comment = models.TextField()
    # agree
    # disagree
    # category

class Comments(models.Model):
    poster = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    text = models.TextField()