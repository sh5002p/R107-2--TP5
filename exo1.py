# Demander les informations des deux personnes
nom1 = input("Entrez le nom de la première personne : ")
prenom1 = input("Entrez le prénom de la première personne : ")

nom2 = input("Entrez le nom de la deuxième personne : ")
prenom2 = input("Entrez le prénom de la deuxième personne : ")

# Formater les noms et prénoms (première lettre du prénom en majuscule, nom en majuscule)
personne1 = f"{prenom1.capitalize()} {nom1.upper()}"
personne2 = f"{prenom2.capitalize()} {nom2.upper()}"

# Comparer les personnes en fonction du nom et éventuellement du prénom
if personne1 < personne2:
    print(personne1)
    print(personne2)
else:
    print(personne2)
    print(personne1)