from .models import *
from rest_framework import serializers

class MedecinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medecin
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

class MedecinApprenantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedecinApprenant
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

class MedecinExpertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedecinExpert
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

    doctor = MedecinSerializer(read_only=True)

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

class PatientVirtuelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientVirtuel
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

class CasCliniqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CasClinique
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

class CasVirtuelSerializer(serializers.HyperlinkedModelSerializer):

    clinical_case = CasCliniqueSerializer(read_only=True)
    virtual_patient = PatientVirtuelSerializer(read_only=True)

    class Meta:
        model = CasVirtuel
        fields = [
            'id',
            'virtual_patient',
            'clinical_case',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):

    expert_physician = MedecinExpertSerializer(read_only=True)

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

    learner_physician = MedecinApprenantSerializer(read_only=True)
    virtual_case = CasVirtuelSerializer(read_only=True)
    feedback = FeedbackSerializer(read_only=True)

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

class HypotheseSerializer(serializers.HyperlinkedModelSerializer):

    learner_physician = MedecinApprenantSerializer(read_only=True)
    evaluation = EvaluationSerializer(read_only=True)

    class Meta:
        model = Hypothese
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

    learner_physician = MedecinApprenantSerializer(read_only=True)
    evaluation = EvaluationSerializer(read_only=True)

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

class InfosPersonnellesSerializer(serializers.HyperlinkedModelSerializer):

    clinical_case = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = InfosPersonnelles
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

class TraitementEnCoursSerializer(serializers.HyperlinkedModelSerializer):

    clinical_case = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = TraitementEnCours
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

class DiagnosticPhysiqueSerializer(serializers.HyperlinkedModelSerializer):

    clinical_case = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = DiagnosticPhysique
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

class ExamenSerializer(serializers.HyperlinkedModelSerializer):

    clinical_case = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = Examen
        fields = [
            'id',
            'description',
            'result',
            'clinical_case',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ExamenPhysiqueSerializer(serializers.HyperlinkedModelSerializer):

    clinical_case = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = ExamenPhysique
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

    exam = ExamenSerializer(read_only=True)

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

class TypeParametreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TypeParametre
        fields = [
            'id',
            'name',
            'unit',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ParametreMedicalSerializer(serializers.HyperlinkedModelSerializer):

    clinical_case = CasCliniqueSerializer(read_only=True)
    type_parameter = TypeParametreSerializer(read_only=True)

    class Meta:
        model = ParametreMedical
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

class ModeVieSerializer(serializers.HyperlinkedModelSerializer):

    clinical_case = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = ModeVie
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

class ActivitePhysiqueSerializer(serializers.HyperlinkedModelSerializer):

    life_style = ModeVieSerializer(read_only=True)

    class Meta:
        model = ActivitePhysique
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

    life_style = ModeVieSerializer(read_only=True)

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

class VoyageSerializer(serializers.HyperlinkedModelSerializer):

    life_style = ModeVieSerializer(read_only=True)

    class Meta:
        model = Voyage
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

class SymptomeSerializer(serializers.HyperlinkedModelSerializer):

    clinical_case = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = Symptome
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

class DescriptionSymptomeSerializer(serializers.HyperlinkedModelSerializer):

    symptom = SymptomeSerializer(read_only=True)

    class Meta:
        model = DescriptionSymptome
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

    clinical_case = CasCliniqueSerializer(read_only=True)

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

class AntecedentMedicalSerializer(serializers.HyperlinkedModelSerializer):

    clinical_case = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = AntecedentMedical
        fields = [
            'id',
            'family_antecedents',
            'clinical_case',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class AntecedentObstetricalSerializer(serializers.HyperlinkedModelSerializer):

    medical_antecedent = AntecedentMedicalSerializer(read_only=True)

    class Meta:
        model = AntecedentObstetrical
        fields = [
            'id',
            'nb_pregnancy',
            'date_of_last_pregnancy',
            'medical_antecedent',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ChirurgieSerializer(serializers.HyperlinkedModelSerializer):

    medical_antecedent = AntecedentMedicalSerializer(read_only=True)

    class Meta:
        model = Chirurgie
        fields = [
            'id',
            'name',
            'date',
            'medical_antecedent',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class AllergieSerializer(serializers.HyperlinkedModelSerializer):

    medical_antecedent = AntecedentMedicalSerializer(read_only=True)

    class Meta:
        model = Allergie
        fields = [
            'id',
            'manifestation',
            'trigger',
            'medical_antecedent',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class TraitementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Traitement
        fields = [
            'id',
            'name',
            'duration',
            'posology',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class MaladieSerializer(serializers.HyperlinkedModelSerializer):

    medical_antecedent = AntecedentMedicalSerializer(read_only=True)
    treatment = TraitementSerializer(read_only=True)

    class Meta:
        model = Maladie
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