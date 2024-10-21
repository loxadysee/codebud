from django.shortcuts import render
from .models import Room


rooms = [
    {   'id': 1,
        'name': 'room1',
        'description': 'room1 description',
        'image': 'room1.jpg',
        'price': 100,
        'capacity': 10,
        'is_active': True,
        'is_free': True,
    },
    {   'id': 2,
        'name': 'room2',
        'description': 'room2 description',
        'image': 'room2.jpg',
        'price': 200,
        'capacity': 20,
        'is_active': True,
        'is_free': False,
    },
    
]
def home(request):
    room = Room.objects.all()
    context = {'rooms': room}
    return render(request, 'base_app/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    
    return render(request, 'base_app/room.html', context)
