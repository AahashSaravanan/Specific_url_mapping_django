from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def msd(request):
    return HttpResponse('<h1>Msd is the best World Class player<h1>')

def captain(request):
    return HttpResponse('<h1>Ruturaj is the Captain of Csk<h1> ')