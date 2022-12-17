from multiprocessing import context
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from .models import *
from .aigenerator import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from random import randint

def homePage(request):

    NounDictionary = {"bestfriendsname":"IMG1", "mother":"IMG2", "spouse":"IMG3"}
    TraitDictionary = {"superpower":"IMG", "fear":"IMG2","loved":"IMG3"}
    LocationDictionary = {"camp":"IMG1", "high school":"IMG2", "church":"IMG3"}

    NounKeys = sorted(NounDictionary.keys())
    TraitKeys = sorted(TraitDictionary.keys())
    LocationKeys = sorted(LocationDictionary.keys())

    RandomKey1 = []
    RandomKey2 = []
    RandomKey3 = []

    for counter in range(2):
        index = randint(0,2)
        RandomNounKey = NounKeys[index]
        RandomTraitKey = TraitKeys[index]
        RandomLocationKey = LocationKeys[index]
        RandomKey1.append(RandomNounKey)
        RandomKey2.append(RandomTraitKey)
        RandomKey3.append(RandomLocationKey)

    re_index = randint(0,1)
    context = {
            "name":RandomKey1[re_index],
            "power":RandomKey2[re_index],
            "location":RandomKey3[re_index],
        } 
    
    
    if request.method == 'POST':
        bookImg = "someone called " + request.POST['name'] + " with " + request.POST['power'] + " powers in " + request.POST['location']
        name = request.POST["name"]
        power = request.POST["power"]
        location = request.POST["location"]
        context = {
            "name":name,
            "power":power,
            "location":location,
        }
            
        context['storybookStory'] = returnStorybookStory(name, power, location)
        context['coverImage'] = returnStorybookImg(bookImg)[0]
        context['image2'] = returnStorybookImg(bookImg)[1]

        return render(request, 'html/base/img.html', context)

    return render(request, 'html/base/home.html', context)



def ImgPage(request):

    context = {} 
    return render(request, 'html/base/img.html', context)