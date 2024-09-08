from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world from home")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello world from about")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("Hello world from contact")
    return render(request, 'website/contact.html')