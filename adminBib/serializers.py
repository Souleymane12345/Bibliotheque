from django.db.models import fields
from rest_framework import serializers
from .models import *

class BibliothecaireSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Bibliothecaire
		fields = '__all__'

class AuteurSerializer(serializers.ModelSerializer):
	class Meta:
		model = Auteur
		fields = '__all__'

class VisiteurSerializer(serializers.ModelSerializer):
	class Meta:
		model = Visiteur
		fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categorie
		fields = '__all__'

class LivreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Livre
		fields = '__all__'

class EditionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Edition
		fields = '__all__'

class ExemplaireSerializer(serializers.ModelSerializer):
	class Meta:
		model = Exemplaire
		fields = '__all__'

class EcrireSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ecrire
		fields = '__all__'

