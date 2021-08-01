from django.urls import path
from .views import *


app_name='NATURE_CLUB'

urlpatterns = [
    path('', Home, name='Home'),
    path('nature_club/About', About, name='About'),
    path('nature_club/Contact', Contact, name='Contact'),
    path('nature_club/Gallery', gallery, name='Gallery'),

    path('nature_club/subcom/tree/', tree, name='tree-planting'),
    path('nature_club/subcom/debate/', debate, name='debate-and-writing'),
    path('nature_club/subcom/bird/', bird, name='birding'),

    path('nature_club/executive/presidential/', presid, name='presidential'),
    path('nature_club/executive/editor/', editor, name='editor'),
    path('nature_club/executive/secretary/', sec, name='secretary'),

    path('nature_club/Search/', SearchResultsView.as_view(), name='search_results'),
    path('nature_club/pdf',getpdf, name='getpdf'),
    # path('nature_club/pdf/download',download_pdf, name='download_pdf'),
    # path('nature_club/Search/', SearchResultsView, name='search_results'),
    # path('nature_club/download/<str:filepath>/', downloads, name="downloads"),
]
