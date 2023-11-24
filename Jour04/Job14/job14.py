def my_long_word(longueur_minimale, texte):
    mots = []
    mot_actuel = ""

    for caractere in texte:
        if caractere.isalpha():
            mot_actuel += caractere
        elif mot_actuel:
            if len(mot_actuel) > longueur_minimale:
                mots.append(mot_actuel)
            mot_actuel = ""

    # Ajouter le dernier mot si sa longueur est suffisante
    if mot_actuel and len(mot_actuel) > longueur_minimale:
        mots.append(mot_actuel)

    return " ".join(mots)

# Exemple d'utilisation
longueur_minimale = 3
texte_exemple = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

# Appeler la fonction et afficher le résultat
resultat = my_long_word(longueur_minimale, texte_exemple)
print("Output :", resultat)
