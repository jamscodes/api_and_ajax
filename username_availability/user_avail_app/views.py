from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('You\'re up and running!')
