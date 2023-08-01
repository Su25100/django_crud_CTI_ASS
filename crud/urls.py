from django.urls import path
from . views import *
urlpatterns = [
    path('book/',Book_view),
    
]
