import csv
import time
import os
def lecture_fichier(nom_fichier):
    with open(nom_fichier, newline='', encoding='latin-1') as fichier_ouvert:
        return list(csv.reader(fichier_ouvert, delimiter=","))

table  =lecture_fichier("RdS.csv")

def initializationu_csv(mein_file):
    organi =["0","Nom de la série","Genre","Date de sortie","Auteur","Nombre d'acteur","Etat","Avis","Liste des acteurs","Recommandation", "Nombre de saison", "Nombre d'épisode", "Liste des saisons+épisode par saison", "Durée des épisodes de chaque saison en moyenne"]
    with open(mein_file, 'a', newline='') as file:
        write = csv.writer(file, delimiter=';')
        write.writerow(organi)
    return

def ajouter_donnees_csv(nom_fichier):
    while True:
        bok =lecture_fichier("RdS.csv")
        print("Veuillez inscrire les informations suivants de la série ou appuyer sur 'Entrer' pour abandonner le processus ou marquez '?' si vous ne savez pas l'information de la série ou 'abd' pour recommencer le processus: \n")
        while True:
            o = []
            infosseries = ['Nom de la série : ', 'Genre : ', 'Date de sortie : ', 'Auteur : ', "Nombre d'acteurs : ", 'Etat : ', 'Avis : ', 'Liste des acteurs : ', 'Recommandation : ', 'Nombre de saison : ', "Nombre d'épisode : ", 'Liste des saisons+épisode par saison (1er saison:liste des épisodes ; 2eme....) : ', "Durée des épisodes de chaque saison en moyenne(1er saisons =...h...min,2eme...) :"]
            for i in infosseries :
                p = input(i)
                if p == "":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                if p == "abd":
                    break
                o.append(p)
            if p == "abd":
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            o.insert(0, str(len(bok)))
            with open(nom_fichier, 'a', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(o)
            print('\n Voici les informations de votre nouvelle série inscrite dans le répertoire : ', o)
            #time.sleep(5)
            entrer = input("\n Voulez-vous continuer d'ajouter une nouvelle série ('oui' ou 'non') ? ")
            if entrer == "non":
                os.system('cls' if os.name == 'nt' else 'clear')
                return
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                break

def menu():
    print("\n Voici les choix disponibles dans votre répertoire de 0 à 4`:\n\n 0 Quitter\n 1 Inscrire une série dans le fichier\n 2 Afficher les infos d'une série\n 3 Modifier\n 4 Supprimer")
    #time.sleep(3)
    choice = input("\n Saisissez en une :")
    os.system('cls' if os.name == 'nt' else 'clear')
    return choice

def getinformation():
    l = lecture_fichier("RdS.csv")
    fail = 0
    v = []
    num = []
    for i in l:
        h = i[0].split(";")
        v.append(h)
    for i in v:
        num.append(i[0])
    while True:
        print("Souhaitez vous: \n 1 Choisir une série à afficher \n 2 Afficher tous les série en fonction de la catégorie\n 3 Revenir dans le menu \n 4 Quitter le programme")
        #time.sleep(3)
        choices = input("\n Saisissez le ci dessous : ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if choices == "1":
            while True:
                error = 0
                special = input("Voulez-vous faire une rechercher de la série (entrer 'recherche') ou le chercher par vous-mêmes (entrer 'myself') ou appuyer sur 'Entrer' pour annuler le processus ? : ")
                while True:
                    if special == '':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return
                    if special == 'myself':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    elif special == 'recherche':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    else:
                        error +=1
                        if error == 3:
                            error = 0
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Voulez-vous faire une rechercher de la série (entrer 'recherche') ou le chercher par vous-mêmes (entrer 'myself') ou appuyer sur 'Entrer' pour annuler le processus ? ")
                            special = input("\n Désolé, votre choix n'est pas correct ou n'existe pas, veuillez réssayer :  ")
                        else:
                            special = input("\n Désolé, votre choix n'est pas correct ou n'existe pas, veuillez réssayer :  ")
                while True :
                    if special == 'myself':
                        print("Choisissez une série dans laquelle vous souhaiterez obtenir ses informations (ou appuyer sur 'Entrer' pour revenir dans le menu d'affichage d'information) ")
                        for m in l[1:]:
                            print(m[0][0],"-->", m[0][2])
                        #time.sleep(2)
                        i = input("----> ")
                        if i == "":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                        while True:
                            if i not in num[1:]:
                                fail +=1
                                if fail == 3:
                                    fail = 0
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Choisissez une série dans laquelle vous souhaiterez obtenir ses informations (ou appuyer sur 'Entrer' pour revenir dans le menu) ")
                                    for m in l[1:]:
                                        print(m[0][0],"-->", m[0][2])
                                    print("\n Désolé, le numéro de série n'existe pas")
                                    i = input("\n ----> ")
                                else:
                                    print("\n Désolé, le numéro de série n'existe pas")
                                    i = input("\n ----> ")
                            else:
                                break
                        #time.sleep(1)
                        if i == '':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                        else:
                            mm = l[int(i)][0].split(";")
                            ement = l[0][0].split(";")
                            print("\n Voici les informations de la série sélectionnée :","\n",)
                            for k in range(1,len(ement)):
                                print(ement[k], " : ", mm[k])
                        #time.sleep(3)
                        fin = input("\n Voulez-vous continuer votre recherche par catégorie ('oui' ou 'non')  ou choisir une autre option d'affichage d'informations ('other') ? : ")
                        if fin == 'non':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            return
                        if fin == 'other' or fin == 'oui':
                            break
                    if special == 'recherche':
                        i = recherche()
                        if i == '':
                            break
                        mm = l[int(i)][0].split(";")
                        ement = l[0][0].split(";")
                        print("\n Voici les informations de la série sélectionnée :","\n",)
                        for k in range(1,len(ement)):
                            print(ement[k], " : ", mm[k])
                        fin = input("\n Voulez-vous continuer votre recherche d'une des séries disponibles dans le répertoire ('oui' ou 'non')  ou choisir une autre option d'affichage d'informations ('other') ? : ")
                        if fin == 'non':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            return
                        if fin == 'other' or fin == 'oui':
                            break
                if i == '':
                    break
                if fin == 'other':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                os.system('cls' if os.name == 'nt' else 'clear')
        if choices == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            while True:
                print("Saisissez soit : ")
                #time.sleep(2)
                catégorie1 = ['- Genre ', '- Date de sortie ', '- Auteur ', "- Nombre d'acteurs ", '- Etat ', '- Avis ', '- Liste des acteurs ', '- Recommandation ', '- Nombre de saison ', "- Nombre d'épisode ", '- Liste des saisons+épisode par saison ', "- Durée des épisodes de chaque saison en moyenne "]
                catégorie2 = ['Genre', 'Date de sortie', 'Auteur', "Nombre d'acteurs", 'Etat', 'Avis', 'Liste des acteurs', '- Recommandation ', 'Nombre de saison', "Nombre d'épisode", 'Liste des saisons+épisode par saison', "Durée des épisodes de chaque saison en moyenne"]
                for i in catégorie1:
                    time.sleep(0.07)
                    print(i)
                print("\n ou bien : \n 1 Revenir dans le menu \n 2 Quitter le programme \n 3 Revenir dans le menu pour l'affichage d'information")
                #time.sleep(2)
                catégorie = input("\n Veuillez le saisir ci dessous : ")
                while True :
                    if catégorie == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return
                    if catégorie == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return catégorie
                    if catégorie == "3":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return
                    if catégorie in catégorie2:
                        break
                    else:
                        catégorie = input("\n Désolé, cette catégorie n'exista pas, veuillez réssayer : ")
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n Veuillez saisir le/la", catégorie, " ou marquez 'annuler' pour annuler le processus : ")
                element = input("----> ")
                if element == 'annuler':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                while True:
                    print("\n Voici la(les) série(s) selon votre choix de la catégorie :")
                    v = []
                    for i in l:
                        h = i[0].split(";")
                        v.append(h)
                    g= []
                    for j in v[0:]:
                        if element == j[v[0].index(catégorie)]:
                            print(j)
                            g.append(j)
                    if len(g) == 0:
                        print("Je suis désolé, la catégorie d'une des séries n'existe pas")
                        print("\n Veuillez resaisir un/une autre", catégorie, " : ")
                        element = input("----> ")
                    if len(g) > 0:
                        break
                if len(g) > 1:
                    infoo = input("Voulez vous chosir une série parmi les suivants à obtenir précisemment ses informations ? ('oui' ou 'non') : ")
                    if infoo == 'oui':
                        while True:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("\n Choisissez une série parmi le filtrage de la catégorie choisi ou marquez 'annuler' pour annuler/finir le processus :\n ")
                            for j in v[0:]:
                                if element == j[v[0].index(catégorie)]:
                                    print(j)
                            numé = input("\n --->")
                            if numé == 'annuler':
                                os.system('cls' if os.name == 'nt' else 'clear')
                                return
                            hh=[]
                            for i in g:
                                if i[0][0] == numé:
                                    hh.append(i)
                            ement = l[0][0].split(";")
                            print("\n Voici les informations de la série sélectionnée : \n : ")
                            for k in range(1,len(ement)):
                                print(ement[k], " : ", hh[0][k])
                            continuer = input("\n\n Voulez-vous continuer de choisir d'autres séries ? ('oui' ou 'non' ) : ")
                            if continuer == 'non':
                                os.system('cls' if os.name == 'nt' else 'clear')
                                break
                    os.system('cls' if os.name == 'nt' else 'clear')
                if len(g) == 1:
                    while True:
                        infoo = input("Voulez vous obtenir précisemment ses informations ? ('oui' ou 'non') : ")
                        if infoo == 'non':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                        print("\n Voici les informations de la série sélectionnée :","\n",)
                        ement = l[0][0].split(";")
                        for k in range(1,len(ement)):
                            print(ement[k], " : ", g[0][k])
                        continuer = input("\n\n Appuyer sur 'Entrer' pour continuer ")
                        if continuer == '':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                            os.system('cls' if os.name == 'nt' else 'clear')
                #time.sleep(3)
                fin = input("\n Voulez vous continuer votre recherche par catégorie ('oui' ou 'non')  ou choisir une autre option d'affichage d'informations ('other') ? : ")
                if fin == 'non':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                if fin == 'other':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                os.system('cls' if os.name == 'nt' else 'clear')
        if choices == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            return
        if choices == "4":
            return choices
def recherche():
    z = lecture_fichier("RdS.csv")
    v = []
    num = []
    fails = 0
    tentative = 0
    for i in z:
        h = i[0].split(";")
        v.append(h)
    for i in v:
        num.append(i[0])
    recherche = input("\n Veuillez saisir un nom d'une série que vous cherchez ou appuyer sur 'Entrer' pour annuler :  ")
    while True:
        if recherche == '':
            os.system('cls' if os.name == 'nt' else 'clear')
            return recherche
        print()
        n = 0
        for i in v:
            if i[1] == recherche:
                print("\n ---> ",i)
                n+=1
        if n == 0:
            tentative +=1
            if tentative == 2:
                tentative = 0
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n Veuillez saisir un nom d'une série que vous cherchez ou appuyer sur 'Entrer' pour annuler :  ")
                print("\nResult not found")
                recherche = input("\n Veuillez réssayer ou appuyer sur 'Entrer' pour annuler :  ")
            else:
                print("\nResult not found")
        elif n != 0:
            choicc = input("\n Choisissez une série (par le numéro)  ou appuyer sur 'Entrer' pour recommencer : ")
            while True:
                if choicc == "":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    recherche = input("\n Veuillez saisir un nom d'une série que vous cherchez ou appuyer sur 'Entrer' pour annuler :  ")
                    break
                if choicc not in num:
                    fails +=1
                    if fails == 2:
                        fails =0
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("\n Choisissez une série (par le numéro)  ou appuyer sur 'Entrer' pour recommencer : ")
                        for i in v:
                            if i[1] == recherche:
                                print("\n ---> ",i)
                        choicc = input("\n Désolé, ce numéro de série n'existe pas, veuillez réesayer : ")
                    else:
                        choicc = input("\n Désolé, ce numéro de série n'existe pas, veuillez réesayer : ")
                else:
                    return choicc



def modification():
    z = lecture_fichier("RdS.csv")
    v = []
    elment = []
    num = []
    for i in z:
        h = i[0].split(";")
        v.append(h)
    for i in v[0]:
        elment.append(i)
    for i in v:
        num.append(i[0])
    while True:
        error = 0
        special = input("Voulez-vous faire une rechercher de la série (entrer 'recherche') ou le chercher par vous-mêmes (entrer 'myself') ou appuyer sur 'Entrer' pour annuler le processus ? : ")
        while True:
            if special == '':
                os.system('cls' if os.name == 'nt' else 'clear')
                return
            if special == 'myself':
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Choisissez une série auquel vous souhaitez le modifier ou appuyer sur 'Entrer' ou annuler le processus : ")
                for i in v[1:]:
                    print(i[0], "-->", i[1])
                break
            elif special == 'recherche':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                error +=1
                if error == 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    special = input("Voulez-vous faire une rechercher de la série (entrer 'recherche') ou le chercher par vous-mêmes (entrer 'myself') ou appuyer sur 'Entrer' pour annuler le processus ? : ")
                else:
                    special = input("\n Désolé, votre choix n'est pas correct ou n'existe pas, veuillez réssayer :  ")
        if special == 'myself':
            raté = 0
            while True:
                modif = input("\n ----> ")
                if modif == "":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                if modif in num:
                        print("\n Vous avez choisi la série suivante : ",z[int(modif)])
                        time.sleep(2)
                        p = input("\n Appuyer sur 'Entrer' pour continuer")
                        if p == "":
                            break
                else:
                    raté += 1
                    if raté == 2:
                        raté = 0
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Choisissez une série auquel vous souhaitez le modifier ou appuyer sur 'Entrer' ou annuler le processus : ")
                        for i in v[1:]:
                            print(i[0], "-->", i[1])
                        print("\n Désoler, ce numéro de série n'existe pas")
                        time.sleep(1)
                    else:
                        print("\n Désoler, ce numéro de série n'existe pas")
                        time.sleep(1)
        if special == 'recherche':
            while True:
                modif = recherche()
                if modif == '':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n Vous avez choisi la série suivante : ",z[int(modif)])
                time.sleep(2)
                p = input("\n Appuyer sur entrer pour continuer")
                if p == "":
                    break
        if special == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        while True:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n Que voulez vous modifier ?")
                for g in v[0][1:]:
                    print("-", g)
                    time.sleep(0.02)
                print("\n", v[int(modif)])
                modiff = input("\n Saisissez le (exemple : Nom de la série (ou bien) Genre.....) ou appuyer sur 'Entrer' pour annuler le processus : ")
                if modiff == "":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return
                while True:
                    if modiff in elment:
                        break
                    else:
                        print("\n Désolé, l'élément n'existe pas")
                        modiff = input("\n Réssayer en une autre : ")
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if modiff == "":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return
                    print("\n", v[0])
                    print("\n", v[int(modif)])
                    element = input("\n Saisissez ce que vous souhaitez remplacez par cette élément ou appuyer sur 'Entrer' pour annuler le processus ou marquez 'retour' pour revenir en arrière ou marquez '??' si l'information est inconnu : ")
                    time.sleep(2)
                    if element == "":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return
                    else:
                        print("\ Désolé, je n'ai pas compris")
                    if element == "retour":
                        break
                    else:
                        print("\ Désolé, je n'ai pas compris")
                    if element != "retour" and element != "":
                        break
                if element != "retour" and element != "":
                    break
            v[int(modif)][v[0].index(modiff)] = element
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n Voici votre modification d'un élément de la série choisi selon votre choix :\n", v[int(modif)])
            #time.sleep(3)
            contnue = input("\n Avez vous finis de modifier votre série ('oui' ou 'non') ? : ")
            if contnue == 'oui':
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                with open('RdS.csv', 'w', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                initializationu_csv("RdS.csv")
                with open("RdS.csv", 'a', newline='') as file:
                    write = csv.writer(file, delimiter=';')
                    for i in v[1:]:
                        write.writerow(i)
            os.system('cls' if os.name == 'nt' else 'clear')
        with open('RdS.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
        initializationu_csv("RdS.csv")
        with open("RdS.csv", 'a', newline='') as file:
            write = csv.writer(file, delimiter=';')
            for i in v[1:]:
                write.writerow(i)
        os.system('cls' if os.name == 'nt' else 'clear')
        #time.sleep(2)
        fin = input("\n Voulez-vous continuer à modifier des séries ('oui' ou 'non' ) ? : ")
        if fin == 'non':
            os.system('cls' if os.name == 'nt' else 'clear')
            return
        os.system('cls' if os.name == 'nt' else 'clear')

    return

def erasing_data_CSV():
    z = lecture_fichier("RdS.csv")
    v = []
    num = []
    for i in z:
        h = i[0].split(";")
        v.append(h)
    for i in v:
        num.append(i[0])
    while True:
        while True:
            error = 0
            special = input("Voulez-vous faire une rechercher de la série (entrer 'recherche') ou le chercher par vous-mêmes (entrer 'myself') ou appuyer sur 'Entrer' pour annuler le processus ? : ")
            while True:
                if special == '':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                if special == 'myself':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                elif special == 'recherche':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    error +=1
                    if error == 3:
                        error = 0
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Voulez-vous faire une rechercher de la série (entrer 'recherche') ou le chercher par vous-mêmes (entrer 'myself') ou appuyer sur 'Entrer' pour annuler le processus ? ")
                        special = input("\n Désolé, votre choix n'est pas correct ou n'existe pas, veuillez réssayer :  ")
                    else:
                        special = input("\n Désolé, votre choix n'est pas correct ou n'existe pas, veuillez réssayer :  ")
            break
        if special == 'myself':
            while True:
                print("Choisissez une série auquel vous souhaitez le supprimer ou appuyer sur 'Entrer' pour annuler le processus : ")
                for i in v[1:]:
                    print(i[0], "-->", i[1])
                modif = input("----> ")
                while True:
                    if modif == "":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        return
                    if modif in num:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    if modif not in num:
                        print("\n Désolé, ce numéro de série n'existe pas")
                        modif = input("\n Veuillez réessayer : ")
                break
        if special == 'recherche':
            modif = recherche()
            if modif == '':
                os.system('cls' if os.name == 'nt' else 'clear')
                return
        print("\n Vous avez choisi la série suivante : ",v[int(modif)])
        supp = input("\n Etes vous sûr de le supprimer ? : ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if supp == "oui":
            print("\n\nSuppresion en cours...")
            time.sleep(2)
            del v[int(modif)]
            print("\n\n\nSuppresion avec succès !")
            time.sleep(2)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        n = 0
        for i in v:
            i[0] = n
            n+=1
            #for i in v:
            #    print(i)
        os.system('cls' if os.name == 'nt' else 'clear')
        with open('RdS.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
        with open("RdS.csv", 'a', newline='') as file:
            write = csv.writer(file, delimiter=';')
            for i in v:
                write.writerow(i)
        continuer = input("\n\n\n Voulez-vous continuer à supprimer d'autres série ? (oui ou non) : ")
        if continuer == "non":
                os.system('cls' if os.name == 'nt' else 'clear')
                return
        os.system('cls' if os.name == 'nt' else 'clear')


