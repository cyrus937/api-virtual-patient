from django.urls import path, include, re_path
#from django.conf.urls import url
from rest_framework import routers

from . import views

routers = routers.DefaultRouter()
routers.register(r'doctor', views.MedecinViewSet)
routers.register(r'doctor-apprenant', views.MedecinApprenantViewSet)
routers.register(r'doctor-expert', views.MedecinExpertViewSet)
routers.register(r'log', views.LogViewSet)
routers.register(r'virtuel-patient', views.PatientVirtuelViewSet)
routers.register(r'clinical-case', views.CasCliniqueViewSet)
routers.register(r'virtual-case', views.CasVirtuelViewSet)
routers.register(r'feedback', views.FeedbackViewSet)
routers.register(r'evaluation', views.EvaluationViewSet)
routers.register(r'hypothesis', views.HypotheseViewSet)
routers.register(r'question', views.QuestionViewSet)
routers.register(r'personnal-information', views.InfosPersonnellesViewSet)
routers.register(r'ongoing-treatment', views.TraitementEnCoursViewSet)
routers.register(r'physical-diagnostic', views.DiagnosticPhysiqueViewSet)
routers.register(r'exam', views.ExamenViewSet)
routers.register(r'physical-exam', views.ExamenPhysiqueViewSet)
routers.register(r'media', views.MediaViewSet)
routers.register(r'type-parametre', views.TypeParametreViewSet)
routers.register(r'medical-parameter', views.ParametreMedicalViewSet)
routers.register(r'symptom', views.SymptomeViewSet)
routers.register(r'description-symptom', views.DescriptionSymptomeViewSet)
routers.register(r'life-style', views.ModeVieViewSet)
routers.register(r'physical-activity', views.ActivitePhysiqueViewSet)
routers.register(r'addiction', views.AddictionViewSet)
routers.register(r'travel', views.VoyageViewSet)
routers.register(r'concept', views.ConceptViewSet)
routers.register(r'medical-antecedent', views.AntecedentMedicalViewSet)
routers.register(r'obstetrical-antecedent', views.AntecedentObstetricalViewSet)
routers.register(r'surgery', views.ChirurgieViewSet)
routers.register(r'allergy', views.AllergieViewSet)
routers.register(r'treatment', views.TraitementViewSet)
routers.register(r'disease', views.MaladieViewSet)

urlpatterns = [
    path('', include(routers.urls)),


    re_path(r'^[a-zA-Z0-9/,;:!\\*-+^$ù&é(-è_çà)]+/$', views.errorPage),
    
]