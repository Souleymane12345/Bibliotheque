from django.urls import path, include
from adminBib import views
from adminBib.api import visiteur
from rest_framework import routers



urlpatterns = [

	################ ACCES PAGE ###################

	path('visiteur', views.visiteur, name='visiteur'),
	path('', views.login2, name='login2'),
	path('login', views.LoginView.as_view(), name='login'),
	path('operation', views.operation, name='operation'),
	path('livre', views.livre, name='livre'),
	path('home', views.home, name='home'),
	path('recherche', views.recherche, name='recherche'),
	path('statistique', views.statistique, name='statistique'),
	path('deconnexion', views.deconnexion, name='deconnexion'),




	#################################################
						#API#

			  ######## VISITEUR ########	

	path('updateVisiteur/<int:id>', views.updateVisiteur, name='update-visiteur'),
	path('deleteVisiteur/<int:id>', views.deleteVisiteur, name='delete-visiteur'),
    path('api-view/visiteur', views.VisiteurList.as_view(),name='api-visiteur'),
	path('api-view/visiteur/<int:pk>', views.VisiteurDetail.as_view(),name='api-visiteur-id'),


			  ######## LIVRE ########	

	path('addLivre', views.addLivre,name='livre-add'),
	path('updateLivre/<int:id>', views.updateLivre, name='update-livre'),
	path('deleteLivre/<int:id>', views.deleteLivre, name='delete-livre'),
    path('api-view/livre', views.LivreList.as_view(),name='api-livre-add'),
	path('api-view/livre/<int:pk>', views.LivreDetail.as_view(),name='api-livre-id'),


			  ######## ASSOCIATION AUTEUR LIVRE ########	

	path('api-view/ecrire', views.EcrireList.as_view(),name='api-ecrire-add'),
	path('api-view/ecrire/<int:pk>', views.EcrireDetail.as_view(),name='api-ecrire-id'),

			  ######## AUTEUR ########	


	path('addAuteur', views.addAuteur,name='auteur-add'),
	path('updateAuteur/<int:id>', views.updateAuteur, name='update-auteur'),
	path('deleteAuteur/<int:id>', views.deleteAuteur, name='delete-auteur'),
    path('api-view/Auteur', views.AuteurList.as_view(),name='api-auteur-add'),
	path('api-view/Auteur/<int:pk>', views.AuteurDetail.as_view(),name='api-auteur-id'),


			  ######## OPERATION LECTURE EMPRUNT ########	

	path('updateOperation/<int:id>', views.updateOperation, name='update-operation'),
	path('deleteOperation/<int:id>', views.deleteOperation, name='delete-operation'),
	path('api-view/operation', views.ExemplaireList.as_view(),name='api-operation-add'),
	path('api-view/operation/<int:pk>', views.ExemplaireDetail.as_view(),name='api-operation-id'),



			######## RECHERCHE OPERATION LECTURE EMPRUNT ########	
	path('api-view/operation-search', views.ExemplaireFilter.as_view(),name='api-operation-search'),


				######## STATISTIQUE ########	
	path('operation-chart', views.operationChart,name='operation-chart'),
	path('statut-chart', views.operationStatut,name='statut-chart'),

]
