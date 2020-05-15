from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Pet, Vaccine

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
        }) # request obj, name of html page, context to pass
    except Pet.DoesNotExist:
        return home(request)