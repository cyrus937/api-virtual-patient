# Generated by Django 4.0.4 on 2022-05-05 14:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalCase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('initial_problem', models.TextField()),
                ('difficulty', models.CharField(choices=[('EASY', 'EASY'), ('MEDIUM', 'MEDIUM'), ('HARD', 'HARD')], max_length=50)),
                ('final_diagnosis', models.CharField(max_length=100)),
                ('system', models.CharField(choices=[('RESPIRATORY SYSTEM', 'RESPIRATORY SYSTEM'), ('CARDIOVASCULAR SYSTEM', 'CARDIOVASCULAR SYSTEM')], max_length=50)),
                ('specialty', models.CharField(choices=[('Generalist', 'Generalist'), ('Neurologist', 'Neurologist'), ('Gynecologist', 'Gynecologist'), ('Pediatrician', 'Pediatrician'), ('Dentist', 'Dentist'), ('Ophthalmologist', 'Ophthalmologist')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(default='+237 ', max_length=20, unique=True)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50, null=True)),
                ('cni', models.CharField(max_length=50, null=True, unique=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=50)),
                ('specialty', models.CharField(choices=[('Generalist', 'Generalist'), ('Neurologist', 'Neurologist'), ('Gynecologist', 'Gynecologist'), ('Pediatrician', 'Pediatrician'), ('Dentist', 'Dentist'), ('Ophthalmologist', 'Ophthalmologist')], max_length=50)),
                ('year_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=150)),
                ('nationality', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LifeStyle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('water_quality', models.CharField(max_length=50, null=True)),
                ('mosquito', models.BooleanField()),
                ('pet_company', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clinical_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.clinicalcase')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('file', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalAntecedent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('family_antecedents', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clinical_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.clinicalcase')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=150, null=True)),
                ('posology', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeParameter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('unit', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VirtualPatient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=50)),
                ('civil_status', models.CharField(choices=[('CELIBATORY', 'CELIBATORY'), ('MARY', 'MARY'), ('DIVORCE', 'DIVORCE')], max_length=50)),
                ('min_age', models.IntegerField(default=0)),
                ('max_age', models.IntegerField(default=0)),
                ('weight', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('modele_3D', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpertPhysician',
            fields=[
                ('doctor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='patient_app.doctor')),
                ('grade', models.CharField(choices=[('GP', 'Generalist Physician'), ('SP', 'Specialist Physician'), ('Prof', 'Professor')], max_length=20)),
            ],
            bases=('patient_app.doctor',),
        ),
        migrations.CreateModel(
            name='LeanerPhysician',
            fields=[
                ('doctor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='patient_app.doctor')),
                ('experience', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], max_length=20)),
                ('knowledge_level', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, null=True)),
            ],
            bases=('patient_app.doctor',),
        ),
        migrations.CreateModel(
            name='VirtualCase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clinical_case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.clinicalcase')),
                ('virtual_patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.virtualpatient')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentInProgress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('administration_mode', models.CharField(max_length=100)),
                ('start_time', models.DateField()),
                ('observation', models.TextField(blank=True)),
                ('efficiency', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clinical_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.clinicalcase')),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=50)),
                ('frequency', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('life_style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.lifestyle')),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('localisation', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100, null=True)),
                ('evolution', models.CharField(max_length=150)),
                ('triggering_activity', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clinical_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.clinicalcase')),
            ],
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('medical_antecedent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.medicalantecedent')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalActivity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('frequency', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('life_style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.lifestyle')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=50)),
                ('age', models.IntegerField()),
                ('civil_status', models.CharField(choices=[('CELIBATORY', 'CELIBATORY'), ('MARY', 'MARY'), ('DIVORCE', 'DIVORCE')], max_length=50)),
                ('profession', models.CharField(max_length=100, null=True)),
                ('nb_child', models.IntegerField(null=True)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O-')], max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clinical_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.clinicalcase')),
            ],
        ),
        migrations.CreateModel(
            name='ObstetricalAntecedent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nb_pregnancy', models.IntegerField()),
                ('date_of_last_pregnancy', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('medical_antecedent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.medicalantecedent')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalParameter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clinical_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.clinicalcase')),
                ('type_parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.typeparameter')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('operation', models.CharField(choices=[('UPDATE', 'UPDATE'), ('CREATE', 'CREATE'), ('DELETE', 'DELETE')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('anatomy', models.CharField(max_length=50)),
                ('result', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clinical_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.clinicalcase')),
                ('file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_app.media')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('FORMATIF', 'FORMATIF'), ('SOMMATIF', 'SOMMATIF')], max_length=20)),
                ('mark', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('note', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('feedback', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.feedback')),
                ('virtual_case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.virtualcase')),
                ('learner_physician', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.leanerphysician')),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('start_time', models.DateField(null=True)),
                ('end_time', models.DateField(null=True)),
                ('observation', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('medical_antecedent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.medicalantecedent')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.treatment')),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosisPhysics',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('physical_diagnosis', models.CharField(choices=[('PALPATION', 'PALPATION'), ('OSCULTATION', 'OSCULTATION'), ('PERCUTION', 'PERCUTION'), ('INSPECTION', 'INSPECTION')], max_length=50)),
                ('result', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clinical_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.clinicalcase')),
                ('file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_app.media')),
            ],
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('clinical_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.clinicalcase')),
            ],
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('manifestation', models.TextField()),
                ('trigger', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('medical_antecedent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.medicalantecedent')),
            ],
        ),
        migrations.CreateModel(
            name='Addiction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('frequency', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('life_style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.lifestyle')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('evaluation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.evaluation')),
                ('learner_physician', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.leanerphysician')),
            ],
        ),
        migrations.CreateModel(
            name='Hypothesis',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('evaluation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.evaluation')),
                ('learner_physician', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.leanerphysician')),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='expert_physician',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.expertphysician'),
        ),
    ]
