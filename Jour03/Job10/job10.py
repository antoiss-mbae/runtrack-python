def est_pair_ou_impair(nombre):
    # Vérifier si le nombre est un entier positif
    if isinstance(nombre, int) and nombre >= 0:
        # Vérifier si le nombre est pair ou impair
        if nombre % 2 == 0:
            return "Pair"
        else:
            return "Impair"
    else:
        return "Veuillez entrer un nombre entier positif."

# Tester la fonction avec différentes valeurs
nombre1 = 10
nombre2 = 7
nombre3 = 2.5  # Non entier
nombre4 = -3   # Nombre négatif

resultat1 = est_pair_ou_impair(nombre1)
resultat2 = est_pair_ou_impair(nombre2)
resultat3 = est_pair_ou_impair(nombre3)
resultat4 = est_pair_ou_impair(nombre4)

# Afficher les résultats
print(f"{nombre1} est {resultat1}.")
print(f"{nombre2} est {resultat2}.")
print(f"{nombre3} est {resultat3}.")
print(f"{nombre4} est {resultat4}.")
