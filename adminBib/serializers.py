from django.db.models import fields
from rest_framework import serializers
from .models import *

class BibliothecaireSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Bibliothecaire
		fields = ('nom','prenom','daNai','daNai','con','biMoPas','biAdr',)

class AuteurSerializer(serializers.ModelSerializer):
	class Meta:
		model = Auteur
		fields = ('nom','prenom','daNai','daNai','con',)

class VisiteurSerializer(serializers.ModelSerializer):
	class Meta:
		model = Visiteur
		fields = ('nom','prenom','daNai','daNai','con','viAdr',)

class CategorieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categorie
		fields = ('Ca',)

class LivreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Livre
		fields = ('liCat','liCat','liCat','liQu',)

class EditionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Edition
		fields = ('edNom',)

class ExemplaireSerializer(serializers.ModelSerializer):
	class Meta:
		model = Exemplaire
		fields = ('exRef','exLi','exCa','exEd','exOp','exDb','exDf',)

class EcrireSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ecrire
		fields = ('ecAu','ecLi','ecCa',)

