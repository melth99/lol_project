from django.urls import path

from . import views

# Import views to connect routes to view functions
#from django.views.generic.edit import CreateView
#from .models import Predator


urlpatterns = [
    path('', views.About.as_view(), name='about'),
    #path('about/', views.about, name='about'),
    path('teams/', views.TeamList.as_view(), name= 'team-list'),
    path('teams/create/', views.TeamCreate.as_view(), name='team-form'),
    path('teams/<int:team_id>/', views.detail, name='team-detail'),
    path('teams/<int:team_id>/update/', views.TeamUpdate.as_view(), name='team-update'),
    path('teams/<int:team_id>/delete/', views.TeamDelete.as_view(), name='team-delete'),
    path('teams/dictionary/', views.dictionary, name='dictionary'),
    #auth
    path('accounts/signup/', views.signup, name='signup'),

    
    
]