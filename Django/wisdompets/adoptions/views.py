from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.core.exceptions import *

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html',{'pets':pets})

def pet_detail(request, id):
    try: 
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet Not Found')
    return render(request, 'pet_detail.html',{'pet':pet})

def getting_input(request):
    # pets = Pet.objects.all()
    # print(request.GET)
    # print(request.POST)
    if request.method == "POST":
        title = request.POST.get('title')
        print(title)
        context = {}
        return render(request,  'getting_input.html',context)