from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.


## DonneCommune au bibliothecaire, visiteur et auteur #### 

class DonneCommune (models.Model):
    nom = models.CharField(max_length=150, verbose_name='Non', null=True, blank=True)
    prenom = models.CharField(max_length=150, verbose_name='Prenom', null=True, blank=True)
    daNai = models.DateField(default=timezone.now, verbose_name='Date de naissance')
    daEm = models.CharField(max_length=150, verbose_name='Email', null=True, blank=True)

   
    class Meta: 
        abstract:True



class Bibliothecaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    daNai = models.DateField(default=timezone.now, verbose_name='Date de naissance')
    biAdr = models.CharField(max_length=500, verbose_name='Adresse', null=True, blank=True)
    con = models.CharField(max_length=15, verbose_name='Contact', null=True, blank=True)


class Visiteur(DonneCommune):
    viAdr = models.CharField(max_length=500, verbose_name='Adresse', null=True, blank=True)
    con = models.CharField(max_length=15, verbose_name='Contact', null=True, blank=True)
  
  

class Auteur(DonneCommune):
    con = models.CharField(max_length=15, verbose_name='Contact', null=True, blank=True)


##############################################################
class  Categorie (models.Model):
    Ca = models.CharField(max_length=150, verbose_name='Categorie', null=True, blank=True)
 
    


class Livre (models.Model):
    liCat = models.ForeignKey(Categorie, on_delete=models.SET_NULL ,blank=True, null=True,related_name='Livre')
    liTi = models.CharField(max_length=150, verbose_name='Titre', null=True, blank=True)
    liDe = models.CharField(max_length=150, verbose_name='Description', null=True, blank=True)
    liQu = models.PositiveIntegerField(verbose_name='Quantité', null=True, blank=True)

    

class Edition (models.Model):
    edNom = models.CharField(max_length=150, verbose_name='Nom de l édition', null=True, blank=True)
    


class Exemplaire (models.Model):

    CHOICES = (
        ('Emprunt', 'Emprunt'),
        ('Lecture','Lecture'),
    )

    exRef = models.CharField(max_length=150)
    exLi = models.ForeignKey(Livre, on_delete=models.SET_NULL ,blank=True, null=True,related_name='Exemplaire')
    exVi = models.ForeignKey(Visiteur, on_delete=models.SET_NULL ,blank=True, null=True,related_name='Visiteur')

    exCa = models.ForeignKey(Categorie,on_delete=models.SET_NULL, blank=True, null=True,related_name='Exemplaire')
    exEd = models.ForeignKey(Edition,on_delete=models.SET_NULL, blank=True, null=True,related_name='Exemplaire')
    exOp = models.CharField(max_length=255, choices=CHOICES, default='lecture', verbose_name='Lecture/Emprunt')
    exDb = models.DateField(default=timezone.now, verbose_name='Date de debut')
    exDf = models.DateField(default=timezone.now, verbose_name='Date de fin')



class Ecrire (models.Model):
    ecAu = models.ForeignKey(Auteur,on_delete=models.SET_NULL, blank=True, null=True,related_name='Ecrire')
    ecLi = models.ForeignKey(Livre,on_delete=models.SET_NULL, blank=True, null=True,related_name='Ecrire')
    ecCa = models.ForeignKey(Categorie,on_delete=models.SET_NULL, blank=True, null=True,related_name='Ecrire')
  
 