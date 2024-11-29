import os.path
import datetime

# Fonction pour obtenir la taille d'un fichier
def obtenir_taille(fichier):
    if os.path.isfile(fichier):
        return os.path.getsize(fichier)  # Renvoie la taille en octets
    else:
        return None

# Fonction pour obtenir la date de dernière modification
def obtenir_date_modification(fichier):
    if os.path.isfile(fichier):
        timestamp = os.path.getmtime(fichier)  # Récupère le timestamp de dernière modification
        return datetime.datetime.fromtimestamp(timestamp)  # Formate en date lisible
    else:
        return None

# Demande à l'utilisateur de saisir les noms des fichiers
fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du second fichier : ")

# Vérifie l'existence des fichiers et affiche les informations
if os.path.isfile(fichier1):
    taille1 = obtenir_taille(fichier1)
    date_modif1 = obtenir_date_modification(fichier1)
    print(f"Le fichier {fichier1} existe.")
    print(f"Sa taille est : {taille1} octets.")
    print(f"Date de dernière modification : {date_modif1}")
else:
    print(f"Le fichier {fichier1} n'existe pas.")

if os.path.isfile(fichier2):
    taille2 = obtenir_taille(fichier2)
    date_modif2 = obtenir_date_modification(fichier2)
    print(f"Le fichier {fichier2} existe.")
    print(f"Sa taille est : {taille2} octets.")
    print(f"Date de dernière modification : {date_modif2}")
else:
    print(f"Le fichier {fichier2} n'existe pas.")

# Comparaison des dates de modification pour déterminer le fichier le plus récent
if os.path.isfile(fichier1) and os.path.isfile(fichier2):
    if date_modif1 > date_modif2:
        print(f"Le fichier {fichier1} est le plus récent.")
    elif date_modif1 < date_modif2:
        print(f"Le fichier {fichier2} est le plus récent.")
    else:
        print("Les deux fichiers ont été modifiés en même temps.")