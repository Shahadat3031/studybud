from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# Python dictionary that contains the data of the rooms
rooms = [
    {
        'id': 1,
        'title': 'Room 1',
        'price': 500,
        'rating': 4.5,
        'image': 'room_1.jpg',
        'description': 'This is the description of room 1'},
    {
        'id': 2,
        'title': 'Room 2',
        'price': 600,
        'rating': 4.7,
        'image': 'room_2.jpg',
        'description': 'This is the description of room 2'},
    {
        'id': 3,
        'title': 'Room 3',
        'price': 700,
        'rating': 4.9,
        'image': 'room_3.jpg',
        'description': 'This is the description of room 3'},
    {
        'id': 4,
        'title': 'Room 4',
        'price': 800,
        'rating': 4.8,
        'image': 'room_4.jpg',
        'description': 'This is the description of room 4'},
    {
        'id': 5,
        'title': 'Room 5',
        'price': 900,
        'rating': 4.6,
        'image': 'room_5.jpg',
        'description': 'This is the description of room 5'},
    ]
    
# This is the view function that will be called when the user visits the home page [1]
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    return render(request, 'base/room.html')

def about(request):
    return render(request, 'base/about.html')
