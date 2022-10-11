# Gestion_Bibliothèque

## À propos du projet 

  > Le projet  que nous avons choisi est gestion d’une bibliothèque. Ce  projet  est une application web permettant d’automatiser tout le processus qui       était fait manuellement au sein de la bibliothèque. Grâce à cette application le bibliothécaire gagne en efficacité et performance dans sa gestion de     la bibliothèque. 
    Cette application a pour but de permettre au bibliothécaire de :
      • s’inscrire, s’identifier ou se déconnecter
      • créer, afficher, mise à jour et supprimer les livres, les inscrits et les emprunts
      • effectuer de rechercher  la liste des livres
      • obtenir des statistiques relatives aux opérations et stocks

## Construire Avec

  >Python
  Django 
  HTML5
  Oracle 19.c

## Conditions préalable

  > Python > 3.7 et oracle 19.c doivent être installés.

## Installation & exécution 

  > Créer le répertoire en y clonant le projet à l'intérieur avec la commande:
  ```
    git clone https://github.com/Souleymane12345/Gestion_bibliotheque.git 
  ```
 > Décompresser le fichier au sein reportoir (pas forcément le même répertoire). 
  
 > Créer un environnement virtuel au sein du  répertoire ou le fichier est décompressé:
  ```
    pip install virtualen (Windows)
    virtualenv name (Windows)
  ```
 > Activer l'environnement virtuel:
  ```
    name\Scripts\activate(Windows)
  ```
 > Installer les bibliothèques nécessaires:
  ```
    pip install -r requirements.txt
  ```
 > Configurer la connexion à la base de données oracle au niveau du settings.py:
  ```
    DATABASES = {
      'default': {
           'ENGINE': 'django.db.backends.oracle',
           'NAME': 'db_name',
           'USER': 'username',
           'PASSWORD': 'password',
      }
    }
  ```
 > Effectuer les migrations:
  ```
    python manage.py makemigrations
    python manage.py migrate
  ```
 > Créer un super utilisateur: 
  ```
    python manage.py createsuperuser
    Username: username
    Password: password
    Password(again): password
  ```
 > Lancer le projet: 
  ```
    python manage.py runserver 8080
  ```
## Usage 

  > Connection à la page connexion (côté administrateur et utilisateur) avec les identifiants du super utilisateur.
  ```
  http://localhost:8080/bib/
  ```
  
  Insertion de données 
    Pour les insertion vous pouvez utiliser les requêtes sql dans le fichier 4_Insertion_lignes_Dabone_Souleymane.sql ou les efféctuées depuis la page d'administration.
    ```
    http://127.0.0.1:8080/admin
    ```
    
  Le fonctionnement l'application étant basé en majeure partie sur des api réalisées en local . Vous devez installer l'extension.. au niveau de chrome     pour faire fonctionner ses api.

## Résultats 

  Capture d'écran 

![mo](https://user-images.githubusercontent.com/62396414/189772238-4ba64f59-54c2-4775-b5bb-fa865016231e.png)
![mld](https://user-images.githubusercontent.com/62396414/189772264-17b6e119-21c8-439f-855b-ecc30b7f6214.png)

![admin](https://user-images.githubusercontent.com/62396414/189772002-6c8b8055-a246-48c9-82c4-e53c55f4554a.png)
![p1](https://user-images.githubusercontent.com/62396414/189772066-1ce7da1d-1e27-4916-bf87-b95ede4f2f7d.png)
![pa1](https://user-images.githubusercontent.com/62396414/189772094-79e4b421-26bd-4fba-96e7-e61bbca7824f.png)
![pl](https://user-images.githubusercontent.com/62396414/189772113-9c3e57c1-ef58-4d46-b688-ce62c373d1a5.png)
![pv](https://user-images.githubusercontent.com/62396414/189772138-8e759693-e422-4747-8032-c5fade283ca4.png)
![po](https://user-images.githubusercontent.com/62396414/189772156-3eae8d81-6167-49ab-b120-e02babcd23be.png)
![pr](https://user-images.githubusercontent.com/62396414/189772171-2a929ccb-894e-4bb7-be17-b931f31592ab.png)
![ps](https://user-images.githubusercontent.com/62396414/189772191-b269f7f5-2247-4790-b71f-98dc2ded0f8f.png)


  Vidéo demo
