from django.urls import path, include, re_path
#from django.conf.urls import url
from rest_framework import routers

from . import views

routers = routers.DefaultRouter()
routers.register(r'doctor', views.MedecinViewSet)
routers.register(r'doctor-apprenant', views.MedecinApprenantViewSet)
routers.register(r'doctor-expert', views.MedecinExpertViewSet)
routers.register(r'log', views.LogViewSet)
routers.register(r'patient-virtuel', views.PatientVirtuelViewSet)
routers.register(r'cas-clinique', views.CasCliniqueViewSet)
routers.register(r'cas-virtuel', views.CasVirtuelViewSet)
routers.register(r'feedback', views.FeedbackViewSet)
routers.register(r'evaluation', views.EvaluationViewSet)
routers.register(r'hypothese', views.HypotheseViewSet)
routers.register(r'question', views.QuestionViewSet)
routers.register(r'information-personnelle', views.InfosPersonnellesViewSet)
routers.register(r'treatment-en-cours', views.TraitementEnCoursViewSet)
routers.register(r'diagnostic-physique', views.DiagnosticPhysiqueViewSet)
routers.register(r'exam', views.ExamenViewSet)
routers.register(r'exam-physique', views.ExamenPhysiqueViewSet)
routers.register(r'media', views.MediaViewSet)
routers.register(r'type-parametre', views.TypeParametreViewSet)
routers.register(r'parametre-medical', views.ParametreMedicalViewSet)
routers.register(r'symptom', views.SymptomeViewSet)
routers.register(r'description-symptom', views.DescriptionSymptomeViewSet)
routers.register(r'mode-vie', views.ModeVieViewSet)
routers.register(r'activite-physique', views.ActivitePhysiqueViewSet)
routers.register(r'addiction', views.AddictionViewSet)
routers.register(r'voyage', views.VoyageViewSet)
routers.register(r'concept', views.ConceptViewSet)
routers.register(r'antecedent-medical', views.AntecedentMedicalViewSet)
routers.register(r'antecedent-obstetrical', views.AntecedentObstetricalViewSet)
routers.register(r'chirurgie', views.ChirurgieViewSet)
routers.register(r'allergie', views.AllergieViewSet)
routers.register(r'treatment', views.TraitementViewSet)
routers.register(r'maladie', views.MaladieViewSet)

urlpatterns = [
    path('', include(routers.urls)),


    re_path(r'^[a-zA-Z0-9/,;:!\\*-+^$ù&é(-è_çà)]+/$', views.errorPage),
    
]