from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.


## DonneCommune au bibliothecaire, visiteur et auteur #### 


class Bibliothecaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    biNom = models.CharField(max_length=150, verbose_name='Non Bibliothecaire', null=True, blank=True)
    biPre = models.CharField(max_length=150, verbose_name='Prenom Bibliothecaire', null=True, blank=True)
    biDaEm = models.CharField(max_length=150, verbose_name='Email Bibliothecaire', null=True, blank=True)
    biDaNai = models.DateField(default=timezone.now, verbose_name='Date de naissance Bibliothecaire')
    biAdr = models.CharField(max_length=500, verbose_name='Adresse Bibliothecaire', null=True, blank=True)
    biCon = models.CharField(max_length=15, verbose_name='Contact Bibliothecaire', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure Enregistrement")
    update_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure de Modification ")


class Visiteur(models.Model):
    viNom = models.CharField(max_length=150, verbose_name='Non Visiteur', null=True, blank=True)
    viPre = models.CharField(max_length=150, verbose_name='Prenom Visiteur', null=True, blank=True)
    daNai = models.DateField(default=timezone.now, verbose_name='Date de naissance Visiteur')
    daEm = models.CharField(max_length=150, verbose_name='Email Visiteur', null=True, blank=True)
    viAdr = models.CharField(max_length=500, verbose_name='Adresse Visiteur', null=True, blank=True)
    viCon = models.CharField(max_length=15, verbose_name='Contact Visiteur', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure Enregistrement")
    update_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure de Modification ")
  
  

class Auteur(models.Model):
    auNom = models.CharField(max_length=150, verbose_name='Non Auteur', null=True, blank=True)
    auPre = models.CharField(max_length=150, verbose_name='Prenom Auteur', null=True, blank=True)
    auDaNai = models.DateField(default=timezone.now, verbose_name='Date de naissance Auteur')
    auDaEm = models.CharField(max_length=150, verbose_name='Email Auteur', null=True, blank=True)
    auCon = models.CharField(max_length=15, verbose_name='Contact Auteur', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure Enregistrement")
    update_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure de Modification ")


##############################################################
class  Categorie (models.Model):
    Ca = models.CharField(max_length=150, verbose_name='Categorie', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure Enregistrement")
    update_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure de Modification ")
 
    


class Livre (models.Model):
    liCat = models.ForeignKey(Categorie, on_delete=models.CASCADE ,blank=True, null=True,related_name='Livre')
    liTi = models.CharField(max_length=150, verbose_name='Titre', null=True, blank=True)
    liDe = models.CharField(max_length=150, verbose_name='Description', null=True, blank=True)
    liQu = models.PositiveIntegerField(verbose_name='Quantité', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure Enregistrement")
    update_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure de Modification ")

    

class Edition (models.Model):
    edNom = models.CharField(max_length=150, verbose_name='Nom de l édition', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure Enregistrement")
    update_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure de Modification ")  

class Ecrire (models.Model):
    ecAu = models.ForeignKey(Auteur,on_delete=models.CASCADE, blank=True, null=True,related_name='Ecrire')
    ecLi = models.ForeignKey(Livre,on_delete=models.CASCADE, blank=True, null=True,related_name='Ecrire')
    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure Enregistrement")
    update_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure de Modification ")

class Exemplaire (models.Model):

    CHOICES = (
        ('Emprunt', 'Emprunt'),
        ('Lecture','Lecture'),
    )

    CHOICES_STATUT = (
        ('Egare', 'Egare'),
        ('Attente','Attente'),
        ('Retour','Retour'),
        ('Lecture','Lecture'),
    )

    exRef = models.CharField(max_length=150)
    exEc = models.ForeignKey(Ecrire, on_delete=models.CASCADE ,blank=True, null=True,related_name='Exemplaire')
    exVi = models.ForeignKey(Visiteur, on_delete=models.CASCADE ,blank=True, null=True,related_name='Visiteur')
    exEd = models.ForeignKey(Edition,on_delete=models.CASCADE, blank=True, null=True,related_name='Exemplaire')
    exOp = models.CharField(max_length=255, choices=CHOICES, default='lecture', verbose_name='Opération')
    exSt = models.CharField(max_length=255, choices=CHOICES_STATUT, default='lecture', verbose_name='Statut')
    exDb = models.DateField(default=timezone.now, verbose_name='Date de debut')
    exDf = models.DateField(default=timezone.now, verbose_name='Date de fin')
    create_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure Enregistrement")
    update_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Date/Heure de Modification ")



  
 