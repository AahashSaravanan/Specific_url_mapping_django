from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def virat(request):
    return HttpResponse('<h1>Virat has the most century record<h1>')

def captain(request):
    return HttpResponse('<h1>Faf is the Captain of rcb<h1> ')
