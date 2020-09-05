from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from hrtc.models import Buses, Busstop
# Create your views here.
def index(request):
    return render(request, "index.html")
def home(request):

        return render(request, "home.html")
def track(request):
        return render(request, "track_live.html")

def search(request):
        return render(request, "search_bus.html")
def details(request):
    bus_no=buses.bus_no
    starting=buses.departure
    destination=buses.arrival
    time=buses.departure_time
    return render(request, "bus_details.html")
def contact(request):
        return render(request, "contact_us.html")
def slides(request):
        return render(request, "slideshow.html")
def side(request):
        return render(request,"side.html")
