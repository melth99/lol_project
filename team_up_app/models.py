from django.db import models
from django.urls import reverse
#encrypt password later!

""" 
class User:
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=30)


class Team(models.Model):
    user = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    team_name = models.CharField(max_length=15)
    top = models.CharField(max_length=15) #for now just type in
    mid = models.CharField(max_length=15)
    bot = models.CharField(max_length=15)
    support = models.CharField(max_length=15)
    jungle = models.CharField(max_length=15) """