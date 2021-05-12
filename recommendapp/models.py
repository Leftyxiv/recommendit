from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=75)
    rating_system = models.CharField(max_length=15)
    # photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    # friends = models.ForeignKey(, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    website = models.CharField(max_length=250)
    # photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    like = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_words = models.CharField(max_length=100)
    description = models.TextField()
    comment = models.TextField()
    # agree
    # disagree
    # category

    def __str__(self):
        return self.name

class Comments(models.Model):
    poster = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Post on {self.post} by {self.poster}"