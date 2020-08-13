from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import date, datetime, timedelta

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=25, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    birthday = models.DateField(null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profiles_index')

class Todo(models.Model):
    title = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Url(models.Model):
    url = models.URLField(max_length=400, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()