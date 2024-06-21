from django.urls import path
from rcb.views import *

app_name='Team_2'
urlpatterns = [
    path('virat/',virat,name='virat'),
    path('captain/',captain,name='captain'),
]