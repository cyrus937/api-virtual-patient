from django.shortcuts import redirect
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User

from .models import *
from .serializers import *

# Create your views here.

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


class ConceptViewSet(viewsets.ModelViewSet):
  queryset = Concept.objects.all()
  serializer_class = ConceptSerializer

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