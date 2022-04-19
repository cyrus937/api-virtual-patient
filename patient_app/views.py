from django.shortcuts import render
import random
from datetime import datetime, timedelta
from uuid import uuid4

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

from django.contrib.auth.models import User
from .models import *
from .serializers import *

# Create your views here.
class MedecinViewSet(viewsets.ModelViewSet):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer

class MedecinApprenantViewSet(viewsets.ModelViewSet):
    queryset = MedecinApprenant.objects.all()
    serializer_class = MedecinApprenantSerializer

class MedecinExpertViewSet(viewsets.ModelViewSet):
    queryset = MedecinExpert.objects.all()
    serializer_class = MedecinExpertSerializer

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class PatientVirtuelViewSet(viewsets.ModelViewSet):
    queryset = PatientVirtuel.objects.all()
    serializer_class = PatientVirtuelSerializer

class CasCliniqueViewSet(viewsets.ModelViewSet):
    queryset = CasClinique.objects.all()
    serializer_class = CasCliniqueSerializer

class CasVirtuelViewSet(viewsets.ModelViewSet):
    queryset = CasVirtuel.objects.all()
    serializer_class = CasVirtuelSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

class HypotheseViewSet(viewsets.ModelViewSet):
    queryset = Hypothese.objects.all()
    serializer_class = HypotheseSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class InfosPersonnellesViewSet(viewsets.ModelViewSet):
    queryset = InfosPersonnelles.objects.all()
    serializer_class = InfosPersonnellesSerializer

class TraitementEnCoursViewSet(viewsets.ModelViewSet):
    queryset = TraitementEnCours.objects.all()
    serializer_class = TraitementEnCoursSerializer

class DiagnosticPhysiqueViewSet(viewsets.ModelViewSet):
    queryset = DiagnosticPhysique.objects.all()
    serializer_class = DiagnosticPhysiqueSerializer

class ExamenViewSet(viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

class ExamenPhysiqueViewSet(viewsets.ModelViewSet):
    queryset = ExamenPhysique.objects.all()
    serializer_class = ExamenPhysiqueSerializer

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class TypeParametreViewSet(viewsets.ModelViewSet):
    queryset = TypeParametre.objects.all()
    serializer_class = TypeParametreSerializer

class ParametreMedicalViewSet(viewsets.ModelViewSet):
    queryset = ParametreMedical.objects.all()
    serializer_class = ParametreMedicalSerializer

class ModeVieViewSet(viewsets.ModelViewSet):
    queryset = ModeVie.objects.all()
    serializer_class = ModeVieSerializer

class ActivitePhysiqueViewSet(viewsets.ModelViewSet):
    queryset = ActivitePhysique.objects.all()
    serializer_class = ActivitePhysiqueSerializer

class AddictionViewSet(viewsets.ModelViewSet):
    queryset = Addiction.objects.all()
    serializer_class = AddictionSerializer

class VoyageViewSet(viewsets.ModelViewSet):
    queryset = Voyage.objects.all()
    serializer_class = VoyageSerializer

class SymptomeViewSet(viewsets.ModelViewSet):
    queryset = Symptome.objects.all()
    serializer_class = SymptomeSerializer

class DescriptionSymptomeViewSet(viewsets.ModelViewSet):
    queryset = DescriptionSymptome.objects.all()
    serializer_class = DescriptionSymptomeSerializer

class ConceptViewSet(viewsets.ModelViewSet):
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer

class AntecedentMedicalViewSet(viewsets.ModelViewSet):
    queryset = AntecedentMedical.objects.all()
    serializer_class = AntecedentMedicalSerializer

class AntecedentObstetricalViewSet(viewsets.ModelViewSet):
    queryset = AntecedentObstetrical.objects.all()
    serializer_class = AntecedentObstetricalSerializer

class ChirurgieViewSet(viewsets.ModelViewSet):
    queryset = Chirurgie.objects.all()
    serializer_class = ChirurgieSerializer

class AllergieViewSet(viewsets.ModelViewSet):
    queryset = Allergie.objects.all()
    serializer_class = AllergieSerializer

class TraitementViewSet(viewsets.ModelViewSet):
    queryset = Traitement.objects.all()
    serializer_class = TraitementSerializer

class MaladieViewSet(viewsets.ModelViewSet):
    queryset = Maladie.objects.all()
    serializer_class = MaladieSerializer