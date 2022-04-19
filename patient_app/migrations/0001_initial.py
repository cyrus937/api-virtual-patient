# Generated by Django 4.0.4 on 2022-04-19 06:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AntecedentMedical',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('antecedents_familiaux', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CasClinique',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('probleme_initial', models.TextField()),
                ('difficulte', models.CharField(choices=[('FACILE', 'FACILE'), ('MOYEN', 'MOYEN'), ('DIFFICILE', 'DIFFICILE')], max_length=50)),
                ('diagnostic_final', models.CharField(max_length=100)),
                ('systeme', models.CharField(choices=[('SYSTEME RESPIRATOIRE', 'SYSTEME RESPIRATOIRE'), ('SYSTEME CARDIOVASCULAIRE', 'SYSTEME CARDIOVASCULAIRE')], max_length=50)),
                ('specialite', models.CharField(choices=[('Généraliste', 'Généraliste'), ('Neurologiste', 'Neurologiste'), ('Gynécologue', 'Gynécologue'), ('Pédiatre', 'Pédiatre'), ('Dentiste', 'Dentiste'), ('Ophtamologue', 'Ophtamologue')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CasVirtuel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('cas_clinique', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.casclinique')),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('resultat', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('cas_clinique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.casclinique')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('commentaire', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('numero_telephone', models.CharField(default='+237 ', max_length=20, unique=True)),
                ('adresse', models.CharField(max_length=30)),
                ('ville', models.CharField(max_length=50, null=True)),
                ('cni', models.CharField(max_length=50, null=True, unique=True)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=50)),
                ('specialite', models.CharField(choices=[('Généraliste', 'Généraliste'), ('Neurologiste', 'Neurologiste'), ('Gynécologue', 'Gynécologue'), ('Pédiatre', 'Pédiatre'), ('Dentiste', 'Dentiste'), ('Ophtamologue', 'Ophtamologue')], max_length=50)),
                ('annee_de_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=150)),
                ('nationalite', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModeVie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('qualite_eau', models.CharField(max_length=50, null=True)),
                ('moustiquaire', models.BooleanField()),
                ('animal_compagnie', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('cas_clinique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.casclinique')),
            ],
        ),
        migrations.CreateModel(
            name='PatientVirtuel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=50)),
                ('etat_civil', models.CharField(choices=[('CELIBATAIRE', 'CELIBATAIRE'), ('MARIE', 'MARIE'), ('DIVORCE', 'DIVORCE')], max_length=50)),
                ('age_min', models.IntegerField(default=0)),
                ('age_max', models.IntegerField(default=0)),
                ('poids', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('modele_3D', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Traitement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('duree', models.CharField(max_length=150, null=True)),
                ('posologie', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeParametre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('unite', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExamenPhysique',
            fields=[
                ('examen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='patient_app.examen')),
                ('anatomie', models.CharField(max_length=50)),
                ('type_resultat', models.CharField(max_length=50, null=True)),
            ],
            bases=('patient_app.examen',),
        ),
        migrations.CreateModel(
            name='MedecinApprenant',
            fields=[
                ('medecin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='patient_app.medecin')),
                ('experience', models.CharField(choices=[('Debutant', 'Debutant'), ('Intermediaire', 'Intermediare'), ('Expert', 'Expert')], max_length=20)),
                ('niveau_connaissance', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, null=True)),
            ],
            bases=('patient_app.medecin',),
        ),
        migrations.CreateModel(
            name='MedecinExpert',
            fields=[
                ('medecin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='patient_app.medecin')),
                ('grade', models.CharField(choices=[('MG', 'Médecin Généraliste'), ('MS', 'Médecin Spécialiste'), ('Prof', 'Professeur')], max_length=20)),
            ],
            bases=('patient_app.medecin',),
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lieu', models.CharField(max_length=50)),
                ('frequence', models.CharField(max_length=50)),
                ('duree', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('mode_vie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.modevie')),
            ],
        ),
        migrations.CreateModel(
            name='TraitementEnCours',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('mode_transmission', models.CharField(max_length=100)),
                ('date_debut', models.DateField()),
                ('observation', models.TextField(blank=True)),
                ('efficacite', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('cas_clinique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.casclinique')),
            ],
        ),
        migrations.CreateModel(
            name='Symptome',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('localisation', models.CharField(max_length=100)),
                ('frequence', models.CharField(max_length=100)),
                ('duree', models.CharField(max_length=100, null=True)),
                ('date_debut', models.DateField(null=True)),
                ('evolution', models.CharField(max_length=150)),
                ('activite_declenchante', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('cas_clinique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.casclinique')),
            ],
        ),
        migrations.CreateModel(
            name='ParametreMedical',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('valeur', models.DecimalField(decimal_places=2, max_digits=10)),
                ('commentaire', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('cas_clinique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.casclinique')),
                ('type_parametre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.typeparametre')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fichier', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('examen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.examen')),
            ],
        ),
        migrations.CreateModel(
            name='Maladie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('date_debut', models.DateField(null=True)),
                ('date_fin', models.DateField(null=True)),
                ('observation', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('antecedent_medical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.antecedentmedical')),
                ('traitement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.traitement')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('operation', models.CharField(choices=[('UPDATE', 'UPDATE'), ('CREATE', 'CREATE'), ('DELETE', 'DELETE')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('medecin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.medecin')),
            ],
        ),
        migrations.CreateModel(
            name='InfosPersonnelles',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=50)),
                ('age', models.IntegerField()),
                ('etat_civil', models.CharField(choices=[('CELIBATAIRE', 'CELIBATAIRE'), ('MARIE', 'MARIE'), ('DIVORCE', 'DIVORCE')], max_length=50)),
                ('profession', models.CharField(max_length=100, null=True)),
                ('nbre_enfant', models.IntegerField(null=True)),
                ('groupe_sanguin', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O-')], max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('cas_clinique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.casclinique')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('FORMATIF', 'FORMATIF'), ('SOMMATIF', 'SOMMATIF')], max_length=20)),
                ('note', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('remarque', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('cas_virtuel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.casvirtuel')),
                ('feedback', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.feedback')),
                ('medecin_apprenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.medecinapprenant')),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosticPhysique',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('diagnostic_physique', models.CharField(choices=[('PALPATION', 'PALPATION'), ('OSCULTATION', 'OSCULTATION'), ('PERCUTION', 'PERCUTION'), ('INSPECTION', 'INSPECTION')], max_length=50)),
                ('resultat', models.TextField()),
                ('fichier', models.FileField(null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('cas_clinique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.casclinique')),
            ],
        ),
        migrations.CreateModel(
            name='DescriptionSymptome',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('degre', models.CharField(max_length=100)),
                ('fonction_physiologique', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('symptome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.symptome')),
            ],
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('cas_clinique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.casclinique')),
            ],
        ),
        migrations.CreateModel(
            name='Chirurgie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('antecedent_medical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.antecedentmedical')),
            ],
        ),
        migrations.AddField(
            model_name='casvirtuel',
            name='patient_virtuel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.patientvirtuel'),
        ),
        migrations.CreateModel(
            name='AntecedentObstetrical',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nbre_grossesse', models.IntegerField()),
                ('date_derniere_grossesse', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('antecedent_medical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.antecedentmedical')),
            ],
        ),
        migrations.AddField(
            model_name='antecedentmedical',
            name='cas_clinique',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.casclinique'),
        ),
        migrations.CreateModel(
            name='Allergie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('manifestation', models.TextField()),
                ('declencheur', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('antecedent_medical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.antecedentmedical')),
            ],
        ),
        migrations.CreateModel(
            name='Addiction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('frequence', models.CharField(max_length=50)),
                ('duree', models.CharField(max_length=50, null=True)),
                ('debut', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('mode_vie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.modevie')),
            ],
        ),
        migrations.CreateModel(
            name='ActivitePhysique',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('frequence', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('mode_vie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.modevie')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('reponse', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('evaluation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.evaluation')),
                ('medecin_apprenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.medecinapprenant')),
            ],
        ),
        migrations.CreateModel(
            name='Hypothese',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('evaluation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.evaluation')),
                ('medecin_apprenant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.medecinapprenant')),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='medecin_expert',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient_app.medecinexpert'),
        ),
    ]
