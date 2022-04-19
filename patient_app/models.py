from random import choices
from django.db import models
import uuid

# Create your models here.
class Medecin(models.Model):
    """
        Medecin Apprenant model
    """
    SEXE = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )

    SPECIALITE = (
        ('Généraliste', 'Généraliste'),
        ('Neurologiste', 'Neurologiste'),
        ('Gynécologue', 'Gynécologue'),
        ('Pédiatre', 'Pédiatre'),
        ('Dentiste', 'Dentiste'),
        ('Ophtamologue', 'Ophtamologue'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50, null=False)
    prenom = models.CharField(max_length=50, null=False)
    numero_telephone = models.CharField(max_length=20, default='+237 ', unique=True)
    adresse = models.CharField(max_length=30, null=False)
    ville = models.CharField(max_length=50, null=True)
    cni = models.CharField(max_length=50, null=True, unique=True)
    sexe = models.CharField(choices=SEXE, max_length=50)
    specialite = models.CharField(choices=SPECIALITE, max_length=50)
    annee_de_naissance = models.DateField(null=False)
    lieu_naissance = models.CharField(max_length=150, null=False)
    nationalite = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50, unique=True, null=False)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return self.nom + " " + self.prenom + " " + str(self.date_naissance)

class MedecinApprenant(Medecin):
    EXPERIENCE = (
        ("Debutant", "Debutant"),
        ("Intermediaire", "Intermediare"),
        ("Expert", "Expert")
    )

    experience = models.CharField(max_length=20, choices=EXPERIENCE)
    niveau_connaissance = models.DecimalField(default=0.0, null=True, decimal_places=2, max_digits=6)

class MedecinExpert(Medecin):
    GRADE = (
        ('MG', 'Médecin Généraliste'),
        ('MS', 'Médecin Spécialiste'),
        ('Prof', 'Professeur')
    )
    grade = models.CharField(max_length=20, choices=GRADE, null=False)

class Log(models.Model):

    OPERATION = (
        ('UPDATE', 'UPDATE'),
        ('CREATE', 'CREATE'),
        ('DELETE', 'DELETE')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    operation = models.CharField(max_length=20, choices=OPERATION)
    medecin = models.ForeignKey(Medecin, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class PatientVirtuel(models.Model):

    SEXE = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )

    ETAT_CIVIL = (
        ('CELIBATAIRE', 'CELIBATAIRE'),
        ('MARIE', 'MARIE'),
        ('DIVORCE', 'DIVORCE')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sexe = models.CharField(choices=SEXE, max_length=50)
    etat_civil = models.CharField(choices=ETAT_CIVIL, max_length=50)
    age_min = models.IntegerField(default=0, null=False)
    age_max = models.IntegerField(default=0, null=False)
    poids = models.DecimalField(default=0.0, null=False, decimal_places=2, max_digits=6)
    modele_3D = models.FileField(null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class CasClinique(models.Model):

    DIFFICULTE = (
        ('FACILE', 'FACILE'),
        ('MOYEN', 'MOYEN'),
        ('DIFFICILE', 'DIFFICILE')
    )

    SYSTEME = (
        ('SYSTEME RESPIRATOIRE', 'SYSTEME RESPIRATOIRE'),
        ('SYSTEME CARDIOVASCULAIRE', 'SYSTEME CARDIOVASCULAIRE')
    )

    SPECIALITE = (
        ('Généraliste', 'Généraliste'),
        ('Neurologiste', 'Neurologiste'),
        ('Gynécologue', 'Gynécologue'),
        ('Pédiatre', 'Pédiatre'),
        ('Dentiste', 'Dentiste'),
        ('Ophtamologue', 'Ophtamologue'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    probleme_initial =  models.TextField(null=False)
    difficulte = models.CharField(choices=DIFFICULTE, max_length=50)
    diagnostic_final = models.CharField(null=False, max_length=100)
    systeme = models.CharField(choices=SYSTEME, max_length=50)
    specialite = models.CharField(choices=SPECIALITE, max_length=50)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class CasVirtuel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_virtuel = models.ForeignKey(PatientVirtuel, on_delete=models.SET_NULL, null=True)
    cas_clinique = models.ForeignKey(CasClinique, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)


class Feedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    commentaire = models.TextField(blank=True)
    medecin_expert = models.ForeignKey(MedecinExpert, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Evaluation(models.Model):

    TYPE = (
        ('FORMATIF', 'FORMATIF'),
        ('SOMMATIF', 'SOMMATIF')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=20, choices=TYPE)
    note = models.DecimalField(default=0.0, null=True, decimal_places=2, max_digits=5)
    remarque = models.TextField(blank=True)
    medecin_apprenant = models.ForeignKey(MedecinApprenant, on_delete=models.SET_NULL, null=True)
    cas_virtuel = models.ForeignKey(CasVirtuel, on_delete=models.SET_NULL, null=True)
    feedback = models.ForeignKey(Feedback, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Hypothese(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(blank=False)
    medecin_apprenant = models.ForeignKey(MedecinApprenant, on_delete=models.SET_NULL, null=True)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Question(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.TextField(blank=False)
    reponse = models.TextField(blank=False)
    medecin_apprenant = models.ForeignKey(MedecinApprenant, on_delete=models.SET_NULL, null=True)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

# Information du cas clinique
class InfosPersonnelles(models.Model):
    SEXE = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )

    ETAT_CIVIL = (
        ('CELIBATAIRE', 'CELIBATAIRE'),
        ('MARIE', 'MARIE'),
        ('DIVORCE', 'DIVORCE')
    )

    GROUPE_SANGUIN = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O-')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sexe = models.CharField(choices=SEXE, max_length=50)
    age = models.IntegerField(null=False)
    etat_civil = models.CharField(choices=ETAT_CIVIL, max_length=50)
    profession = models.CharField(max_length=100, null=True)
    nbre_enfant = models.IntegerField(null=True)
    groupe_sanguin = models.CharField(choices=GROUPE_SANGUIN, null=True, max_length=50)
    cas_clinique = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class TraitementEnCours(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50, null=False)
    mode_transmission = models.CharField(max_length=100)
    date_debut = models.DateField(null=False)
    observation = models.TextField(blank=True)
    efficacite = models.CharField(max_length=50, null=True)
    cas_clinique = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class DiagnosticPhysique(models.Model):

    DIAGNOSTIC_PHYSIQUE = (
        ('PALPATION', 'PALPATION'),
        ('OSCULTATION', 'OSCULTATION'),
        ('PERCUTION', 'PERCUTION'),
        ('INSPECTION', 'INSPECTION')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    diagnostic_physique = models.CharField(max_length=50, choices=DIAGNOSTIC_PHYSIQUE)
    resultat = models.TextField(blank=False)
    fichier = models.FileField(null=True)
    cas_clinique = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Examen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(blank=False)
    resultat = models.TextField(blank=False)
    cas_clinique = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class ExamenPhysique(Examen):
    anatomie = models.CharField(max_length=50)
    type_resultat = models.CharField(max_length=50, null=True)

class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fichier = models.FileField(null=False)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class TypeParametre(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=30)
    unite = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return self.nom + " en " + self.unite
class ParametreMedical(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    valeur = models.DecimalField(max_digits=10, decimal_places=2)
    commentaire = models.TextField(blank=True)
    type_parametre = models.ForeignKey(TypeParametre, on_delete=models.CASCADE, null=False)
    cas_clinique = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return self.type_parametre.nom + " = " + self.valeur + " " + self.type_parametre.unite

class ModeVie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    qualite_eau = models.CharField(max_length=50, null=True)
    moustiquaire = models.BooleanField(null=False)
    animal_compagnie = models.CharField(max_length=50, null=True)
    cas_clinique = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class ActivitePhysique(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50)
    frequence = models.CharField(max_length=50)
    mode_vie = models.ForeignKey(ModeVie, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Addiction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=50)
    frequence = models.CharField(max_length=50)
    duree = models.CharField(max_length=50, null=True)
    debut = models.DateField(null=True)
    mode_vie = models.ForeignKey(ModeVie, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Voyage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lieu = models.CharField(max_length=50)
    frequence = models.CharField(max_length=50)
    duree = models.CharField(max_length=50, null=True)
    mode_vie = models.ForeignKey(ModeVie, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Symptome(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    localisation = models.CharField(max_length=100)
    frequence = models.CharField(max_length=100)
    duree = models.CharField(max_length=100, null=True)
    date_debut = models.DateField(null=True)
    evolution = models.CharField(max_length=150)
    activite_declenchante = models.CharField(max_length=100)
    cas_clinique = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class DescriptionSymptome(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    degre = models.CharField(max_length=100)
    fonction_physiologique = models.CharField(max_length=100)
    symptome = models.ForeignKey(Symptome, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Concept(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100)
    cas_clinique = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class AntecedentMedical(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    antecedents_familiaux = models.CharField(max_length=100)
    cas_clinique = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class AntecedentObstetrical(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nbre_grossesse = models.IntegerField()
    date_derniere_grossesse = models.DateField(null=True)
    antecedent_medical = models.ForeignKey(AntecedentMedical, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Chirurgie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100)
    date = models.DateField(null=True)
    antecedent_medical = models.ForeignKey(AntecedentMedical, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Allergie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manifestation = models.TextField(blank=False)
    declencheur = models.CharField(max_length=200, null=True)
    antecedent_medical = models.ForeignKey(AntecedentMedical, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Traitement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100)
    duree = models.CharField(max_length=150 ,null=True)
    posologie = models.TextField(blank=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Maladie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    observation = models.TextField(blank=True)
    antecedent_medical = models.ForeignKey(AntecedentMedical, on_delete=models.CASCADE, null=False)
    traitement = models.ForeignKey(Traitement, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)