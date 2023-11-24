# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Filtrer les valeurs dans l'intervalle [25, 90]
valeurs_filtrees = [valeur for valeur in L if 25 <= valeur <= 90]

# Calculer le produit des valeurs filtrées
produit = 1
for valeur in valeurs_filtrees:
    produit *= valeur

# Afficher le résultat
print(f"Le produit des valeurs dans l'intervalle [25, 90] est : {produit}")
