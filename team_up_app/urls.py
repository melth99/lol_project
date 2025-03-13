from django.urls import path
from . import views # Import views to connect routes to view functions
#from django.views.generic.edit import CreateView
#from .models import Predator


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teams/', views.index, name= 'index'),
    #path('teams/create/', views.PredatorCreate.as_view(), name='predator-form'),
]
#