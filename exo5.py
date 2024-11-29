def calculer_salaire(heures_travaillees, salaire_horaire):
    # Initialisation du salaire
    salaire = 0

    # Si les heures travaillées sont inférieures ou égales à 160
    if heures_travaillees <= 160:
        salaire = heures_travaillees * salaire_horaire
    # Si les heures travaillées sont entre 161 et 200
    elif heures_travaillees <= 200:
        salaire = 160 * salaire_horaire  # Salaire pour les 160 premières heures
        heures_supplementaires = heures_travaillees - 160
        salaire += heures_supplementaires * salaire_horaire * 1.25  # Majoration de 25% pour les heures entre 161 et 200
    # Si les heures travaillées sont supérieures à 200
    else:
        salaire = 160 * salaire_horaire  # Salaire pour les 160 premières heures
        salaire += 40 * salaire_horaire * 1.25  # Majoration de 25% pour les heures entre 161 et 200
        heures_supplementaires = heures_travaillees - 200
        salaire += heures_supplementaires * salaire_horaire * 1.5  # Majoration de 50% pour les heures après 200

    return salaire

# Demander à l'utilisateur le nombre d'heures travaillées et le salaire horaire
heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

# Calcul du salaire
salaire = calculer_salaire(heures_travaillees, salaire_horaire)

# Affichage du résultat
print(f"Le salaire pour {heures_travaillees} heures travaillées est : {salaire:.2f} euros.")