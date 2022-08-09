from django.urls import path
from . import views
from adminBib.api import visiteur

urlpatterns = [

	################ ACCES PAGE ###################
	path('', views.home, name='home'),
	path('visiteur', views.visiteur, name='visiteur'),
	path('login2', views.login2, name='login2'),
	path('login_1', views.login_1, name='login_1'),
	path('emprunt', views.emprunt, name='emprunt'),
	path('livre', views.livre, name='livre'),



	#################################################
						#API#

			  ######## VISITEUR ########	

	path('create/', visiteur.add, name='add-visiteur'),
	path('all/', visiteur.view, name='view-visiteur'),
	path('update/<int:pk>/', visiteur.update, name='update-visiteur'),
	path('delete/<int:pk>/', visiteur.delete, name='delete-visiteur'),
	
	
]