from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Pet, Vaccine
from django.db import models


def home(request):
    try:
        allpets = Pet.objects.all()
    except:
        raise Http404('we could not load pets for you')
    return render(request, 'home.html', {
        'pets': allpets,
        'testArg': 2137
    })


def pet_detail(request, pet_id: int):
    try:
        pet = Pet.objects.get(id=pet_id)
        return render(request, 'pet_detail.html', {
            'pet': pet
        })  # request obj, name of html page, context to pass
    except Pet.DoesNotExist:
        return home(request)


def create_pet_get(request):
    pet = Pet(name='random', breed='random')
    return render(request, 'create_pet.html', {'pet': pet})


def create_pet_post(request, pet_name):
    try:
        pet2 = Pet(name=pet_name, submitter='asd', species='asdasd', breed='asd',
                   description='asdasd', sex='M', submission_date='2007-01-01 10:00:00')
        pet2.save()
    except:
        return render(request, 'dupa.html')
        # return Http404('we could not create a pet')
    return home(request)
