from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

"""
def home(request):
    return render(request,'views/home.html')
"""

def visiteur(request):

    vis = Visiteur.objects.all()
    return render(request,'views/visiteur.html',locals())

def login2(request):
    return render(request,'views/login.html')

def emprunt(request):
    return render(request,'views/emprunt.html')

def livre(request):
    return render(request,'views/livre.html')


def login_1(request):
    if request.method == 'POST':
            loginId = request.POST['loginId']
            loginPassword = request.POST['loginPassword']
            user = authenticate(username=loginId, password=loginPassword)
            print(user)
            if user is not None:  # Si l'objet renvoyé n'est pas None
                if user.is_active:
                    login(request, user)  # nous connectons l'utilisateur
                    return render(request, 'views/home.html',locals())
                else:
                       return render(request, 'views/login.html')
            else: # sinon une erreur sera affichée
                   return render(request, 'views/login.html')
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request, 'views/login.html')

"""
def login_1(request):
    if request.POST:
        error = False
        if request.method == 'POST':
            form =  login(request.POST)
            
            if form.is_valid():
                loginEmail = form.cleaned_data["loginEmail"]
                loginPassword = form.cleaned_data["loginPassword"]
                user = authenticate(email=loginEmail, password=loginPassword)
                if user:  # Si l'objet renvoyé n'est pas None
                    if user.is_active:
                        login(request, user)  # nous connectons l'utilisateur
                        return redirect(reverse(home))
                    else:
                        error = True
                else: # sinon une erreur sera affichée
                    error = True
    else:
        form = login()

    return render(request, 'views/home.html', locals())

def delogin(request):
    logout(request)
    return redirect(reverse(login))


def login_diagnostic_form(request):
    
    if request.method == 'POST':
        email = request.POST.get('loginEmail')   
        password = request.POST.get('loginPassword')
        if Bibliothecaire.objects.filter(email = email ):       
            if  Bibliothecaire.objects.filter( password = password ):
                return render(request, 'pages_agents/login_agent.html',locals() )
            else:
                print("code incorrect")
                return render(request, 'pages_banks/login_bank.html' )
            else:
                print("Email incorrect")
                return render(request, 'pages_banks/login_bank.html' )
        #name = int(name)


        return render(request,'views/layouts/diagnostic/login.html')
"""