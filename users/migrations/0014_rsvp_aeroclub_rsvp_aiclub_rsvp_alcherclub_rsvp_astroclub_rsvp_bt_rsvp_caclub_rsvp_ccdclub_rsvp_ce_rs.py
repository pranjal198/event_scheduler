# Generated by Django 3.2.4 on 2021-10-04 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0069_auto_20211004_1616'),
        ('users', '0013_profile_programme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rsvp_UGCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.ugclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='UGCLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='UGCLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='UGCLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_TechnicheCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.technicheclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='TechnicheCLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='TechnicheCLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='TechnicheCLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
                ('maybe', models.ManyToManyField(blank=True, related_name='Taskmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='Taskno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='Taskyes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_SWC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.swc')),
                ('maybe', models.ManyToManyField(blank=True, related_name='SWCmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='SWCno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='SWCyes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_SAILCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.sailclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='SAILCLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='SAILCLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='SAILCLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_ROBOTICSCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.roboticsclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='ROBOTICSCLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='ROBOTICSCLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='ROBOTICSCLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_PRAKRITICLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.prakriticlub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='PRAKRITICLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='PRAKRITICLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='PRAKRITICLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_PH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.ph')),
                ('maybe', models.ManyToManyField(blank=True, related_name='PHmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='PHno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='PHyes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_OTHERCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.otherclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='OTHERCLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='OTHERCLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='OTHERCLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_ME',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.me')),
                ('maybe', models.ManyToManyField(blank=True, related_name='MEmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='MEno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='MEyes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_MA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.ma')),
                ('maybe', models.ManyToManyField(blank=True, related_name='MAmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='MAno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='MAyes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_FNCCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.fncclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='FNCCLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='FNCCLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='FNCCLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_EEE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.eee')),
                ('maybe', models.ManyToManyField(blank=True, related_name='EEEmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='EEEno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='EEEyes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_EECLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.eeclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='EECLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='EECLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='EECLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_EDCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.edclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='EDCLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='EDCLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='EDCLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_ECE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.ece')),
                ('maybe', models.ManyToManyField(blank=True, related_name='ECEmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='ECEno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='ECEyes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_DES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.des')),
                ('maybe', models.ManyToManyField(blank=True, related_name='DESmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='DESno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='DESyes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_CSE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.cse')),
                ('maybe', models.ManyToManyField(blank=True, related_name='CSEmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='CSEno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='CSEyes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_CODINGCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.codingclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='CODINGCLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='CODINGCLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='CODINGCLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_CL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.cl')),
                ('maybe', models.ManyToManyField(blank=True, related_name='CLmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='CLno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='CLyes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_CH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.ch')),
                ('maybe', models.ManyToManyField(blank=True, related_name='CHmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='CHno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='CHyes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_CE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.ce')),
                ('maybe', models.ManyToManyField(blank=True, related_name='CEmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='CEno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='CEyes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_CCDCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.ccdclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='CCDCLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='CCDCLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='CCDCLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_CACLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.caclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='CACLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='CACLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='CACLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_BT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.bt')),
                ('maybe', models.ManyToManyField(blank=True, related_name='BTmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='BTno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='BTyes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_ASTROCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.astroclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='ASTROCLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='ASTROCLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='ASTROCLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_ALCHERCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.alcherclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='ALCERCLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='ALCERCLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='ALCERCLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_AICLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.aiclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='AICLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='AICLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='AICLUByes', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rsvp_AEROCLUB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.aeroclub')),
                ('maybe', models.ManyToManyField(blank=True, related_name='AEROCLUBmaybe', to='users.Profile')),
                ('no', models.ManyToManyField(blank=True, related_name='AEROCLUBno', to='users.Profile')),
                ('yes', models.ManyToManyField(blank=True, related_name='AEROCLUByes', to='users.Profile')),
            ],
        ),
    ]
