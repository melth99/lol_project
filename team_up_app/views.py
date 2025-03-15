from django.shortcuts import render
from .models import Team
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponse
from django.views.generic import ListView


# Import HttpResponse to send text-based responses
""" class Team():
    def __init__(self,name,mid,top,bot,sup,jg):
        self.name = name
        self.mid = mid
        self.top = top
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


def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Home sweet home</h1>')

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
    #success_url = '/teams/'
    fields = '__all__'