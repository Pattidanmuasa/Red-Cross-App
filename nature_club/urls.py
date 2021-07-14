from django.urls import path
from .views import *

app_name='NATURE_CLUB'

urlpatterns = [
    path('', Home, name='Home'),
    path('nature_club/About', About, name='About'),
    path('nature_club/Contact', Contact, name='Contact'),
    path('nature_club/Gallery', gallery, name='Gallery'),
    path('nature_club/Events', events, name='Events'),
]