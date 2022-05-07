from django.shortcuts import render, redirect

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

import json
import time
import os

from .models import *
from .serializers import *

import pandas as pd
import numpy as np
import pyAgrum as gum

# Create your views here.

path = os.path.realpath(__file__)
print("Le répertoire courant est : " + path)
print("")
print("Importing the Bayesian network")
if os.environ.get('ENV') == 'PRODUCTION':
    bn=gum.loadBN("app\virtual_patient_api\media\Bayesian_network.bif")
else:
    bn=gum.loadBN("virtual_patient_api\media\Bayesian_network.bif")
print("")
print("Successful import")
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
def inference_disease_symptoms(request):
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
      for disease in list_diseases:
        res[disease] = infere_network(disease, symptoms)[1]

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
      This view is returned when no url matches the one called
    """
    result = {
      "status": False,
      "message": "Check your URL",
      "data": {}
    }
    return Response(result, status=status.HTTP_404_NOT_FOUND)


def root(request):
    return redirect('/api')