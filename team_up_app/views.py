from django.shortcuts import render, redirect
from .models import Team
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required # function based views
from django.contrib.auth.mixins import LoginRequiredMixin # for CBVS


# Import HttpResponse to send text-based responses
""" class Team():
    def __init__(self,name,mid,top,bot,sup,jg):
        self.name = name
        self.mid = mid
        self.top = top]
        self.bot = bot
        self.jg = jg
        self.sup = sup
 
teams = [
    Team('winners', 'middle', 'top', 'bottom', 'jungle', 'soraka'),
    Team('jinxers', 'fizz', 'trundle', 'caitlyn', 'rengar', 'nami'),
    Team('topsiders', 'neeko', 'fiora', 'jinx', 'warwick', 'biltzcrank'),
    Team('rats', 'katarina', 'kled', 'twitch', 'teemo', 'pantheon')
]
"""

# Define the home view function

""" 
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Home sweet home</h1>') """

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('<h1>about</h1>')

""" def index(request):
    teams = Team.objects.all()
    return render(request, 'index.html', {'teams':teams}) """
class TeamList(ListView):
    model = Team

    
def detail(request, team_id):
    team = Team.objects.get(id=team_id)
    return render(request, 'teams/team_detail.html', {'team':team})
    
class TeamCreate(CreateView):
    model = Team
    fields = '__all__'
    pk_url_kwarg = 'team_id'
    
    
class TeamDelete(DeleteView):
    model = Team
    pk_url_kwarg = 'team_id'
    success_url = '/teams/'
    
    
class TeamUpdate(UpdateView):
    model = Team
    fields = '__all__'
    pk_url_kwarg = 'team_id'
    template_name = './team_up_app/team_form.html' #teamplate name needs to be address! within template folder!
    success_url = '/teams/'
    

#auth

class About(LoginView): #home 
    template_name='about.html'
    

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save() #saves new user to database
            login(request,user)
            return redirect('team_list') #appears different bc user if/else
        else:
            error_message = 'Please try again :('
    else:
        form = UserCreationForm()  # Create an empty form for GET requests

    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)