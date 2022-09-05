# Generated by Django 4.1 on 2022-08-18 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminBib', '0004_alter_auteur_aucon_alter_auteur_audaem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auteur',
            name='auCon',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Contact Auteur'),
        ),
        migrations.AlterField(
            model_name='auteur',
            name='auDaEm',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Email Auteur'),
        ),
        migrations.AlterField(
            model_name='auteur',
            name='auNom',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Non Auteur'),
        ),
        migrations.AlterField(
            model_name='auteur',
            name='auPre',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Prenom Auteur'),
        ),
        migrations.AlterField(
            model_name='bibliothecaire',
            name='biAdr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Adresse Bibliothecaire'),
        ),
        migrations.AlterField(
            model_name='bibliothecaire',
            name='biCon',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Contact Bibliothecaire'),
        ),
        migrations.AlterField(
            model_name='bibliothecaire',
            name='biDaEm',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Email Bibliothecaire'),
        ),
        migrations.AlterField(
            model_name='bibliothecaire',
            name='biNom',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Non Bibliothecaire'),
        ),
        migrations.AlterField(
            model_name='bibliothecaire',
            name='biPre',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Prenom Bibliothecaire'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='Ca',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Categorie'),
        ),
        migrations.AlterField(
            model_name='ecrire',
            name='ecAu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Ecrire', to='adminBib.auteur'),
        ),
        migrations.AlterField(
            model_name='ecrire',
            name='ecCa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Ecrire', to='adminBib.categorie'),
        ),
        migrations.AlterField(
            model_name='ecrire',
            name='ecLi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Ecrire', to='adminBib.livre'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='edNom',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nom de l édition'),
        ),
        migrations.AlterField(
            model_name='exemplaire',
            name='exCa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Exemplaire', to='adminBib.categorie'),
        ),
        migrations.AlterField(
            model_name='exemplaire',
            name='exEd',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Exemplaire', to='adminBib.edition'),
        ),
        migrations.AlterField(
            model_name='livre',
            name='liDe',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='livre',
            name='liQu',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Quantité'),
        ),
        migrations.AlterField(
            model_name='livre',
            name='liTi',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='visiteur',
            name='daEm',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Email Visiteur'),
        ),
        migrations.AlterField(
            model_name='visiteur',
            name='viAdr',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Adresse Visiteur'),
        ),
        migrations.AlterField(
            model_name='visiteur',
            name='viCon',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Contact Visiteur'),
        ),
        migrations.AlterField(
            model_name='visiteur',
            name='viNom',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Non Visiteur'),
        ),
        migrations.AlterField(
            model_name='visiteur',
            name='viPre',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Prenom Visiteur'),
        ),
    ]