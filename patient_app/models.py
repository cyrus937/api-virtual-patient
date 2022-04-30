from random import choices
from django.db import models
import uuid

# Create your models here.
class Medecin(models.Model):
    """
        Medecin Apprenant model
    """
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    SPECIALTY = (
        ('Generalist', 'Generalist'),
        ('Neurologist', 'Neurologist'),
        ('Gynecologist', 'Gynecologist'),
        ('Pediatrician', 'Pediatrician'),
        ('Dentist', 'Dentist'),
        ('Ophthalmologist', 'Ophthalmologist'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=20, default='+237 ', unique=True)
    address = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=50, null=True)
    cni = models.CharField(max_length=50, null=True, unique=True)
    sex = models.CharField(choices=SEX, max_length=50)
    specialty = models.CharField(choices=SPECIALTY, max_length=50)
    year_of_birth = models.DateField(null=False)
    place_of_birth = models.CharField(max_length=150, null=False)
    nationality = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50, unique=True, null=False)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.first_name + " " + str(self.year_of_birth)

class MedecinApprenant(Medecin):
    EXPERIENCE = (
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Expert", "Expert")
    )

    experience = models.CharField(max_length=20, choices=EXPERIENCE)
    knowledge_level = models.DecimalField(default=0.0, null=True, decimal_places=2, max_digits=6)

class MedecinExpert(Medecin):
    GRADE = (
        ('GP', 'Generalist Physician'),
        ('SP', 'Specialist Physician'),
        ('Prof', 'Professor')
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
    doctor = models.ForeignKey(Medecin, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class PatientVirtuel(models.Model):

    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    CIVIL_STATUS = (
        ('CELIBATORY', 'CELIBATORY'),
        ('MARY', 'MARY'),
        ('DIVORCE', 'DIVORCE')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sex = models.CharField(choices=SEX, max_length=50)
    civil_status = models.CharField(choices=CIVIL_STATUS, max_length=50)
    min_age = models.IntegerField(default=0, null=False)
    max_age = models.IntegerField(default=0, null=False)
    weight = models.DecimalField(default=0.0, null=False, decimal_places=2, max_digits=6)
    modele_3D = models.FileField(null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class CasClinique(models.Model):

    DIFFICULTE = (
        ('EASY', 'EASY'),
        ('MEDIUM', 'MEDIUM'),
        ('HARD', 'HARD')
    )

    SYSTEM = (
        ('RESPIRATORY SYSTEM', 'RESPIRATORY SYSTEM'),
        ('CARDIOVASCULAR SYSTEM', 'CARDIOVASCULAR SYSTEM')
    )

    SPECIALTY = (
        ('Generalist', 'Generalist'),
        ('Neurologist', 'Neurologist'),
        ('Gynecologist', 'Gynecologist'),
        ('Pediatrician', 'Pediatrician'),
        ('Dentist', 'Dentist'),
        ('Ophthalmologist', 'Ophthalmologist'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    initial_problem =  models.TextField(null=False)
    difficulty = models.CharField(choices=DIFFICULTE, max_length=50)
    final_diagnosis = models.CharField(null=False, max_length=100)
    system = models.CharField(choices=SYSTEM, max_length=50)
    specialty = models.CharField(choices=SPECIALTY, max_length=50)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class CasVirtuel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    virtual_patient = models.ForeignKey(PatientVirtuel, on_delete=models.SET_NULL, null=True)
    clinical_case = models.ForeignKey(CasClinique, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)


class Feedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.TextField(blank=True)
    expert_physician = models.ForeignKey(MedecinExpert, on_delete=models.SET_NULL, null=True)
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
    mark = models.DecimalField(default=0.0, null=True, decimal_places=2, max_digits=5)
    note = models.TextField(blank=True)
    learner_physician = models.ForeignKey(MedecinApprenant, on_delete=models.SET_NULL, null=True)
    virtual_case = models.ForeignKey(CasVirtuel, on_delete=models.SET_NULL, null=True)
    feedback = models.ForeignKey(Feedback, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Hypothese(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(blank=False)
    learner_physician = models.ForeignKey(MedecinApprenant, on_delete=models.SET_NULL, null=True)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Question(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.TextField(blank=False)
    answer = models.TextField(blank=False)
    learner_physician = models.ForeignKey(MedecinApprenant, on_delete=models.SET_NULL, null=True)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

# Information du cas clinique
class InfosPersonnelles(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    CIVIL_STATUS = (
        ('CELIBATORY', 'CELIBATORY'),
        ('MARY', 'MARY'),
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
    sex = models.CharField(choices=SEX, max_length=50)
    age = models.IntegerField(null=False)
    civil_status = models.CharField(choices=CIVIL_STATUS, max_length=50)
    profession = models.CharField(max_length=100, null=True)
    nb_child = models.IntegerField(null=True)
    blood_group = models.CharField(choices=GROUPE_SANGUIN, null=True, max_length=50)
    clinical_case = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class TraitementEnCours(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=False)
    transmission_mode = models.CharField(max_length=100)
    start_time = models.DateField(null=False)
    observation = models.TextField(blank=True)
    efficiency = models.CharField(max_length=50, null=True)
    clinical_case = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
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
    physical_diagnosis = models.CharField(max_length=50, choices=DIAGNOSTIC_PHYSIQUE)
    result = models.TextField(blank=False)
    file = models.FileField(null=True)
    clinical_case = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Examen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(blank=False)
    result = models.TextField(blank=False)
    clinical_case = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class ExamenPhysique(Examen):
    anatomy = models.CharField(max_length=50)
    type_result = models.CharField(max_length=50, null=True)

class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(null=False)
    exam = models.ForeignKey(Examen, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class TypeParametre(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    unit = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return self.name + " en " + self.unit
class ParametreMedical(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True)
    type_parameter = models.ForeignKey(TypeParametre, on_delete=models.CASCADE, null=False)
    clinical_case = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

    def __str__(self):
        return self.type_parameter.name + " = " + self.value + " " + self.type_parameter.unit

class ModeVie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    water_quality = models.CharField(max_length=50, null=True)
    mosquito = models.BooleanField(null=False)
    pet_company = models.CharField(max_length=50, null=True)
    clinical_case = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class ActivitePhysique(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    life_style = models.ForeignKey(ModeVie, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Addiction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    duration = models.CharField(max_length=50, null=True)
    start = models.DateField(null=True)
    life_style = models.ForeignKey(ModeVie, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Voyage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    duration = models.CharField(max_length=50, null=True)
    life_style = models.ForeignKey(ModeVie, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Symptome(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    localisation = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100, null=True)
    start_time = models.DateField(null=True)
    evolution = models.CharField(max_length=150)
    triggering_activity = models.CharField(max_length=100)
    clinical_case = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class DescriptionSymptome(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    degree = models.CharField(max_length=100)
    physiological_function = models.CharField(max_length=100)
    symptom = models.ForeignKey(Symptome, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Concept(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    clinical_case = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class AntecedentMedical(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    family_antecedents = models.CharField(max_length=100)
    clinical_case = models.ForeignKey(CasClinique, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class AntecedentObstetrical(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nb_pregnancy = models.IntegerField()
    date_of_last_pregnancy = models.DateField(null=True)
    medical_antecedent = models.ForeignKey(AntecedentMedical, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Chirurgie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    date = models.DateField(null=True)
    medical_antecedent = models.ForeignKey(AntecedentMedical, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Allergie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manifestation = models.TextField(blank=False)
    trigger = models.CharField(max_length=200, null=True)
    medical_antecedent = models.ForeignKey(AntecedentMedical, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Traitement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=150 ,null=True)
    posology = models.TextField(blank=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)

class Maladie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    start_time = models.DateField(null=True)
    end_time = models.DateField(null=True)
    observation = models.TextField(blank=True)
    medical_antecedent = models.ForeignKey(AntecedentMedical, on_delete=models.CASCADE, null=False)
    treatment = models.ForeignKey(Traitement, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    deleted_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now_add=True)