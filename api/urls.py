from django.urls import path
from api.views import *

urlpatterns = [
    path('', index, name='index'),
    # intelligence
    # overview
    path('getSales', getSales, name='getSales'),
    # customer
    path('top10Customer', top10Customer, name='top10Customer'),

]