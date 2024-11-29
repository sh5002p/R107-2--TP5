def taille_chaine(T):
    taille = 0
    while taille < len(T) and T[taille] != '\0':  # On s'arrête au caractère de fin de chaîne
        taille += 1
    return taille


def pourcentage_voyelles(T):
    voyelles = "aeiouyAEIOUY"
    nb_voyelles = 0
    taille = taille_chaine(T)

    for i in range(taille):
        if T[i] in voyelles:
            nb_voyelles += 1

    return (nb_voyelles / taille) * 100 if taille > 0 else 0


def rechercher_sous_chaine(T, sous_chaine):
    taille = taille_chaine(T)
    len_sous_chaine = len(sous_chaine)

    for i in range(taille - len_sous_chaine + 1):
        # On vérifie chaque sous-chaîne de la même longueur que "wagon"
        if ''.join(T[i:i + len_sous_chaine]) == sous_chaine:
            return i  # Retourner l'indice du début de la première occurrence
    return -1  # Retourne -1 si "wagon" n'est pas trouvé


def compter_occurrences(T, sous_chaine):
    taille = taille_chaine(T)
    len_sous_chaine = len(sous_chaine)
    count = 0

    for i in range(taille - len_sous_chaine + 1):
        if ''.join(T[i:i + len_sous_chaine]) == sous_chaine:
            count += 1

    return count


# Lecture de la chaîne de caractères de l'utilisateur
T = list(input("Entrez une chaîne de caractères : ") + '\0')  # Ajout du caractère de fin de chaîne

# Calcul de la taille de la chaîne
print(f"Taille de la chaîne : {taille_chaine(T)}")

# Calcul du pourcentage de voyelles
print(f"Pourcentage de voyelles : {pourcentage_voyelles(T):.2f}%")

# Recherche de la sous-chaîne "wagon"
sous_chaine = "wagon"
index = rechercher_sous_chaine(T, sous_chaine)
if index != -1:
    print(f"'wagon' est trouvé pour la première fois à l'indice {index}.")
else:
    print("'wagon' n'est pas trouvé.")

# Nombre d'occurrences de "wagon"
occurrences = compter_occurrences(T, sous_chaine)
print(f"Le nombre d'occurrences de 'wagon' : {occurrences}")