# Saisie de la chaîne de caractères depuis l'utilisateur
chaine = input("Entrez une chaîne de caractères : ")

# Vérification si la chaîne contient le caractère "e"
contient_e = 'e' in chaine.lower()  # Utilisation de lower() pour traiter les majuscules et minuscules de manière équivalente

# Affichage du résultat
if contient_e:
    print("La chaîne contient le caractère 'e'.")
else:
    print("La chaîne ne contient pas le caractère 'e'.")
