from asyncio import constants
from audioop import avg
from unicodedata import decimal
from django.shortcuts import redirect
from patient_app.models import LeanerPhysician
from patient_app.serializers import LeanerPhysicianSerializer
from patient_app.views import Convert
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.db.models import Sum
import json
from decimal import Decimal

from .models import *
from .serializers import *

# Create your views here.
class SymptomViewSet(viewsets.ModelViewSet):
  queryset = Symptom.objects.all()
  serializer_class = SymptomSerializer

class DiseaseViewSet(viewsets.ModelViewSet):
  queryset = Disease.objects.all()
  serializer_class = DiseaseSerializer

class WeightSymptomDiseaseViewSet(viewsets.ModelViewSet):
  queryset = WeightSymptomDisease.objects.all()
  serializer_class = WeightSymptomDiseaseSerializer

class SystemViewSet(viewsets.ModelViewSet):
  queryset = System.objects.all()
  serializer_class = SystemSerializer

class WeightDiseaseSystemViewSet(viewsets.ModelViewSet):
  queryset = WeightDiseaseSystem.objects.all()
  serializer_class = WeightDiseaseSystemSerializer

class RatingDiseaseViewSet(viewsets.ModelViewSet):
  queryset = RatingDisease.objects.all()
  serializer_class = RatingDiseaseSerializer

class RatingSystemViewSet(viewsets.ModelViewSet):
  queryset = RatingSystem.objects.all()
  serializer_class = RatingSystemSerializer

@api_view(['GET'])
def getratingUser(request, pk):
  systems = {}
  diseases = {}
  det = {}
  details = {}
  context = {
        'request': request,
    }

  try: 
    learner = LeanerPhysicianSerializer(LeanerPhysician.objects.get(pk=pk), many=False, context=context).data
  except LeanerPhysician.DoesNotExist: 
    return JsonResponse({'message': 'The learner does not exist'}, status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':

    rating_system = RatingSystemSerializer(RatingSystem.objects.all().filter(learner=learner["id"]), many=True, context=context).data

    for sys in rating_system:
      sys = Convert(sys, {})
      s = sys["system"].split('/')
      syst = SystemSerializer(System.objects.get(pk=s[-2]), many=False, context=context).data
      systems[syst["name"]] = sys["rating"]

      det["rating"] = sys["rating"]
      diseases_rating = RatingDiseaseSerializer(RatingDisease.objects.all().filter(system=s[-2], learner=learner["id"]), many=True, context=context).data
      for dis_rate in diseases_rating:
        dis_rate = Convert(dis_rate, {})
        d = dis_rate["disease"].split('/')
        dis = DiseaseSerializer(Disease.objects.get(pk=d[-2]), many=False, context=context).data
        det[dis["name"]] = dis_rate["rating"]
      
      details[syst["name"]] = det

      det = {}

    
    #rating_disease = RatingDiseaseSerializer(RatingDisease.objects.all().filter(learner=learner["id"]), many=True, context=context).data
    rating_disease = list(Disease.objects.annotate(rating=Sum('ratingdisease__rating')).values('name', 'rating', 'ratingdisease__learner').filter(ratingdisease__learner=pk))
    """for dis in rating_disease:
      dis = Convert(dis, {})
      disease = DiseaseSerializer(Disease.objects.get(pk=dis["disease"]), many=False, context=context).data
      diseases[disease["name"]] = dis["rating"]"""
    for dis in rating_disease:
      diseases[dis["name"]] = dis["rating"]
    
    result = {
      "system":systems if systems else None,
      "disease":diseases if diseases else None,
      "detail":details if details else None
    }

  return Response(result, status=status.HTTP_200_OK)

@api_view(['POST'])
def rating(request):
  body = json.loads(request.body)
  context = {
        'request': request,
    }

  if body == None:
    result = {
      "status": "FAILURE",
      "message": "learner, system, disease, symptoms required"
    }
    return Response(result, status.HTTP_204_NO_CONTENT)
  else:
    if 'learner' not in body:
      result = {
        "status": "FAILURE",
        "message": "learner required"
      }
      return Response(result, status.HTTP_204_NO_CONTENT)
    if 'system' not in body:
      result = {
        "status": "FAILURE",
        "message": "system required"
      }
      return Response(result, status.HTTP_204_NO_CONTENT)
    if 'disease' not in body:
      result = {
        "status": "FAILURE",
        "message": "disease required"
      }
      return Response(result, status.HTTP_204_NO_CONTENT)
    if 'symptoms' not in body:
      result = {
        "status": "FAILURE",
        "message": "symptoms required"
      }
      return Response(result, status.HTTP_204_NO_CONTENT)
  
  try:
    learner = LeanerPhysician.objects.get(pk=body["learner"])
  except LeanerPhysician.DoesNotExist: 
    return JsonResponse({'message': 'The learner does not exist'}, status=status.HTTP_404_NOT_FOUND)

  sys = System.objects.get(pk=body["system"])
  for disease in body["disease"] :
    try:
      weight_disease = Decimal(WeightDiseaseSystemSerializer(WeightDiseaseSystem.objects.get(disease=disease, system=body["system"]), many=False, context=context).data["weight"])
    except WeightDiseaseSystem.DoesNotExist:
      continue
    
    for symptom in body["symptoms"]:
      try:
        weight_symptom = WeightSymptomDiseaseSerializer(WeightSymptomDisease.objects.get(disease=disease, symptom=symptom), many=False, context=context).data
      except WeightSymptomDisease.DoesNotExist:
        continue
      
      weight_symptom = Decimal(weight_symptom["weight"])
      try:
        rating_disease = RatingDisease.objects.get(disease=disease, system=body["system"], learner=body["learner"])
        rating_disease.rating += weight_symptom
        rating_disease.rating = rating_disease.rating
        rating_disease.save()
      except RatingDisease.DoesNotExist:
        dis = Disease.objects.get(pk=disease)
        rating_disease = RatingDisease.objects.create(
          rating = weight_symptom,
          disease = dis,
          learner = learner,
          system = sys
        )
        rating_disease.save()
      
    try:
      rating_system = RatingSystem.objects.get(system=body["system"], learner=body["learner"])
      rating_system.rating += rating_disease.rating * weight_disease
      rating_system.save()
    except RatingSystem.DoesNotExist:
      rating_system = RatingSystem.objects.create(
        rating = round(rating_disease.rating * weight_disease, 3),
        system = sys,
        learner = learner
      )
      rating_system.save()
  
  result = {
      "message": "rating success",
      "status": True
    }

  return Response(result, status=status.HTTP_200_OK)

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
    return Response(result, status=status.HTTP_200_OK)


def root(request):
    return redirect('/api')