import random

from django.shortcuts import render, redirect

from .models import TournamentParticipant, Shiba

# Create your views here.

def home(request):
    print("accessing the homepage")

    return render(request, 'pages/home.html')

def lessons(request):
    print("accessing the lessons page")

    return render(request, 'pages/lessons.html')

def events(request):
    print("accessing the events page")

    return render(request, 'pages/events.html')


def tournaments(request):
    print("accessing the tournaments page")
    context = {}
    #TournamentParticipant.objects.create(
    #    age=2,
    #    name='wallace',
    #)
    print(request.POST)


    if 'name' in request.POST:
        age = int(request.POST['age'])
        name = request.POST['name']
        print('They entered:', name)
       

        return redirect('tournaments')

      
    #    TournamentParticipant.objects.create(
    #        age=age,
    #        name=name,
    #    )

        # Finally, we'll just redirect to '/'
    #    return redirect('/')


    return render(request, 'pages/tournaments.html', context)


def add_dog(request):
    print("viewing add_dog function")
    context = {}  # No need for context on this page

    if 'name' in request.POST:
        age = int(request.POST['age'])
        name = request.POST['name']
        print('They entered:', name)

        # Add a new Shiba to our database
        # For now, we'll just make them all have the same image
        Shiba.objects.create(
            age=age,
            name=name,
            #image_src='https://i.imgur.com/VEslUBl.png',
        )

        # Finally, we'll just redirect to '/'
        return redirect('/')


    # "add_dog.html" tells Django to look for the template in
    # `templates/add_dog.html'
    return render(request, 'pages/add_dog.html', context)