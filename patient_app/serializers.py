from .models import *
from rest_framework import serializers

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'id',
            'name',
            'first_name',
            'phone_number',
            'address',
            'city',
            'cni',
            'sex',
            'specialty',
            'year_of_birth',
            'place_of_birth',
            'nationality',
            'email',
            'username',
            'password',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class LeanerPhysicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LeanerPhysician
        fields = [
            'id',
            'name',
            'first_name',
            'phone_number',
            'address',
            'city',
            'cni',
            'sex',
            'specialty',
            'year_of_birth',
            'place_of_birth',
            'nationality',
            'email',
            'username',
            'password',
            'experience',
            'knowledge_level',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ExpertPhysicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExpertPhysician
        fields = [
            'id',
            'name',
            'first_name',
            'phone_number',
            'address',
            'city',
            'cni',
            'sex',
            'specialty',
            'year_of_birth',
            'place_of_birth',
            'nationality',
            'email',
            'username',
            'password',
            'grade',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class LogSerializer(serializers.HyperlinkedModelSerializer):

   

    class Meta:
        model = Log
        fields = [
            'id',
            'operation',
            'doctor',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class VirtualPatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VirtualPatient
        fields = [
            'id',
            'sex',
            'civil_status',
            'min_age',
            'max_age',
            'weight',
            'modele_3D',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ClinicalCaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClinicalCase
        fields = [
            'id',
            'initial_problem',
            'difficulty',
            'final_diagnosis',
            'system',
            'specialty',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class VirtualCaseSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = VirtualCase
        fields = [
            'id',
            'virtual_patient',
            'clinical_case',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Feedback
        fields = [
            'id',
            'comment',
            'expert_physician',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class EvaluationSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Evaluation
        fields = [
            'id',
            'type',
            'mark',
            'note',
            'learner_physician',
            'virtual_case',
            'feedback',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class HypothesisSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Hypothesis
        fields = [
            'id',
            'description',
            'learner_physician',
            'evaluation',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class QuestionSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Question
        fields = [
            'id',
            'question',
            'answer',
            'learner_physician',
            'evaluation',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class PersonalInfoSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = PersonalInfo
        fields = [
            'id',
            'sex',
            'civil_status',
            'profession',
            'nb_child',
            'blood_group',
            'clinical_case',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class TreatmentInProgressSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = TreatmentInProgress
        fields = [
            'id',
            'name',
            'transmission_mode',
            'start_time',
            'observation',
            'efficiency',
            'clinical_case',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class DiagnosisPhysicsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DiagnosisPhysics
        fields = [
            'id',
            'physical_diagnosis',
            'result',
            'file',
            'clinical_case',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ExamSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Exam
        fields = [
            'id',
            'description',
            'result',
            'clinical_case',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ExamPhysicsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ExamPhysics
        fields = [
            'id',
            'description',
            'result',
            'clinical_case',
            'anatomy',
            'type_result',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class MediaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Media
        fields = [
            'id',
            'file',
            'exam',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class TypeParameterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TypeParameter
        fields = [
            'id',
            'name',
            'unit',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class MedicalParameterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MedicalParameter
        fields = [
            'id',
            'value',
            'commantaire',
            'type_parameter',
            'clinical_case',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class LifeStyleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LifeStyle
        fields = [
            'id',
            'water_quality',
            'mosquito',
            'pet_company',
            'clinical_case',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class PhysicalActivitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PhysicalActivity
        fields = [
            'id',
            'name',
            'frequency',
            'life_style',
            'created_at',
            'deleted_at',
            'updated_at'
        ]
    
class AddictionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Addiction
        fields = [
            'id',
            'name',
            'frequency',
            'duration',
            'start',
            'life_style',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class TravelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Travel
        fields = [
            'id',
            'location',
            'frequency',
            'duration',
            'life_style',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class SymptomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Symptom
        fields = [
            'id',
            'localisation',
            'frequency',
            'duration',
            'start_time',
            'evolution',
            'triggering_activity',
            'clinical_case',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class DescriptionSymptomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DescriptionSymptom
        fields = [
            'id',
            'degree',
            'physiological_function',
            'symptom',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ConceptSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Concept
        fields = [
            'id',
            'name',
            'clinical_case',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class MedicalAntecedentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MedicalAntecedent
        fields = [
            'id',
            'family_antecedents',
            'clinical_case',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ObstetricalAntecedentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ObstetricalAntecedent
        fields = [
            'id',
            'nb_pregnancy',
            'date_of_last_pregnancy',
            'medical_antecedent',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class SurgerySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Surgery
        fields = [
            'id',
            'name',
            'date',
            'medical_antecedent',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class AllergySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Allergy
        fields = [
            'id',
            'manifestation',
            'trigger',
            'medical_antecedent',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class TreatmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Treatment
        fields = [
            'id',
            'name',
            'duration',
            'posology',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class DiseaseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Disease
        fields = [
            'id',
            'name',
            'start_time',
            'end_time',
            'observation',
            'medical_antecedent',
            'treatment',
            'created_at',
            'deleted_at',
            'updated_at'
        ]