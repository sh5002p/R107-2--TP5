def est_palindrome(chaine):
    # Conversion de la chaîne en minuscules
    chaine = chaine.lower()

    # Retirer les caractères non alphabétiques
    chaine_epuree = ''.join([c for c in chaine if c.isalpha()])

    # Vérification si la chaîne épurée est un palindrome
    if chaine_epuree == chaine_epuree[::-1]:
        return True
    else:
        return False


# Lecture de la chaîne entrée par l'utilisateur
chaine = input("Entrez un mot ou une phrase : ")

# Test si la chaîne est un palindrome
if est_palindrome(chaine):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")