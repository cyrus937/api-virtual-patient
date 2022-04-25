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
# Importation du dataset
bn=gum.loadBN("virtual_patient_api\media\Bayesian_network.bif")
""" data = pd.read_csv("virtual_patient_api\media\dataset.csv")

# Suppression des espaces
data['Disease'] = data['Disease'].replace([' '], '_', regex=True)

disease_weights = {
  'Malaria': 10,
  '(vertigo)_Paroymsal__Positional_Vertigo': 2,
  'AIDS': 7,
  'Acne': 2,
  'Alcoholic_hepatitis': 5,
  'Allergy': 6,
  'Arthritis': 4,
  'Bronchial_Asthma': 8,
  'Cervical_spondylosis': 3,
  'Chicken_pox': 4,
  'Chronic_cholestasis': 3,
  'Common_Cold': 10,
  'Dengue': 1,
  'Diabetes_': 8,
  'Dimorphic_hemmorhoids(piles)': 5,
  'Drug_Reaction': 4,
  'Fungal_infection': 7,
  'GERD': 3,
  'Gastroenteritis': 6,
  'Heart_attack': 8,
  'Hepatitis_B': 6,
  'Hepatitis_C': 7,
  'Hepatitis_D': 4,
  'Hepatitis_E': 3,
  'Hypertension_': 8,
  'Hyperthyroidism': 6,
  'Hypoglycemia': 6,
  'Hypothyroidism': 5,
  'Impetigo': 2,
  'Jaundice': 3,
  'Migraine': 8,
  'Osteoarthristis': 5,
  'Paralysis_(brain_hemorrhage)': 5,
  'Peptic_ulcer_diseae': 4,
  'Pneumonia': 7,
  'Psoriasis': 1,
  'Tuberculosis': 7,
  'Typhoid': 9,
  'Urinary_tract_infection': 6,
  'Varicose_veins': 1,
  'hepatitis_A': 5
} """

#bn=gum.BayesNet('Disease Network')

list_diseases = ['Malaria', 'Tuberculosis', 'Diabetes_', 'Typhoid', 'hepatitis_A', 'Hepatitis_B', 'Hypoglycemia', 'Common_Cold', 'Chicken_pox', 'Pneumonia']

def select_diseases(data):
  diseases = {}
  print(list_diseases)
  for dis in list_diseases:
    diseases[dis] = data[data['Disease'] == dis]
  print("--> Filtrage du dataframe par maladie") #filtrer le dataframe par maladie
  
  return diseases

def get_symptoms(disease):
  """
    disease: type dataframe;
    description: permet de récupérer l'ensemble des symptomes d'une maladie (disease).
    return: [] liste des symptômes.
  """
  symptoms = []
  columns = list(disease.drop(columns=['Disease', 'weight']).columns)
  for column in columns:
    symptoms.extend(list(disease[column].dropna().unique()))
  symptoms = list(set(symptoms))
  return symptoms

#########################################################

def get_symp_frequency_disease(disease):
  """
    disease: type dataframe;
    description: permet de calculer la fréquence des symptomes dans une maladie (disease).
    return: un dictionnaire avec clé=symtômes et valeur=fréquence.
  """
  sum = 0
  freqs = {}
  columns = list(disease.drop(columns=['Disease', 'weight']).columns)
  symptoms = get_symptoms(disease)

  for symp in symptoms:
    for col in columns:
      sum += (disease[col].values == symp).sum()
    freqs[symp] = sum
    sum = 0
  
  return freqs

#########################################################

def get_symp_sum_weight(data):
  """
    description: permet de calculer la somme des poids d'un symptome dans le dataset.
    return: un dictionnaire avec clé=symtômes et valeur=somme.
  """
  freqs = {}
  symptoms = get_symptoms(data)

  for symp in symptoms:
    filter_symp = data.apply(lambda row: row.astype(str).str.contains(symp.replace(' ', '')).any(), axis=1) # rechercher le symptomes sur la ligne; filter_symp : series
    filter_symp = data[filter_symp]

    freqs[symp] = filter_symp['weight'].sum()
  
  return freqs

#########################################################


def frequencies_to_probabilities(disease):
  """
    disease: type dataframe;
    description: permet de calculer la probabilité des symptomes dans une maladie (disease).
    return: un dictionnaire avec clé=symtômes et valeur=probabilité.
  """
  frequencies = get_symp_frequency_disease(disease) #dict
  length = len(disease)
  result = {}

  for key in frequencies:
    result[key] = frequencies[key] / length
  
  return result

#########################################################

def truthtable (n):
  """
    n: type entier;
    description: permet de créer une table de vérité de taille n.
    return: un tableau 2D: ex [[0,0], [0,1], [1,0], [1,1]] avec n=2
  """
  if n < 1:
    return [[]]
  subtable = truthtable(n-1)

  return [ row + [v] for row in subtable for v in [0,1] ]

#########################################################

def list_to_dict(key_list, values):
  """
    key_list: type list: contient les clés du dictionnaire à créer; values: les valeurs du dictionnaire à créer
    description: permet de convertir une liste en dictionnaire
    return: un dictionnaire
  """
  result = {}
  for i in range(0, len(key_list)):
    result[key_list[i]] = values[i]
  
  return result

#########################################################

def probability_generator(node, dataframes):
  #global bn
  """
    node: un node du réseau bayésien, plus precisement les maladies.
    result: retourne un tuple contenant un objet et une liste de probabilité
  """
  vars = bn.cpt(node).var_names #ex: vars = [' congestion', ' runny_nose', ' cough', 'Common_Cold']
  disease = vars.pop() #ex: 'Common_Cold'

  table = truthtable(len(vars)) # génère la table de vérité selon la nombre symptomes d'une maladie

  final_result = []
  symtom_prob_in_disease = frequencies_to_probabilities(dataframes[disease]) # calculer la probabilité d'apparution d'un symptomes dans une maladie

  for tab in table:
    # pour n=4 : tab = [0,0,0,0] à la première itération
    obj = list_to_dict(vars, tab)
    # obj = {' congestion': 0, ' runny_nose': 0, ' cough': 0} à la première itération
    probabilities = []

    p = 0
    num = 0
    for key in obj:
      if obj[key] == 1:
        p += symtom_prob_in_disease[key]
      
      num += symtom_prob_in_disease[key]

    if num > 0:
      p = p/num
    probabilities.append(1 - p)
    probabilities.append(p)
    
    final_result.append((obj, probabilities))
  
  return final_result

def set_probability_tables(node, probabilities):
  global bn
  """
    node: noeud dans le réseau; probabilities: liste de tuple qui provient de 'probability_generator'
    description: insère les valeurs dans les tables de probabilités conditionnels
  """
  for item in probabilities:
    bn.cpt(node)[item[0]] = item[1]

""" def infere_network(node, evidence):
  ie=gum.LazyPropagation(bn)

  ie.setEvidence(evidence)
  ie.makeInference()
  return ie.posterior(node) """

@api_view(['PUT', 'POST'])
def createreseaubayesien(request):
    if request.method in ['PUT', 'POST']:
        file_ = request.Files['file']

        # Importation du dataset
        data = pd.read_csv(file_)
        print("--> importation du dataset")

        # Suppression des espaces
        data['Disease'] = data['Disease'].replace([' '], '_', regex=True)
        print("--> Suppression des espaces")
        
        disease_weights = {
            'Malaria': 10,
            '(vertigo)_Paroymsal__Positional_Vertigo': 2,
            'AIDS': 7,
            'Acne': 2,
            'Alcoholic_hepatitis': 5,
            'Allergy': 6,
            'Arthritis': 4,
            'Bronchial_Asthma': 8,
            'Cervical_spondylosis': 3,
            'Chicken_pox': 4,
            'Chronic_cholestasis': 3,
            'Common_Cold': 10,
            'Dengue': 1,
            'Diabetes_': 8,
            'Dimorphic_hemmorhoids(piles)': 5,
            'Drug_Reaction': 4,
            'Fungal_infection': 7,
            'GERD': 3,
            'Gastroenteritis': 6,
            'Heart_attack': 8,
            'Hepatitis_B': 6,
            'Hepatitis_C': 7,
            'Hepatitis_D': 4,
            'Hepatitis_E': 3,
            'Hypertension_': 8,
            'Hyperthyroidism': 6,
            'Hypoglycemia': 6,
            'Hypothyroidism': 5,
            'Impetigo': 2,
            'Jaundice': 3,
            'Migraine': 8,
            'Osteoarthristis': 5,
            'Paralysis_(brain_hemorrhage)': 5,
            'Peptic_ulcer_diseae': 4,
            'Pneumonia': 7,
            'Psoriasis': 1,
            'Tuberculosis': 7,
            'Typhoid': 9,
            'Urinary_tract_infection': 6,
            'Varicose_veins': 1,
            'hepatitis_A': 5
            }
        
        weight_column = []
        for dis in data['Disease']:
            weight_column.append(disease_weights[dis])

        # Ajouter la colonne des poids dans le dataframe
        data['weight'] = weight_column

        dataframes = select_diseases(data)
        print("--> Selection des maladies")

        # dictionnaire qui contient les noeuds du réseau
        disease_nodes = {}
        symptoms_nodes = {}

        # Ajouter les maladies choisi
        print("--> Ajout des maladies dans le réseau bayésien")
        for dis in list_diseases:
            node = gum.LabelizedVariable(dis, dis, 2)
            node.changeLabel(0, 'F')
            node.changeLabel(1, 'V')
            disease_nodes[dis] = bn.add(node)


        # Ajouter les symptomes liés aux maladies choisi
        print("--> Obtention des symptômes")
        list_sypm = []
        for dis in list_diseases:
            list_sypm.extend(get_symptoms(dataframes[dis]))

        print("--> Extraction des possibles duplication de symptomes dans la liste")
        list_sypm = list(set(list_sypm)) # retirer les possibles duplication de symptomes dans la liste

        print("--> Ajout des symptômes liés aux maladies choisies dans le réseau bayésien")
        for symp in list_sypm:
            node = gum.LabelizedVariable(symp, symp, 2)
            node.changeLabel(0, 'F')
            node.changeLabel(1, 'V')
            symptoms_nodes[symp] = bn.add(node)
        
        print("--> Création des arcs et connexion des noeuds du réseaux")
        for key in disease_nodes:
            for symp in get_symptoms(dataframes[key]):
                bn.addArc(symptoms_nodes[symp], disease_nodes[key]) # ex: A -> B
        
        print("--> création des tables de probabilité initiaux du graphe")
        # Pour remplir les tableaux initiaux des noeuds du graphe, on se base sur les données du dataset
        # On détermine le nombre d'occurence de chaque symptomes dans tout le dataset et l'on divise par le nombre total de donnée

        size = len(data) # somme total des poids
        symps_prob = get_symp_frequency_disease(data) # fréquence des symptômes dans tous le dataset

        # symps_prob = {k: v for k, v in sorted(symps.items(), key=lambda item: item[1], reverse=True)} #trier le dict

        for key in symps_prob:
          symps_prob[key] = (symps_prob[key] / size) + 0.3
        
        print("--> création des tables de probabilité conditionnelle")
        for key in symptoms_nodes:
          bn.cpt(symptoms_nodes[key]).fillWith([1-symps_prob[key], symps_prob[key]])
        
        for key in disease_nodes:
          prob_items=probability_generator(disease_nodes[key])
          set_probability_tables(disease_nodes[key], prob_items)

    return "null"

def infere_network(disease, symptoms):
  global bn
  ie=gum.LazyPropagation(bn)

  ie.setEvidence(symptoms)
  ie.makeInference()
  return ie.posterior(disease)

def Convert(tup, di):
  for a, b in tup: 
    #di.setdefault(a, []).append(b) 
    di[a] = b
  #di = dict(tup)
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
    #disease = body['disease']
    symptoms = body['symptoms']

    #for s in symptoms:
    #  symp[s] = 1
    
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