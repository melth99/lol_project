from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from django.shortcuts import render, redirect
from .models import Team
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required  # function based views
from django.contrib.auth.mixins import LoginRequiredMixin  # for CBVS
from .services import get_ddragon,get_alphabet


# Import HttpResponse to send text-based responses

# Define the home view function

""" 
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Home sweet home</h1>') """


def about(request):
    return render(request, "about.html")
    # return HttpResponse('<h1>about</h1>')


""" def index(request):
    teams = Team.objects.all()
    return render(request, 'index.html', {'teams':teams}) """


class TeamList(LoginRequiredMixin, ListView):
    model = Team

    def get_queryset(self):
        return Team.objects.filter(user=self.request.user)

    # limit to my own


def detail(request, team_id):
    # Fetch champion data
    champions = get_ddragon()
    
    # Get the specific team
    team = get_object_or_404(Team, id=team_id)

    # Extract specific champion data for each role
    top_champion = champions.get(team.top.capitalize())
    jungle_champion = champions.get(team.jungle.capitalize())
    mid_champion = champions.get(team.mid.capitalize())
    bot_champion = champions.get(team.bot.capitalize)
    support_champion = champions.get(team.support.capitalize())


    context = {
        'team': team,
        'champions': champions,
        'top_champion': top_champion,
        'jungle_champion': jungle_champion,
        'mid_champion': mid_champion,
        'bot_champion': bot_champion,
        'support_champion': support_champion,
    }
    return render(request, "teams/team_detail.html", context)

def dictionary(request): 
    champions = get_ddragon()  # Fetch champion data from services.py
    alpha_dict = get_alphabet
    alphabet = "abcdefghijkmnopqrstuvwxyz".upper()

    context = {
        'champions': champions,  # Pass champion data to the template
        'alpha_dict': alpha_dict,
        'alphabet': alphabet
        
    }
    print(type(champions), 'CHAMPION CHAMPION CHAMPION!!!!!!!!U932R9032R9032R930R283902R83920R839R208390R2839R08')
    champ_letters = {
    }
    
    return render(request, "positions.html", context)


class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    fields = ["name","top","mid","bot","support","jungle"]
    pk_url_kwarg = "team_id"
    def form_valid(self, form):
        # this is a place where you can add things to the form once it was submitted to the
        # server

        # assign the logged in user to the form (instance)that was submitted to the server
        form.instance.user = self.request.user # self.request.user is the logged in user! 
        # let the form add the new to the database now!
        return super().form_valid(form)
"""   def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

"""
class TeamDelete(LoginRequiredMixin, DeleteView):
    model = Team
    pk_url_kwarg = "team_id"
    success_url = "/teams/"


class TeamUpdate(LoginRequiredMixin, UpdateView):
    model = Team
    fields = fields = ["name","top","mid","bot","support","jungle"]
    pk_url_kwarg = "team_id"
    template_name = "./team_up_app/team_form.html"  # teamplate name needs to be address! within template folder!
    success_url = "/teams/"


# auth


class About(LoginView):  # home
    template_name = "about.html"


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # saves new user to database
            login(request, user)
            return redirect("team-list")  # appears different bc user if/else
        else:
            error_message = "Please try again :("
    else:
        form = UserCreationForm()
        print("bug is here")
        # Create an empty form for GET requests

    context = {"form": form, "error_message": error_message}
    print("line 86")
    print(context)
    return render(request, "signup.html", context)
