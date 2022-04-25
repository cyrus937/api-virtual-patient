from django.shortcuts import render, redirect

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

import json
import time

from .models import *
from .serializers import *

import pandas as pd
import numpy as np
import pyAgrum as gum
import pyAgrum.lib.notebook as gnb

# Create your views here.
class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer



# Réseau bayésien
# Importation du réseau bayésien
print("")
print("Importation du réseau bayésien")
bn=gum.loadBN("virtual_patient_api\media\Bayesian_network.bif")
print("")
print("Importation réussie")
print("")

list_diseases = ['Malaria', 'Tuberculosis', 'Diabetes_', 'Typhoid', 'hepatitis_A', 'Hepatitis_B', 'Hypoglycemia', 'Common_Cold', 'Chicken_pox', 'Pneumonia']

def infere_network(disease, symptoms):
  global bn
  ie=gum.LazyPropagation(bn)

  ie.setEvidence(symptoms)
  ie.makeInference()
  return ie.posterior(disease)

def Convert(tup, di):
  for a, b in tup: 
    di[a] = b
  return di

@api_view(['POST'])
def inference_maladie_symptoms(request):
  res = {}
  symp = {}
  body = json.loads(request.body)
  
  if body == None:
    result = {
            "status": "FAILURE",
            "message": "disease or symptoms required"
        }
    return Response(result, status.HTTP_204_NO_CONTENT)
  
  else:
    symptoms = body['symptoms']
    
    if 'disease' not in body:
      for dis in list_diseases:
        res[dis] = infere_network(dis, symptoms)[1]

      dic = Convert(sorted(res.items(), key=lambda x: x[1], reverse=True), {})
      res = dict(list(dic.items())[0: 5])
      
      return Response(res, status=status.HTTP_201_CREATED)
    else:
      disease = body['disease']
      res[disease] = infere_network(disease, symptoms)[1]
      
      return Response(res, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def errorPage(request):
    """
                Cette vue est renvoyé lorsque aucune url ne correspond a celle appelé
        """
    result = {
        "status": False,
        "message": "Vérifiez votre URL",
        "data": {}
    }
    return Response(result, status=status.HTTP_404_NOT_FOUND)


def root(request):
    return redirect('/api')