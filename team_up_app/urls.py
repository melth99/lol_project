from django.urls import path


from . import views

# Import views to connect routes to view functions
#from django.views.generic.edit import CreateView
#from .models import Predator


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teams/', views.TeamList.as_view(), name= 'team-list'),
    path('teams/create/', views.TeamCreate.as_view(), name='team-form'),
    path('teams/<int:team_id>/', views.detail, name='team-detail'),
    path('teams/<int:team_id>/update/', views.TeamUpdate.as_view(), name='team-update'),
    path('teams/<int:team_id>/delete/', views.TeamDelete.as_view(), name='team-delete')
    #auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/[name='login']', include('django.contrib.auth.urls')),
    path('accounts/logout/ [name='logout']', include('django.contrib.auth.urls')),
    path('accounts/password_change/ [name='password_change']', include('django.contrib.auth.urls')),
    path('accounts/password_change/done/ [name='password_change_done']', include('django.contrib.auth.urls')),
    path('accounts/password_reset/done/ [name='password_reset_done']', include('django.contrib.auth.urls')),
    path('accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']', include('django.contrib.auth.urls')),
    path('accounts/reset/done/ [name='password_reset_complete']', include('django.contrib.auth.urls'))
    
]


    
