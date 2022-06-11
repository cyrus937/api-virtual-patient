from django.urls import path, include, re_path
#from django.conf.urls import url
from rest_framework import routers

from . import views

urlpatterns = [
    #path('', include(routers.urls)),

    path('response/',views.response, name='response'),
    #path('rating/',views.rating, name='rating'),
    re_path(r'^[a-zA-Z0-9/,;:!\\*-+^$ù&é(-è_çà)]+/$', views.errorPage),
    
]