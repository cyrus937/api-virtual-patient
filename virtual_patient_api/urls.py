"""virtual_patient_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.decorators import api_view
from rest_framework.response import Response
from patient_app import views

@api_view(['GET'])
def root(request):
    """
        Entry point of the API
    """
    
    return Response({
        "PATIENT VIRTUEL API": request.build_absolute_uri() + 'patient-virtuel/',
    })

urlpatterns = [
    path('', views.root),
    path('api/', root),
    path('api/patient-virtuel/', include('patient_app.urls')),

    path('admin/', admin.site.urls),
]
