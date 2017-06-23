from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=120, blank=True)
    content = models.TextField()
    create_time = models.DateField(auto_now=True)
    modify_time = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.name
