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
    
    # print(request)
    print(request.method)
    
    
    if request.method == "POST":
        data = request.POST.dict()
        text = data.get("text")
        print(text)
        return HttpResponse("This is a post request")
    context = {}
    return render(request,  'getting_input.html',context)