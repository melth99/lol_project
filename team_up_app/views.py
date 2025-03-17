from django.db.models.query import QuerySet
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
    team = Team.objects.get(id=team_id)
    return render(request, "teams/team_detail.html", {"team": team})


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
