from django.urls import path, include, re_path
#from django.conf.urls import url
from rest_framework import routers

from . import views

routers = routers.DefaultRouter()
routers.register(r'media', views.MediaViewSet)

urlpatterns = [
    path('', include(routers.urls)),

    path('inference/',views.inference_maladie_symptoms, name='inference_maladie_symptoms'),
    re_path(r'^[a-zA-Z0-9/,;:!\\*-+^$ù&é(-è_çà)]+/$', views.errorPage),
    
]