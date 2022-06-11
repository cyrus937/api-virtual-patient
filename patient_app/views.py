from django.shortcuts import redirect
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User

from .models import *
from .serializers import *

# Create your views here.

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, YourCustomType):
            return str(obj)
        return super().default(obj)

class RegistrationAPIView(generics.GenericAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        
        if(serializer.is_valid()):
            self.perform_create(serializer)
            user = User.objects.create(
                username = serializer.data["username"],
                first_name = serializer.data["firts_name"],
                last_name = serializer.data["name"],
                email = serializer.data["email"],
            )
            user.set_password(serializer.data["password"])
            user.save()
            user = DoctorViewSet()
            return Response({
                "status":True,
                "RequestId": str(uuid.uuid4()),
                "Message": "Doctor created successfully",
                "User":serializer.data}, status=status.HTTP_201_CREATED
                )
        print(serializer.errors )
        
        return Response({"status":False,"Errors":serializer.errors}, status.HTTP_400_BAD_REQUEST)

class CutomObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainSerializer

class DoctorViewSet(viewsets.ModelViewSet):
  queryset = Doctor.objects.all()
  serializer_class = DoctorSerializer

  def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data = request.data)
        
        print(serializer.is_valid())
        if(serializer.is_valid()):
            self.perform_create(serializer)
            user = User.objects.create(
                username = serializer.data["username"],
                first_name = serializer.data["first_name"],
                last_name = serializer.data["name"],
                email = serializer.data["email"],
            )
            user.set_password(serializer.data["password"])
            user.save()
            return Response({
                "status":True,
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                "User":serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"status":False,"Errors":serializer.errors}, status.HTTP_400_BAD_REQUEST)

class LeanerPhysicianViewSet(viewsets.ModelViewSet):
  queryset = LeanerPhysician.objects.all()
  serializer_class = LeanerPhysicianSerializer

  def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data = request.data)
        
        print(serializer.is_valid())
        if(serializer.is_valid()):
            self.perform_create(serializer)
            user = User.objects.create(
                username = serializer.data["username"],
                first_name = serializer.data["first_name"],
                last_name = serializer.data["name"],
                email = serializer.data["email"],
            )
            user.set_password(serializer.data["password"])
            user.save()
            return Response({
                "status":True,
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                "User":serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"status":False,"Errors":serializer.errors}, status.HTTP_400_BAD_REQUEST)

class ExpertPhysicianViewSet(viewsets.ModelViewSet):
  queryset = ExpertPhysician.objects.all()
  serializer_class = ExpertPhysicianSerializer

  def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data = request.data)
        
        print(serializer.is_valid())
        if(serializer.is_valid()):
            self.perform_create(serializer)
            user = User.objects.create(
                username = serializer.data["username"],
                first_name = serializer.data["first_name"],
                last_name = serializer.data["name"],
                email = serializer.data["email"],
            )
            user.set_password(serializer.data["password"])
            user.save()
            return Response({
                "status":True,
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                "User":serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"status":False,"Errors":serializer.errors}, status.HTTP_400_BAD_REQUEST)

class LogViewSet(viewsets.ModelViewSet):
  queryset = Log.objects.all()
  serializer_class = LogSerializer

class VirtualPatientViewSet(viewsets.ModelViewSet):
  queryset = VirtualPatient.objects.all()
  serializer_class = VirtualPatientSerializer

class ClinicalCaseViewSet(viewsets.ModelViewSet):
  queryset = ClinicalCase.objects.all()
  serializer_class = ClinicalCaseSerializer

class VirtualCaseViewSet(viewsets.ModelViewSet):
  queryset = VirtualCase.objects.all()
  serializer_class = VirtualCaseSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
  queryset = Feedback.objects.all()
  serializer_class = FeedbackSerializer

class EvaluationViewSet(viewsets.ModelViewSet):
  queryset = Evaluation.objects.all()
  serializer_class = EvaluationSerializer

class HypothesisViewSet(viewsets.ModelViewSet):
  queryset = Hypothesis.objects.all()
  serializer_class = HypothesisSerializer

class QuestionViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer

class PersonalInfoViewSet(viewsets.ModelViewSet):
  queryset = PersonalInfo.objects.all()
  serializer_class = PersonalInfoSerializer

class TreatmentInProgressViewSet(viewsets.ModelViewSet):
  queryset = TreatmentInProgress.objects.all()
  serializer_class = TreatmentInProgressSerializer

class MediaViewSet(viewsets.ModelViewSet):
  queryset = Media.objects.all()
  serializer_class = MediaSerializer
  filter_backends = [OrderingFilter]
  search_fields = ['type']
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['type']

class PhysicalDiagnosisViewSet(viewsets.ModelViewSet):
  queryset = PhysicalDiagnosis.objects.all()
  serializer_class = PhysicalDiagnosisSerializer

class ExamViewSet(viewsets.ModelViewSet):
  queryset = Exam.objects.all()
  serializer_class = ExamSerializer

class TypeParameterViewSet(viewsets.ModelViewSet):
  queryset = TypeParameter.objects.all()
  serializer_class = TypeParameterSerializer

class MedicalParameterViewSet(viewsets.ModelViewSet):
  queryset = MedicalParameter.objects.all()
  serializer_class = MedicalParameterSerializer

class LifeStyleViewSet(viewsets.ModelViewSet):
  queryset = LifeStyle.objects.all()
  serializer_class = LifeStyleSerializer

class PhysicalActivityViewSet(viewsets.ModelViewSet):
  queryset = PhysicalActivity.objects.all()
  serializer_class = PhysicalActivitySerializer

class AddictionViewSet(viewsets.ModelViewSet):
  queryset = Addiction.objects.all()
  serializer_class = AddictionSerializer

class TravelViewSet(viewsets.ModelViewSet):
  queryset = Travel.objects.all()
  serializer_class = TravelSerializer

class SymptomViewSet(viewsets.ModelViewSet):
  queryset = Symptom.objects.all()
  serializer_class = SymptomSerializer


"""class ConceptViewSet(viewsets.ModelViewSet):
  queryset = Concept.objects.all()
  serializer_class = ConceptSerializer"""

class MedicalAntecedentViewSet(viewsets.ModelViewSet):
  queryset = MedicalAntecedent.objects.all()
  serializer_class = MedicalAntecedentSerializer

class ObstetricalAntecedentViewSet(viewsets.ModelViewSet):
  queryset = ObstetricalAntecedent.objects.all()
  serializer_class = ObstetricalAntecedentSerializer

class SurgeryViewSet(viewsets.ModelViewSet):
  queryset = Surgery.objects.all()
  serializer_class = SurgerySerializer

class AllergyViewSet(viewsets.ModelViewSet):
  queryset = Allergy.objects.all()
  serializer_class = AllergySerializer

class TreatmentViewSet(viewsets.ModelViewSet):
  queryset = Treatment.objects.all()
  serializer_class = TreatmentSerializer

class DiseaseViewSet(viewsets.ModelViewSet):
  queryset = Disease.objects.all()
  serializer_class = DiseaseSerializer

def Convert(tup, di):
  for a, b in tup.items(): 
    di[a] = b
  return di

@api_view(['GET'])
def getStat(request):

  learner_physician = LeanerPhysician.objects.all().count()
  clinical_case = ClinicalCase.objects.all().count()
  expert = ExpertPhysician.objects.all().count()
  evaluation = Evaluation.objects.all().count()

  result = {
      "learner_physician": learner_physician,
      "clinical_case": clinical_case,
      "expert": expert,
      "evaluation": evaluation
    }
  
  return Response(result, status=status.HTTP_200_OK)

def clinicalCase(request, id_clinical_case):
  l = []
  list_medical_parameter = []
  list_physical_dignosis = []
  list_exam = []
  list_life_style = []
  list_medical_antecedent = []
  list_disease = []

  context = {
        'request': request,
    }
  
  if id_clinical_case != 'all':
    clinical_cases = ClinicalCaseSerializer(ClinicalCase.objects.all().filter(id = id_clinical_case), many=True, context=context).data
  else:
    clinical_cases = ClinicalCaseSerializer(ClinicalCase.objects.all(), many=True, context=context).data
  
  for cl in clinical_cases:
    cl = Convert(cl, {})

    # Personal Information
    personal_info = PersonalInfo.objects.all().filter(clinical_case = cl["id"])
    p = PersonalInfoSerializer(personal_info, many=True, context=context).data
    cl["personal_info"] = [ Convert(t, {}) for t in p][0]

    # Medical Parameter
    medical_parameter = MedicalParameter.objects.all().filter(clinical_case = cl["id"])
    medical_parameters = MedicalParameterSerializer(medical_parameter, many=True, context=context).data
    type_parameter = TypeParameterSerializer(TypeParameter.objects.all(), many=True, context=context).data

    for medPar in medical_parameters:
      medPar = Convert(medPar, {})
      for type in type_parameter:
        type = Convert(type, {})
        if type["url"] == medPar["type_parameter"]:
          medPar["type_parameter"] = type
          break
      list_medical_parameter.append(medPar)
    cl["medical_parameter"] = list_medical_parameter
    list_medical_parameter = []

    # Physical Diagnosis
    physical_diagnosis = PhysicalDiagnosisSerializer(PhysicalDiagnosis.objects.all().filter(clinical_case = cl["id"]), many=True, context=context).data
    medias = MediaSerializer(Media.objects.all(), many=True, context=context).data
    for phydiag in physical_diagnosis:
      phydiag = Convert(phydiag, {})
      for med in medias:
        med = Convert(med, {})
        if med["url"] == phydiag["file"]:
          phydiag["file"] = med
          break
      list_physical_dignosis.append(phydiag)
    cl["physical_diagnosis"] = list_physical_dignosis
    list_physical_dignosis = []

    # Exam
    exams = ExamSerializer(Exam.objects.all().filter(clinical_case = cl["id"]), many=True, context=context).data
    medias = MediaSerializer(Media.objects.all(), many=True, context=context).data
    for ex in exams:
      ex = Convert(ex, {})
      for med in medias:
        med = Convert(med, {})
        if med["url"] == ex["file"]:
          ex["file"] = med
          break
      list_exam.append(ex)
    cl["exam"] = list_exam
    list_exam = []

    # Treatment in progress
    treatment_in_progress = TreatmentInProgressSerializer(TreatmentInProgress.objects.all().filter(clinical_case = cl["id"]), many=True, context=context).data
    cl["treatment_in_progress"] = [ Convert(t, {}) for t in treatment_in_progress]

    # Life style
    lifSty = None
    life_styles = LifeStyleSerializer(LifeStyle.objects.all().filter(clinical_case = cl["id"]), many=True, context=context).data
    for life_style in life_styles:
      life_style = Convert(life_style, {})

      physical_activities = PhysicalActivitySerializer(PhysicalActivity.objects.all().filter(life_style=life_style["id"]), many=True, context=context).data
      life_style["physical_activity"] = [Convert(t, {}) for t in physical_activities]

      addictions = AddictionSerializer(Addiction.objects.all().filter(life_style=life_style["id"]), many=True, context=context).data
      life_style["addiction"] = [Convert(t, {}) for t in addictions]

      travels = TravelSerializer(Travel.objects.all().filter(life_style=life_style["id"]), many=True, context=context).data
      life_style["travel"] = [Convert(t, {}) for t in travels]
      list_life_style.append(life_style)
    cl["life_style"] = list_life_style
    list_life_style = []

    # Symptom
    symptoms = SymptomSerializer(Symptom.objects.all().filter(clinical_case = cl["id"]), many=True, context=context).data
    cl["symptom"] = [ Convert(t, {}) for t in symptoms]

    # Medical Antecedent
    medical_antecedents = MedicalAntecedentSerializer(MedicalAntecedent.objects.all().filter(clinical_case = cl["id"]), many=True, context=context).data
    for medical_antecedent in medical_antecedents:
      medical_antecedent = Convert(medical_antecedent, {})

      obstetrical_antecedents = ObstetricalAntecedentSerializer(ObstetricalAntecedent.objects.all().filter(medical_antecedent=medical_antecedent["id"]), many=True, context=context).data
      medical_antecedent["obstetrical_antecedent"] = [Convert(t) for t in obstetrical_antecedents]

      surgeries = SurgerySerializer(Surgery.objects.all().filter(medical_antecedent = medical_antecedent["id"]), many=True, context=context).data
      medical_antecedent["surgery"] = [Convert(t, {}) for t in surgeries]

      allergies = AllergySerializer(Allergy.objects.all().filter(medical_antecedent=medical_antecedent["id"]), many=True, context=context).data
      medical_antecedent["allergy"] = [Convert(t, {}) for t in allergies]

      diseases = DiseaseSerializer(Disease.objects.all().filter(medical_antecedent=medical_antecedent["id"]), many=True, context=context).data
      for disease in diseases:
        disease = Convert(disease, {})

        treatements = TreatmentSerializer(Treatment.objects.all().filter(disease=disease["id"]), many=True, context=context).data
        disease["treatement"] = [Convert(t, {}) for t in treatements]

        list_disease.append(disease)
      medical_antecedent["disease"] = list_disease
      list_disease = []

      list_medical_antecedent.append(medical_antecedent)
    cl["medical_antecedent"] = list_medical_antecedent
    list_medical_antecedent = []

    l.append(cl)  
  
  return l

@api_view(['GET'])
def getClinicalCase(request, id_clinical_case):
  l = []
  list_medical_parameter = []
  list_physical_dignosis = []
  list_exam = []
  list_life_style = []
  list_medical_antecedent = []
  list_disease = []

  context = {
        'request': request,
    }
  
  if id_clinical_case != 'all':
    clinical_cases = ClinicalCaseSerializer(ClinicalCase.objects.all().filter(id = id_clinical_case), many=True, context=context).data
  else:
    clinical_cases = ClinicalCaseSerializer(ClinicalCase.objects.all(), many=True, context=context).data
  
  for cl in clinical_cases:
    cl = Convert(cl, {})

    # Personal Information
    personal_info = PersonalInfo.objects.all().filter(clinical_case = cl["id"])
    p = PersonalInfoSerializer(personal_info, many=True, context=context).data
    cl["personal_info"] = [ Convert(t, {}) for t in p][0]

    # Medical Parameter
    medical_parameter = MedicalParameter.objects.all().filter(clinical_case = cl["id"])
    medical_parameters = MedicalParameterSerializer(medical_parameter, many=True, context=context).data
    type_parameter = TypeParameterSerializer(TypeParameter.objects.all(), many=True, context=context).data

    for medPar in medical_parameters:
      medPar = Convert(medPar, {})
      for type in type_parameter:
        type = Convert(type, {})
        if type["url"] == medPar["type_parameter"]:
          medPar["type_parameter"] = type
          break
      list_medical_parameter.append(medPar)
    cl["medical_parameter"] = list_medical_parameter
    list_medical_parameter = []

    # Physical Diagnosis
    physical_diagnosis = PhysicalDiagnosisSerializer(PhysicalDiagnosis.objects.all().filter(clinical_case = cl["id"]), many=True, context=context).data
    medias = MediaSerializer(Media.objects.all(), many=True, context=context).data
    for phydiag in physical_diagnosis:
      phydiag = Convert(phydiag, {})
      for med in medias:
        med = Convert(med, {})
        if med["url"] == phydiag["file"]:
          phydiag["file"] = med
          break
      list_physical_dignosis.append(phydiag)
    cl["physical_diagnosis"] = list_physical_dignosis
    list_physical_dignosis = []

    # Exam
    exams = ExamSerializer(Exam.objects.all().filter(clinical_case = cl["id"]), many=True, context=context).data
    medias = MediaSerializer(Media.objects.all(), many=True, context=context).data
    for ex in exams:
      ex = Convert(ex, {})
      for med in medias:
        med = Convert(med, {})
        if med["url"] == ex["file"]:
          ex["file"] = med
          break
      list_exam.append(ex)
    cl["exam"] = list_exam
    list_exam = []

    # Treatment in progress
    treatment_in_progress = TreatmentInProgressSerializer(TreatmentInProgress.objects.all().filter(clinical_case = cl["id"]), many=True, context=context).data
    cl["treatment_in_progress"] = [ Convert(t, {}) for t in treatment_in_progress]

    # Life style
    lifSty = None
    life_styles = LifeStyleSerializer(LifeStyle.objects.all().filter(clinical_case = cl["id"]), many=True, context=context).data
    for life_style in life_styles:
      life_style = Convert(life_style, {})

      physical_activities = PhysicalActivitySerializer(PhysicalActivity.objects.all().filter(life_style=life_style["id"]), many=True, context=context).data
      life_style["physical_activity"] = [Convert(t, {}) for t in physical_activities]

      addictions = AddictionSerializer(Addiction.objects.all().filter(life_style=life_style["id"]), many=True, context=context).data
      life_style["addiction"] = [Convert(t, {}) for t in addictions]

      travels = TravelSerializer(Travel.objects.all().filter(life_style=life_style["id"]), many=True, context=context).data
      life_style["travel"] = [Convert(t, {}) for t in travels]
      list_life_style.append(life_style)
    cl["life_style"] = list_life_style
    list_life_style = []

    # Symptom
    symptoms = SymptomSerializer(Symptom.objects.all().filter(clinical_case = cl["id"]), many=True, context=context).data
    cl["symptom"] = [ Convert(t, {}) for t in symptoms]

    # Medical Antecedent
    medical_antecedents = MedicalAntecedentSerializer(MedicalAntecedent.objects.all().filter(clinical_case = cl["id"]), many=True, context=context).data
    for medical_antecedent in medical_antecedents:
      medical_antecedent = Convert(medical_antecedent, {})

      obstetrical_antecedents = ObstetricalAntecedentSerializer(ObstetricalAntecedent.objects.all().filter(medical_antecedent=medical_antecedent["id"]), many=True, context=context).data
      medical_antecedent["obstetrical_antecedent"] = [Convert(t) for t in obstetrical_antecedents]

      surgeries = SurgerySerializer(Surgery.objects.all().filter(medical_antecedent = medical_antecedent["id"]), many=True, context=context).data
      medical_antecedent["surgery"] = [Convert(t, {}) for t in surgeries]

      allergies = AllergySerializer(Allergy.objects.all().filter(medical_antecedent=medical_antecedent["id"]), many=True, context=context).data
      medical_antecedent["allergy"] = [Convert(t, {}) for t in allergies]

      diseases = DiseaseSerializer(Disease.objects.all().filter(medical_antecedent=medical_antecedent["id"]), many=True, context=context).data
      for disease in diseases:
        disease = Convert(disease, {})

        treatements = TreatmentSerializer(Treatment.objects.all().filter(disease=disease["id"]), many=True, context=context).data
        disease["treatement"] = [Convert(t, {}) for t in treatements]

        list_disease.append(disease)
      medical_antecedent["disease"] = list_disease
      list_disease = []

      list_medical_antecedent.append(medical_antecedent)
    cl["medical_antecedent"] = list_medical_antecedent
    list_medical_antecedent = []

    l.append(cl)  
  
  return Response(l, status=status.HTTP_200_OK)

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