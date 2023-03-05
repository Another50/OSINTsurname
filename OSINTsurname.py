import csv

# Ouvrir le fichier contenant les données de noms de famille
with open('surname.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    # Créer un dictionnaire qui associe chaque nom de famille à son compte
    noms_comptes = {row["patronyme"].upper(): int(row["count"]) for row in reader}

# Demander à l'utilisateur les initiales en majuscules
initiales = input("Entrez les initiales : ").upper()

# Demander à l'utilisateur si la première lettre des initiales doit être la première lettre du nom de famille
premiere_lettre = input("La première lettre des initiales doit-elle être la première lettre du nom de famille ? (o/n) : ")

# Créer une liste de tous les noms de famille commençant par les initiales dans l'ordre voulu
noms_trouves = {}
for nom, count in noms_comptes.items():
    index = 0
    if premiere_lettre == "o":
        if initiales[0] != nom[0]:
            continue
        index = 1
    for initiale in initiales[index:]:
        if initiale in nom[index:]:
            index = nom.index(initiale, index) + 1
        else:
            break
    else:
        noms_trouves[nom.capitalize()] = count

# Trier les noms trouvés par ordre décroissant de compte
noms_trouves = dict(sorted(noms_trouves.items(), key=lambda item: item[1], reverse=True))

# Créer le fichier de sortie avec le nom des initiales
nom_fichier = initiales + ".txt"
with open(nom_fichier, "w") as fichier:
    # Écrire les noms de famille trouvés avec leur compte dans le fichier
    fichier.write("Noms de famille correspondants : \n")
    for nom, count in noms_trouves.items():
        fichier.write(nom + " (" + str(count) + ")\n")
print(f"le fichier {nom_fichier} viens d'être enregistrer dans le dossier !")