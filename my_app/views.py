from django.shortcuts import render ,HttpResponse

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse('about')

def contact(request):
    return HttpResponse('contact')



    
