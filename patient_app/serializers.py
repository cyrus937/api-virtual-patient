from .models import *
from rest_framework import serializers

class MedecinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medecin
        fields = [
            'id',
            'nom',
            'prenom',
            'numero_telephone',
            'adresse',
            'ville',
            'cni',
            'sexe',
            'specialite',
            'annee_de_naissance',
            'lieu_naissance',
            'nationalite',
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
            'nom',
            'prenom',
            'numero_telephone',
            'adresse',
            'ville',
            'cni',
            'sexe',
            'specialite',
            'annee_de_naissance',
            'lieu_naissance',
            'nationalite',
            'email',
            'username',
            'password',
            'experience',
            'niveau_connaissance',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class MedecinExpertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedecinExpert
        fields = [
            'id',
            'nom',
            'prenom',
            'numero_telephone',
            'adresse',
            'ville',
            'cni',
            'sexe',
            'specialite',
            'annee_de_naissance',
            'lieu_naissance',
            'nationalite',
            'email',
            'username',
            'password',
            'grade',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class LogSerializer(serializers.HyperlinkedModelSerializer):

    medecin = MedecinSerializer(read_only=True)

    class Meta:
        model = Log
        fields = [
            'id',
            'operation',
            'medecin',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class PatientVirtuelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientVirtuel
        fields = [
            'id',
            'sexe',
            'etat_civil',
            'age_min',
            'age_max',
            'poids',
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
            'probleme_initial',
            'difficulte',
            'diagnostic_final',
            'systeme',
            'specialite',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class CasVirtuelSerializer(serializers.HyperlinkedModelSerializer):

    cas_clinique = CasCliniqueSerializer(read_only=True)
    patient_virtuel = PatientVirtuelSerializer(read_only=True)

    class Meta:
        model = CasVirtuel
        fields = [
            'id',
            'patient_virtuel',
            'cas_clinique',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):

    medecin_expert = MedecinExpertSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = [
            'id',
            'commentaire',
            'medecin_expert',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class EvaluationSerializer(serializers.HyperlinkedModelSerializer):

    medecin_apprenant = MedecinApprenantSerializer(read_only=True)
    cas_virtuel = CasVirtuelSerializer(read_only=True)
    feedback = FeedbackSerializer(read_only=True)

    class Meta:
        model = Evaluation
        fields = [
            'id',
            'type',
            'note',
            'remarque',
            'medecin_apprenant',
            'cas_virtuel',
            'feedback',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class HypotheseSerializer(serializers.HyperlinkedModelSerializer):

    medecin_apprenant = MedecinApprenantSerializer(read_only=True)
    evaluation = EvaluationSerializer(read_only=True)

    class Meta:
        model = Hypothese
        fields = [
            'id',
            'description',
            'medecin_apprenant',
            'evaluation',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    medecin_apprenant = MedecinApprenantSerializer(read_only=True)
    evaluation = EvaluationSerializer(read_only=True)

    class Meta:
        model = Question
        fields = [
            'id',
            'question',
            'reponse',
            'medecin_apprenant',
            'evaluation',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class InfosPersonnellesSerializer(serializers.HyperlinkedModelSerializer):

    cas_clinique = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = InfosPersonnelles
        fields = [
            'id',
            'sexe',
            'etat_civil',
            'profession',
            'nbre_enfant',
            'groupe_sanguin',
            'cas_clinique',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class TraitementEnCoursSerializer(serializers.HyperlinkedModelSerializer):

    cas_clinique = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = TraitementEnCours
        fields = [
            'id',
            'nom',
            'mode_transmission',
            'date_debut',
            'observation',
            'efficacite',
            'cas_clinique',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class DiagnosticPhysiqueSerializer(serializers.HyperlinkedModelSerializer):

    cas_clinique = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = DiagnosticPhysique
        fields = [
            'id',
            'diagnostic_physique',
            'resultat',
            'fichier',
            'cas_clinique',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ExamenSerializer(serializers.HyperlinkedModelSerializer):

    cas_clinique = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = Examen
        fields = [
            'id',
            'description',
            'resultat',
            'cas_clinique',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ExamenPhysiqueSerializer(serializers.HyperlinkedModelSerializer):

    cas_clinique = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = ExamenPhysique
        fields = [
            'id',
            'description',
            'resultat',
            'cas_clinique',
            'anatomie',
            'type_resultat',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class MediaSerializer(serializers.HyperlinkedModelSerializer):

    examen = ExamenSerializer(read_only=True)

    class Meta:
        model = Media
        fields = [
            'id',
            'fichier',
            'examen',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class TypeParametreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TypeParametre
        fields = [
            'id',
            'nom',
            'unite',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ParametreMedicalSerializer(serializers.HyperlinkedModelSerializer):

    cas_clinique = CasCliniqueSerializer(read_only=True)
    type_parametre = TypeParametreSerializer(read_only=True)

    class Meta:
        model = ParametreMedical
        fields = [
            'id',
            'valeur',
            'commantaire',
            'type_parametre',
            'cas_clinique',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ModeVieSerializer(serializers.HyperlinkedModelSerializer):

    cas_clinique = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = ModeVie
        fields = [
            'id',
            'qualite_eau',
            'moustiquaire',
            'animal_compagnie',
            'cas_clinique',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ActivitePhysiqueSerializer(serializers.HyperlinkedModelSerializer):

    mode_vie = ModeVieSerializer(read_only=True)

    class Meta:
        model = ActivitePhysique
        fields = [
            'id',
            'nom',
            'frequence',
            'mode_vie',
            'created_at',
            'deleted_at',
            'updated_at'
        ]
    
class AddictionSerializer(serializers.HyperlinkedModelSerializer):

    mode_vie = ModeVieSerializer(read_only=True)

    class Meta:
        model = Addiction
        fields = [
            'id',
            'nom',
            'frequence',
            'duree',
            'debut',
            'mode_vie',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class VoyageSerializer(serializers.HyperlinkedModelSerializer):

    mode_vie = ModeVieSerializer(read_only=True)

    class Meta:
        model = Voyage
        fields = [
            'id',
            'lieu',
            'frequence',
            'duree',
            'mode_vie',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class SymptomeSerializer(serializers.HyperlinkedModelSerializer):

    cas_clinique = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = Symptome
        fields = [
            'id',
            'localisation',
            'frequence',
            'duree',
            'date_debut',
            'evolution',
            'activite_declenchante',
            'cas_clinique',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class DescriptionSymptomeSerializer(serializers.HyperlinkedModelSerializer):

    symptome = SymptomeSerializer(read_only=True)

    class Meta:
        model = DescriptionSymptome
        fields = [
            'id',
            'degre',
            'fonction_physiologique',
            'symptome',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ConceptSerializer(serializers.HyperlinkedModelSerializer):

    cas_clinique = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = Concept
        fields = [
            'id',
            'nom',
            'cas_clinique',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class AntecedentMedicalSerializer(serializers.HyperlinkedModelSerializer):

    cas_clinique = CasCliniqueSerializer(read_only=True)

    class Meta:
        model = AntecedentMedical
        fields = [
            'id',
            'antecedents_familiaux',
            'cas_clinique',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class AntecedentObstetricalSerializer(serializers.HyperlinkedModelSerializer):

    antecedent_medical = AntecedentMedicalSerializer(read_only=True)

    class Meta:
        model = AntecedentObstetrical
        fields = [
            'id',
            'nbre_grossesse',
            'date_dernier_grossesse',
            'antecedent_medical',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class ChirurgieSerializer(serializers.HyperlinkedModelSerializer):

    antecedent_medical = AntecedentMedicalSerializer(read_only=True)

    class Meta:
        model = Chirurgie
        fields = [
            'id',
            'nom',
            'date',
            'antecedent_medical',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class AllergieSerializer(serializers.HyperlinkedModelSerializer):

    antecedent_medical = AntecedentMedicalSerializer(read_only=True)

    class Meta:
        model = Allergie
        fields = [
            'id',
            'manifestation',
            'declencheur',
            'antecedent_medical',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class TraitementSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Traitement
        fields = [
            'id',
            'nom',
            'duree',
            'posologie',
            'created_at',
            'deleted_at',
            'updated_at'
        ]

class MaladieSerializer(serializers.HyperlinkedModelSerializer):

    antecedent_medical = AntecedentMedicalSerializer(read_only=True)
    traitement = TraitementSerializer(read_only=True)

    class Meta:
        model = Maladie
        fields = [
            'id',
            'nom',
            'date_debut',
            'date_fin',
            'observation',
            'antecedent_medical',
            'traitement',
            'created_at',
            'deleted_at',
            'updated_at'
        ]