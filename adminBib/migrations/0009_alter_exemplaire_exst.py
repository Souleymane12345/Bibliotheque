# Generated by Django 4.1 on 2022-08-19 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminBib', '0008_rename_exst_exemplaire_exst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exemplaire',
            name='exSt',
            field=models.CharField(choices=[('Egare', 'Egare'), ('Attente', 'Attente'), ('Retour', 'Retour'), ('Lecture', 'Lecture')], default='lecture', max_length=255, verbose_name='Statut'),
        ),
    ]
