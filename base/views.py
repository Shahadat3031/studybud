from django.shortcuts import render
from .models import Room

# Create your views here.

# This is the view function that will be called when the user visits the home page [1]
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    rooms = Room.objects.get(id=pk)
    context = {'room' : rooms}
    return render(request, 'base/room.html', context)

def about(request):
    return render(request, 'base/about.html')
