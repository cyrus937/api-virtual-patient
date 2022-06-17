from unittest import result
from django.shortcuts import render

import pandas as pd
from learner_app.views import getRating
import numpy as np
from patient_app.views import clinicalCase, getClinicalCase
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.http import HttpRequest

import requests as rq
import json
import ast

from datetime import datetime, timezone
import pytz
from difflib import SequenceMatcher

from nltk import PCFG
from random import randint

url_symptom = "https://57919.gradio.app/api/predict/"
session_symptom = "gnundql1bx"

url_life_style = "https://10381.gradio.app/api/predict/"
session_life_style = "kj8ktiw938q"

url_antecedent = "https://35134.gradio.app/api/predict/"
session_antecedent = "ex6c24vfiyj"

url_classify = "https://16195.gradio.app/api/predict/"
session_classify = "a2ematfe5f"

# Create your views here.
def getkeySymptom(text):
  r = rq.post(url_symptom, json={"fn_index": 0, "data": [text], "session_hash": session_symptom})
  t = r.json()
  result = {
    "data":ast.literal_eval(t["data"][0])
  }
  return result

def getkeyLifeStyle(text):
  r = rq.post(url_life_style, json={"fn_index": 0, "data": [text], "session_hash": session_life_style})
  t = r.json()
  result = {
    "data":ast.literal_eval(t["data"][0])
  }
  return result

def getkeyAntecedent(text):
  r = rq.post(url_antecedent, json={"fn_index": 0, "data": [text], "session_hash": session_antecedent})
  t = r.json()
  result = {
    "data":ast.literal_eval(t["data"][0])
  }
  return result

def classifyText(text):
  r = rq.post(url_classify, json={"fn_index": 0, "data": [text], "session_hash": session_classify})
  t = r.json()

  return t["data"][0]

def getPeriod():
  now = datetime.now()
  hr = now.hour + 1 # GMT+1  in Cameroon
  if (hr > 5 and hr < 12):
    return 'morning'
  elif (hr > 12 and hr < 18):
    return 'afternoon'
  else:
    return 'evening'

def getSymptoms(clinical_case, symptom):
  symptoms = clinical_case['symptom']
  for symp in symptoms:
    if symptom == symp['name']:
      return symp

def getLifeStyle(clinical_case, life):
  return clinical_case['life_style']

def getAntecedent(clinical_case, antec):
  return

def all_equal(prods):
  max = prods[0].prob()
  for prod in prods:
    if prod.prob() != max:
      return False
  return True

def get_max_prob(prods):
  """
    get production rule with the maximum probability.
    ex: A -> B[0.2] | CD[0.5] | E[0.3]: selects A -> CD, and returns [C, D] where C and D non terminals
  """
  if len(prods) == 1: # ex: A -> B[1.0]. No need to select max
    return list(prods[0].rhs()) # return list of elements on rhs
  elif all_equal(prods): # ex: A -> B[0.5] | C[0.5]. Choose at random to diversify words choosen, to broaden language
    index = randint(0, len(prods)-1)
    return list(prods[index].rhs())
  else: # A -> B[0.2] | CD[0.5] | E[0.3]
    max = 0
    maxIndex = 0
    index = 0
    for prod in prods:
      if prod.prob() > max:
        max = prod.prob()
        maxIndex = index

      index += 1
    return list(prods[maxIndex].rhs())

def get_word(grammar, non_terminal):
  """
    recursive algorithm: parses through the grammar (derivation tree) till we reach the leaves.
    At each level, we choose the leaf with the greatest probability.
  """
  prods = grammar.productions(lhs=non_terminal)
  prod = get_max_prob(prods) # list

  phrase = []
  for pr in prod:
    if type(pr) == str:
      if pr != '':
        phrase.append(pr)
    else:
      phrase.append(get_word(grammar, non_terminal=pr))
  
  return ' '.join(phrase)


def remove_spaces(word):
  """
    to principally remove unnecessary spaces when empty string from grammar is returned and spaces before full stop.
  """
  while word.find(' .') != -1:
    word = word.replace(' .', '.')
  
  word = word.replace('  ', ' ')

  return word

def similar(a, b):
  return SequenceMatcher(None, a, b).ratio()

def max_similar(keywords, word):
  max = 0
  maxWord = ''
  for key in keywords:
    sq = similar(key, word)
    if sq > max:
      max = sq
      maxWord = key
  
  return maxWord

def symptom_phrase_grammar(entities_ner, symptom_obj):
  """
    We create a grammar with varying probabilities considering the entities present in entities_ner
  """

  symptom_grammar = """
    S -> B1 B2 B3 B4 B5 B6 B7 [1.0]

    A1 -> 'I have' [0.3333] | 'Yes Doctor, I have' [0.3333] | 'I feel' [0.3333]
    A2 -> 'about' [0.25] | 'for about' [0.25] | 'around' [0.25] | 'nearly' [0.25]
    A3 -> 'since' [0.2] | 'for the past' [0.2] | 'for' [0.2] | 'for nearly' [0.2] | 'for about' [0.2]
    A4 -> '. The intensity is' [0.5] | ', and the intensity is quite' [0.5]
    A5 -> 'and it is triggered by' [0.25] | '. It is stimulated when I do' [0.25] | '. It starts when' [0.25] | '. The triggering activity is' [0.25]
    A6 -> '. The pain is located at' [0.25] | ' and the pain is located at' [0.25] | '. The pain is situated at' [0.25] | ' and the pain is positioned at' [0.25]
    A7 -> ". It's evolution is" [0.5] | '. The progress of the symptom is' [0.5]

  """

  if 'SYMPTOM' in entities_ner:
    symptom_grammar = symptom_grammar + "B1 -> A1 '" + symptom_obj['name'] + "' [1.0]\n"

  if 'FREQUENCY' in entities_ner:
    symptom_grammar = symptom_grammar + "B2 -> A2 '" + symptom_obj['frequency'] + "' [1.0] | [0.0]\n"
  else:
    symptom_grammar = symptom_grammar + "B2 -> A2 '" + "none" + "' [0.0] | [1.0]\n"

  if 'DURATION' in entities_ner:
    symptom_grammar = symptom_grammar + "B3 -> A3 '" + symptom_obj['duration'] + "' [1.0] | [0.0]\n"
  else:
    symptom_grammar = symptom_grammar + "B3 -> A3 '" + "none" + "' [0.0] | [1.0]\n"

  if 'INTENSITY' in entities_ner:
    symptom_grammar = symptom_grammar + "B4 -> A4 '" + symptom_obj['degree'] + "' [1.0] | [0.0]\n"
  else:
    symptom_grammar = symptom_grammar + "B4 -> A4 '" + "none" + "' [0.0] | [1.0]\n"

  if 'TRIGGER' in entities_ner:
    symptom_grammar = symptom_grammar + "B5 -> A5 '" + symptom_obj['triggering_activity'] + "' [1.0] | [0.0]\n"
  else:
    symptom_grammar = symptom_grammar + "B5 -> A5 '" + "none" + "' [0.0] | [1.0]\n"

  if 'LOCALISATION' in entities_ner:
    symptom_grammar = symptom_grammar + "B6 -> A6 '" + symptom_obj['localisation'] + "' [1.0] | [0.0]\n"
  else:
    symptom_grammar = symptom_grammar + "B6 -> A6 '" + "none" + "' [0.0] | [1.0]\n"

  if 'EVOLUTION' in entities_ner:
    symptom_grammar = symptom_grammar + "B7 -> A7 '" + symptom_obj['evolution'] + "' [1.0] | [0.0]\n"
  else:
    symptom_grammar = symptom_grammar + "B7 -> A7 '" + "none" + "' [0.0] | [1.0]\n"

  grammar = PCFG.fromstring(symptom_grammar)  # we construct the grammar

  S = grammar.start() # axiom of the grammar
  word = get_word(grammar=grammar, non_terminal=S) # parses grammar through left-most derivation to create the word
  return remove_spaces(word)

similar('smoke', 'smoking')
max_similar(['Cigarette', 'Tramol', 'Marijuana', 'Canabis', 'Medecine', 'Smoke'], 'mari')

def lifestyle_phrase_grammar(entities_ner, life_obj):
  """
    We create a grammar with varying probabilities considering the entities present in entities_ner
  """

  if 'MOSQUITO NET' in entities_ner:
    if life_obj['mosquito'] == True:
      return 'Yes Doctor, I sleep under a mosquito net', True
    else:
      return "No Doctor, I don't sleep under a mosquito net", True
  
  elif 'PET' in entities_ner:
    if life_obj['pet_company'] == "":
      return "No Doctor, I don't have any pet", False
    else:
      pets = life_obj['pet_company'].replace(';', ', ')
      return "I have a " + pets, True
  
  elif 'WATER' in entities_ner:
    return 'I usually drink ' + life_obj['water_quality'], True
  
  elif 'ALCOHOL' in entities_ner:
    gram = """
      S -> A1 A2 A3 [1.0]

      A1 -> 'Yes doctor, I consume alcohol' [0.25] | 'I drink alcohol' [0.25] | 'I usually drink alcohol' [0.25] | 'I take acohol, doctor' [0.25]

      B2 -> 'about' [0.25] | 'for about' [0.25] | 'around' [0.25] | 'nearly' [0.25]
      B3 -> 'since' [0.2] | 'for the past' [0.2] | 'for' [0.2] | 'for nearly' [0.2] | 'for about' [0.2]
    """
    alcohol = None
    for life in life_obj['addiction']:
      if life['name'] in ['Alcohol', 'Beer']:
        alcohol = life
        break
    if alcohol == None:
      return "No doctor, I don't consume any alcohol", False
    
    if 'FREQUENCY' in entities_ner:
      gram = gram + "A2 -> B2 '" + alcohol['frequency'] + "' [1.0] | [0.0]\n"
    else:
      gram = gram + "A2 -> B2 '" + "none" + "' [0.0] | [1.0]\n"

    if 'DURATION' in entities_ner:
      gram = gram + "A3 -> B3 '" + alcohol['duration'] + "' [1.0] | [0.0]\n"
    else:
      gram = gram + "A3 -> B3 '" + "none" + "' [0.0] | [1.0]\n"
    
    grammar = PCFG.fromstring(gram)  # we construct the grammar

    S = grammar.start() # axiom of the grammar
    word = get_word(grammar=grammar, non_terminal=S) # parses grammar through left-most derivation to create the word
    return word, True
  
  
  elif 'DRUG' in entities_ner:
    gram = """
      S -> A1 A2 A3 [1.0]

      B1 -> 'Yes doctor, I consume' [0.25] | 'I take' [0.25] | 'I smoke' [0.25] | 'I usually consume' [0.25]
      B2 -> 'about' [0.25] | 'for about' [0.25] | 'around' [0.25] | 'nearly' [0.25]
      B3 -> 'since' [0.2] | 'for the past' [0.2] | 'for' [0.2] | 'for nearly' [0.2] | 'for about' [0.2]
    """
    drugs = []
    for life in life_obj['addiction']:
      if life['name'] in ['Cigarette', 'Tramol', 'Marijuana', 'Canabis', 'Medecine',]:
        drugs.append(life)

    if len(drugs) == 0:
      return "No doctor, I don't smoke anything.", False
    
    drug = None
    drug_name = max_similar(['Cigarette', 'Tramol', 'Marijuana', 'Canabis', 'Medecine', 'Smoke'], entities_ner['DRUG'])
    if drug_name == 'Smoke':
      all_drugs = ""
      for dr in drugs:
        all_drugs = all_drugs + dr['name'] + ", "
      return 'Yes doctor, I consume ' + all_drugs, True
    
    else:
      for dr in drugs:
        if dr['name'] == drug_name:
          drug = dr
          break

    if drugs == None:
      return "I don't smoke " + drug_name + " doctor", False
    
    gram = gram + "A1 -> B1 '" + drug['name'] + "' [1.0] | [0.0]\n"
    if 'FREQUENCY' in entities_ner:
      gram = gram + "A2 -> B2 '" + drug['frequency'] + "' [1.0] | [0.0]\n"
    else:
      gram = gram + "A2 -> B2 '" + "none" + "' [0.0] | [1.0]\n"

    if 'DURATION' in entities_ner:
      gram = gram + "A3 -> B3 '" + drug['duration'] + "' [1.0] | [0.0]\n"
    else:
      gram = gram + "A3 -> B3 '" + "none" + "' [0.0] | [1.0]\n"
    
    grammar = PCFG.fromstring(gram)  # we construct the grammar

    S = grammar.start() # axiom of the grammar
    word = get_word(grammar=grammar, non_terminal=S) # parses grammar through left-most derivation to create the word
    return word, True
  
  elif 'SPORT' in entities_ner:
    sports = life_obj['physical_activity']
    if len(sports) == 0:
      return "I don't do any sport of physical activity, doctor", False
    all_sports = ""
    for sp in sports:
      all_sports = all_sports + sp['name'] + " about " + sp['frequency'] + ", "
    return "I play " + all_sports, True
  
  elif 'TRAVEL' in entities_ner:
    gram = """
      S -> A1 A2 A3 [1.0]

      B1 -> 'Yes doctor, I traveled to' [0.25] | 'I traveled to' [0.25] | 'I made a trip to' [0.25] | 'I went to' [0.25]
      B2 -> 'about' [0.25] | 'for about' [0.25] | 'around' [0.25] | 'nearly' [0.25]
      B3 -> 'since' [0.5] | 'about' [0.5]
    """
    travels = life_obj['travel']
    
    if len(travels) == 0:
      return "No doctor, I didn't travel recently", False
    
    travel = travels[0]
    gram = gram + "A1 -> B1 '" + travel['location'] + "' [1.0] | [0.0]\n"
    if 'FREQUENCY' in entities_ner:
      gram = gram + "A2 -> B2 '" + travel['frequency'] + "' [1.0] | [0.0]\n"
    else:
      gram = gram + "A2 -> B2 '" + "none" + "' [0.0] | [1.0]\n"

    if 'DURATION' in entities_ner:
      gram = gram + "A3 -> B3 '" + travel['duration'] + " ago.' [1.0] | [0.0]\n"
    else:
      gram = gram + "A3 -> B3 '" + "none" + "' [0.0] | [1.0]\n"
    
    grammar = PCFG.fromstring(gram)  # we construct the grammar

    S = grammar.start() # axiom of the grammar
    word = get_word(grammar=grammar, non_terminal=S) # parses grammar through left-most derivation to create the word
    return word, True

def antecedent_phrase_grammar(entities_ner, antecedent_obj):
  """
    We create a grammar with varying probabilities considering the entities present in entities_ner
  """

  if 'ANTECEDENT' in entities_ner:
    if antecedent_obj['family_antecedents']:
      return 'Yes Doctor, my family history includes ' + antecedent_obj['family_antecedents'], True
    else:
      return "No Doctor, I don't have family history", False
  
  elif 'PREGNANCY' in entities_ner:
    if len(antecedent_obj['obstetrical_antecedent']) == 0:
      return "No Doctor, I don't have obstetrical antecedent", False
    else:
      return "I already had " + antecedent_obj['obstetrical_antecedent'][0]['nb_pregnancy'] + " grossesse(s) " + "and the last one was the " + antecedent_obj['obstetrical_antecedent'][0]['date_of_last_pregnancy'], True
  
  elif 'ALLERGY' in entities_ner:
    gram = """
      S -> A1 A2 [1.0]

      A1 -> 'Yes doctor,' [1.0]
      B1 -> 'it manifests itself by' [0.5] | 'it manifested itself by' [0.5]
    """
    allergies = {}
    manifestations = []
    triggers = []

    for allergy in antecedent_obj['allergy']:
      manifestations.append(allergy['manifestation'])
      if allergy['trigger']:
        triggers.append(allergy['manifestation'] + " which is triggered by " + allergy['trigger'])
      else:
        triggers.append(allergy['manifestation'] + " I don't know the trigger activity")
    
    allergies["manifestation"] = ", ".join(manifestations)
    allergies["trigger"] = ", ".join(triggers)

    if 'TRIGGER' in entities_ner:
      gram = gram + "A2 -> B1 '" + allergies['trigger'] + "' [1.0] | [0.0]\n"
    else:
      if allergies['manifestation']:
        gram = gram + "A2 -> B1 '" + allergies['manifestation'] + "' [1.0] | [0.0]\n"
      else:
        return "No doctor, I don't have any allergy", False
    
    grammar = PCFG.fromstring(gram)  # we construct the grammar

    S = grammar.start() # axiom of the grammar
    word = get_word(grammar=grammar, non_terminal=S) # parses grammar through left-most derivation to create the word
    return word, True
  
  elif 'SURGERY' in entities_ner:
    gram = """
      S -> A1 A2 [1.0]

      A1 -> 'Yes doctor,' [1.0]
      B1 -> 'I have done' [0.3333] | 'I did' [0.3333] | "I've done" [0.3333]
    """
    surgeries = []

    for surg in antecedent_obj['surgery']:
      if surg['date']:
        surgeries.append(surg['name'] + " on the " + datetime.strptime(surg['date'], '%Y-%m-%d').date().strftime('%B %Y'))
      else:
        surgeries.append(surg['name'] + " i don't remember the date")
    
    surgery = ", ".join(surgeries)

    if surgery :
      gram = gram + "A2 -> B1 '" + surgery + "' [1.0] | [0.0]\n"
    else:
      word = "No doctor, I did not do any surgery."
    
    grammar = PCFG.fromstring(gram)  # we construct the grammar

    S = grammar.start() # axiom of the grammar
    word = get_word(grammar=grammar, non_terminal=S) # parses grammar through left-most derivation to create the word
    return word

def generate_text(category, clinical_case=None, response=None, symptom_entities = None, life_style_entities = None, antecedent_entities = None):
  # clinical_case = get_clinical_case('ae538715-2b8a-4680-bfb8-a4ccebf4b988')
  if category == 'salutation':
    return 'Good ' + getPeriod() + ' Doctor', True
  elif category == 'initial_problem':
    return "I don't feel well doctor. " + clinical_case['initial_problem'], True
  elif category == 'repetition':
    return 'repetition', True
  elif category == 'life_style':
    if life_style_entities != None:
      return lifestyle_phrase_grammar(entities_ner=life_style_entities, life_obj=clinical_case['life_style'][0])
    return
  elif category == 'antecedent':
    if antecedent_entities != None:
      return antecedent_phrase_grammar(entities_ner=antecedent_entities, antecedent_obj=clinical_case['medical_antecedent'][0])
    return
  elif category == 'symptoms':
    if symptom_entities != None:
      symptoms = getSymptoms(clinical_case, symptom_entities['SYMPTOM'])
      if symptoms == None:
        return "No doctor, I don't have " + symptom_entities['SYMPTOM'], symptom_entities['SYMPTOM'], False
      else:
        return symptom_phrase_grammar(entities_ner=symptom_entities, symptom_obj=symptoms), symptom_entities['SYMPTOM'], True
    return

@api_view(['POST'])
def response(request):
  body = json.loads(request.body)

  text = body["question"]
  id = body["clinical_case"]

  symp = None
  

  clinical_case = clinicalCase(request=request, id_clinical_case=id)

  cl = classifyText(text)

  print(cl)
  if cl == "Symptoms":
    if text in ["Hello", "hello"]:
      res = "False classification :-("
    else:
      symptom_entities = getkeySymptom(text)["data"]
      res, symp, in_case = generate_text('symptoms', clinical_case=clinical_case[0], symptom_entities=symptom_entities)
  elif cl == "Life Style":
    life_style_entities = getkeyLifeStyle(text)["data"]
    res, in_case = generate_text('life_style', clinical_case=clinical_case[0], life_style_entities=life_style_entities)
  elif cl == "Antecedent":
    antecedent_entities = getkeyAntecedent(text)["data"]
    res, in_case = generate_text('antecedent', clinical_case=clinical_case[0], antecedent_entities=antecedent_entities)
  elif cl == "Salutation":
    res, in_case = generate_text('salutation')
  elif cl == "Initial Problem":
    res, in_case = generate_text('initial_problem', clinical_case=clinical_case[0])
  elif cl == "Repetition":
    if "response" in body:
      resp = body["response"]
      if resp:
        res, in_case = generate_text('repetition',response=resp)
      else:
        result = {
          "status": False,
          "message": "The field response not be empty"
        }
        return Response(result, status = status.HTTP_404_NOT_FOUND)
    else:
      result = {
        "status": False,
        "message": "No field response"
      }
      return Response(result, status = status.HTTP_404_NOT_FOUND)

  result = {
    "status": in_case,
    "response": res,
    "class": cl,
    "symptom": symp if symp else None
  }
  return Response(result, status.HTTP_200_OK)

def checkDifficulty(rate):
  if 0 <= rate <= 0.4:
    return "EASY"
  elif 0.5 <= rate <= 0.7:
    return "MEDIUM"
  else:
    return "HARD"

@api_view(["POST"])
def chooseClinicalCase(request):
  body = json.loads(request.body)
  context = {
        'request': request,
    }

  if body == None:
    result = {
      "status": "FAILURE",
      "message": "random, learner, system required"
    }
    return Response(result, status.HTTP_204_NO_CONTENT)
  if 'random' not in body:
    result = {
      "status": "FAILURE",
      "message": "random required"
    }
    return Response(result, status.HTTP_204_NO_CONTENT)
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
  
  system_name = ""
  systems, diseases, details = getRating(request=request, pk=body["leaner"])

  if body["random"]:
    for key in systems:
      if systems[key] == 0.00:
        system_name = key
        break
  return 0

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
    return JsonResponse(result, status=status.HTTP_200_OK)


def root(request):
    return redirect('/api')