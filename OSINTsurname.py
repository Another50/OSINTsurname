import csv
import requests

response = requests.get('https://api.github.com/repos/Another50/OSINTsurname/releases/latest')
latest_release = response.json()

if latest_release['tag_name'] != '1.1':
    print(f'Une nouvelle version ({latest_release["tag_name"]}) est disponible !')
    print(f'Téléchargez-la ici : {latest_release["html_url"]}')

with open('surname.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    noms_comptes = {row["patronyme"].upper(): int(row["count"]) for row in reader}

initiales = input("Entrez les initiales : ").upper()

premiere_lettre = input("La première lettre des initiales doit-elle être la première lettre du nom de famille ? (o/n) : ")

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

noms_trouves = dict(sorted(noms_trouves.items(), key=lambda item: item[1], reverse=True))

nom_fichier = initiales + ".txt"
with open(nom_fichier, "w") as fichier:
    fichier.write("Noms de famille correspondants : \n")
    for nom, count in noms_trouves.items():
        fichier.write(nom + " (" + str(count) + ")\n")
print(f"le fichier {nom_fichier} viens d'être enregistrer dans le dossier !")
