from django.shortcuts import render ,HttpResponse
from . import models

def index(request):
    context = {}
   
       
    classes = models.Classes.objects.all().order_by("id")
   
    context ['classes'] = classes
    
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def general(request):
    context = {}
   
       
    classes = models.Classes.objects.filter(class_category=1).order_by("id")
   
    context ['classes'] = classes
    return render(request,'general.html',context)

def special_subjects(request):
    context = {}
   
       
    classes = models.Classes.objects.filter(class_category=2).order_by("id")
   
    context ['classes'] = classes
 
   
    return render(request, 'special_subjects.html',context)

def optional_subjects(request):
    context = {}
   
       
    classes = models.Classes.objects.filter(class_category=3).order_by("id")
   
    context ['classes'] = classes
 
   
    return render(request, 'optional_subjects.html',context)



    
