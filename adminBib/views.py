from rest_framework import serializers,status,generics,filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action,api_view
from adminBib import serializers
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from adminBib.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def home(request):
    return render(request,'views/home.html')

@login_required
def visiteur(request):

    vis = Visiteur.objects.all()
    return render(request,'layouts/visiteur/listvisiteur.html',locals())

def login2(request):
    return render(request,'views/login.html')

@login_required
def operation(request):
    ex = Exemplaire.objects.all()
    visiteur = Visiteur.objects.all()
    ecrire = Ecrire.objects.all()
    edition = Edition.objects.all()
    return render(request,'layouts/operation/listeoperation.html',locals())

@login_required
def livre(request):
    livre = Livre.objects.all()
    auteur = Auteur.objects.all()
    ecr = Ecrire.objects.all()
    return render(request,'layouts/livre/listelivre.html',locals())

@login_required
def recherche(request):
    return render(request,'views/recherche.html')

@login_required
def statistique(request):
    livre = Livre.objects.count()
    bibliothecaire = Bibliothecaire.objects.count()
    exemplaire = Exemplaire.objects.count()
    visiteur = Visiteur.objects.count()
    return render(request,'views/statistique.html',locals())

@login_required
def deconnexion(request):
    logout(request)
    return redirect(reverse(login2))

#***************************************** LOGIN *******************************#
#*******************************************************************************************#


class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data

        loginId = data.get('loginId', None)
        loginPassword = data.get('loginPassword', None)

        user = authenticate(username=loginId, password=loginPassword)

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'views/home.html',locals())
            else:
                return render(request, 'views/login.html')
        else:
            return render(request, 'views/login.html')

#***************************************** VISITEUR *******************************#
#*******************************************************************************************#

@login_required
def updateVisiteur(request, id):
    visiteur = Visiteur.objects.get(id=id)
    return render(request, 'layouts/visiteur/updatevisteur.html',locals())

@login_required
def deleteVisiteur(request, id):
    visiteur = Visiteur.objects.get(id=id)
    return render(request, 'layouts/visiteur/deletevisiteur.html',locals())


class VisiteurList(APIView):

    @login_required
    def get(self, request, format=None):
        visiteurs_ = Visiteur.objects.all()
        serializer = serializers.VisiteurSerializer(visiteurs, many=True)
        return redirect(reverse(visiteur))

    @login_required
    def post(self, request, format=None):
        serializer = serializers.VisiteurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse(visiteur))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VisiteurDetail(APIView):
    
    @login_required
    def get(self, request, pk, format=None):
        visiteur_ = get_object_or_404(Visiteur.objects.all(), pk=pk)
        visiteur_.delete()
        return redirect(reverse(visiteur))

    @login_required
    def post(self, request, pk, format=None):
        visiteur_ = get_object_or_404(Visiteur.objects.all(), pk=pk)
        serializer = serializers.VisiteurSerializer(visiteur_, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse(visiteur))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#***************************************** ASSOCIATION AUTEUR LIVRE  ***********************************#
#*******************************************************************************************#

class EcrireList(APIView):

    @login_required
    def get(self, request, format=None):
        ecrire_ = Ecrire.objects.all()
        serializer = serializers.EcrireSerializer(ecrire_, many=True)
        return redirect(reverse(libre))

    @login_required
    def post(self, request, format=None):
        serializer = serializers.EcrireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse(livre))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EcrireDetail(APIView):

    @login_required
    def get(self, request, pk, format=None):
        ecrire_ = get_object_or_404(Ecrire.objects.all(), pk=pk)
        ecrire_.delete()
        return redirect(reverse(livre))

    @login_required
    def post(self, request, pk, format=None):
        ecrire_ = get_object_or_404(Ecrire.objects.all(), pk=pk)
        serializer = serializers.EcrireSerializer(ecrire_, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse(livre))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





#***************************************** LIVRE  ******************************************#
#*******************************************************************************************#
@login_required
def addLivre(request):
    cat = Categorie.objects.all()
    return render(request, 'layouts/livre/addlivre.html',locals())

@login_required
def updateLivre(request, id):
    cat = Categorie.objects.all()
    livre = Livre.objects.get(id=id)
    return render(request, 'layouts/livre/updatelivre.html',locals())

@login_required
def deleteLivre(request, id):
    livre = Livre.objects.get(id=id)
    return render(request, 'layouts/livre/deletelivre.html',locals())


class LivreList(APIView):

    @login_required
    def get(self, request, format=None):
        livre_ = Livre.objects.all()
        serializer = serializers.LivreSerializer(livre_, many=True)
        return redirect(reverse(livre))

    @login_required
    def post(self, request, format=None):
        serializer = serializers.LivreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse(livre))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LivreDetail(APIView):

    @login_required
    def get(self, request, pk, format=None):
        livre_ = get_object_or_404(Livre.objects.all(), pk=pk)
        livre_.delete()
        return redirect(reverse(livre))

    @login_required
    def post(self, request, pk, format=None):
        livre_ = get_object_or_404(Livre.objects.all(), pk=pk)
        serializer = serializers.LivreSerializer(livre_, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse(livre))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   




#***************************************** AUTEUR  *******************************#
#*******************************************************************************************#
@login_required
def addAuteur(request):
    return render(request, 'layouts/livre/addauteur.html',locals())

@login_required
def updateAuteur(request, id):
    auteur = Auteur.objects.get(id=id)
    return render(request, 'layouts/livre/updateauteur.html',locals())

@login_required
def deleteAuteur(request, id):
    auteur = Auteur.objects.get(id=id)
    return render(request, 'layouts/livre/deleteauteur.html',locals())


class AuteurList(APIView):

    @login_required
    def get(self, request, format=None):
        auteur_ = Auteur.objects.all()
        serializer = serializers.AuteurSerializer(auteur_, many=True)
        return redirect(reverse(libre))

    @login_required
    def post(self, request, format=None):
        serializer = serializers.AuteurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse(livre))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuteurDetail(APIView):

    @login_required
    def get(self, request, pk, format=None):
        auteur_ = get_object_or_404(Auteur.objects.all(), pk=pk)
        auteur_.delete()
        return redirect(reverse(livre))

    @login_required
    def post(self, request, pk, format=None):
        auteur_ = get_object_or_404(Auteur.objects.all(), pk=pk)
        serializer = serializers.AuteurSerializer(auteur_, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse(livre))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#***************************************** OPERATION EXEMPLAIRE ***********************************#
#*******************************************************************************************#

@login_required
def updateOperation(request, id):
    ex = Exemplaire.objects.get(id=id)
    visiteur = Visiteur.objects.all()
    ecrire = Ecrire.objects.all()
    edition = Edition.objects.all()
    return render(request,'layouts/operation/updateoperation.html',locals())

@login_required
def deleteOperation(request, id):
    ex = Exemplaire.objects.get(id=id)
    return render(request,'layouts/operation/deleteoperation.html',locals())

class ExemplaireList(APIView):

    @login_required
    def get(self, request, format=None):
        exemplaire_ = Exemplaire.objects.all()
        serializer = serializers.ExemplaireSerializer(exemplaire_, many=True)
        return redirect(reverse(operation))

    @login_required
    def post(self, request, format=None):
        serializer = serializers.ExemplaireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse(operation))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExemplaireDetail(APIView):

    @login_required
    def get(self, request, pk, format=None):
        exemplaire_ = get_object_or_404(Exemplaire.objects.all(), pk=pk)
        exemplaire_.delete()
        return redirect(reverse(operation))

    @login_required
    def post(self, request, pk, format=None):
        exemplaire_ = get_object_or_404(Exemplaire.objects.all(), pk=pk)
        serializer = serializers.ExemplaireSerializer(exemplaire_, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse(operation))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#***************************************** RECHERCHE OPERATION EXEMPLAIRE ***********************************#
#*******************************************************************************************#

class ExemplaireFilter(generics.ListCreateAPIView):
    search_fields = ['exOp','exSt']
    filter_backends = (filters.SearchFilter,)
    queryset = Exemplaire.objects.all()
    serializer_class = serializers.ExemplaireSerializer




#***************************************** STATISTIQUE ***********************************#
#*******************************************************************************************#
@login_required
def operationChart(request):
    labels = []
    data = []

    queryset = Exemplaire.objects.order_by('-exRef')
    for ex in queryset:
        labels.append(ex.exOp)
        data.append(1)

  
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

@login_required
def operationStatut(request):
    labels = []
    data = []

    queryset = Exemplaire.objects.order_by('-exRef')
    for ex in queryset:
        labels.append(ex.exSt)
        data.append(1)

  
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
