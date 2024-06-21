from django.urls import path
from dc.views import *

app_name='Team_2'
urlpatterns = [
    path('pant/',pant,name='pant'),
    path('captain/',captain,name='captain'),
]