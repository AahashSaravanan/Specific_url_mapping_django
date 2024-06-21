from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pant(request):
    return HttpResponse('<h1>Pant is the best finisher<h1>')

def captain(request):
    return HttpResponse('<h1>Pant is the Captain of rcb<h1> ')