# Créé par beytu, le 22/02/2024 en Python 3.7

import csv
import mains
import time
import os
os.system('cls' if os.name == 'nt' else 'clear')
os.system("color 6")
print("Bienvenue dans l'outil de traitement de données dans le répertoire de série dans lequel vous pourrez avoir plusieurs choix")
#time.sleep(4)
info = ["0;Nom de la série;Genre;Date de sortie;Auteur;Nombre d'acteur;Etat;Avis;Liste des acteurs;Recommandation;Nombre de saison;Nombre d'épisode;Liste des saisons+épisode par saison;Durée des épisodes de chaque saison en moyenne"]
table =mains.lecture_fichier("RdS.csv")
if info in table:
    print("")
else:
    mains.initializationu_csv("RdS.csv")
while True:
    os.system("color 6")
    choix = mains.menu()
    if choix == "0":
        print("Merci pour votre utilisation !")
        os.system("color 7")
        #time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    if choix == "1":
        os.system("color A")
        mains.ajouter_donnees_csv("RdS.csv")
    if choix == "2":
        os.system("color B")
        choi = mains.getinformation()
        if choi =="2" or choi == "4":
            os.system("color 7")
            break
    if choix == "3":
        os.system("color 9")
        if mains.modification() == "":
            break
    if choix == "4":
        os.system("color 4")
        mains.erasing_data_CSV()