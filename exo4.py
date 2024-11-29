def decompose_somme(somme):
    # Calcul du nombre de billets de 100
    billets_100 = somme // 100
    somme -= billets_100 * 100

    # Calcul du nombre de billets de 50
    billets_50 = somme // 50
    somme -= billets_50 * 50

    # Calcul du nombre de billets de 10
    billets_10 = somme // 10
    somme -= billets_10 * 10

    # Calcul du nombre de pièces de 2
    pieces_2 = somme // 2
    somme -= pieces_2 * 2

    # Le reste est constitué de pièces de 1
    pieces_1 = somme

    return billets_100, billets_50, billets_10, pieces_2, pieces_1


# Lecture de la somme en euros
somme = int(input("Entrez une somme en euros : "))

# Décomposition de la somme
billets_100, billets_50, billets_10, pieces_2, pieces_1 = decompose_somme(somme)

# Affichage du résultat
print(
    f"{somme} euros, c'est donc {billets_100} billets de 100, {billets_50} de 50, {billets_10} de 10, {pieces_2} pièces de 2 et {pieces_1} pièce(s) de 1.")