# ProjetTestUnitaire
Projet commun

Ce projet de fin d'étude a pour but de solidifier des connaissances vues tout au long de l'annéeS. Ici, l'objectif est de créer un site web, dont la base de données est alimentée par un fichier CSV, et qui affiche un rapport statistique dudit fichier. 

Les technologies que nous avons choisis sont les suivantes : 
  - Front-End : HTML/CSS 
      - IDE : Visual Studio  
  - Back-End : Javascript
      - IDE : Visual Studio
  - Base de données : PostGreSQL
  - Scraping de données/interroger le fichier : Python/Scala
      - IDE : Jupyter Notebook/Intellij


https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/


# How to Launch the project 
# Sans Docker
pip install pandas
pip freeze | grep -i pandas
pip install -r -requirements.txt
python app.py


# Avec Docker
docker build -f Dockerfile -t myapppython .
docker compose up
docker compose up --build

# Regarder le port 
sudo lsof -i :5000 

Recherche d'historique de commande  : Ctrl + R

### Lancer le projet
```
python app.py
```

or
```
docker compose up
```
