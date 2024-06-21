from django.urls import path
from csk.views import *

app_name='Team_1'
urlpatterns = [
    path('msd/',msd,name='msd'),
    path('captain/',captain,name='captain')
]