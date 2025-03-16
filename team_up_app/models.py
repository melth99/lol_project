from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
#encrypt password later!
""" 
class User:
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
"""

class Team(models.Model):
    
    name = models.CharField(max_length=15)
    top = models.CharField(max_length=15) #for now just type in selection later
    mid = models.CharField(max_length=15)
    bot = models.CharField(max_length=15)
    support = models.CharField(max_length=15)
    jungle = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name #
    
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('team-detail', kwargs={'team_id': self.id})
    
    
