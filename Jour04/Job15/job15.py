def arrondir_nombre(nombre):
    partie_entiere = int(nombre)
    partie_fractionnaire = nombre - partie_entiere

    # Arrondir à la partie entière ou à la partie entière + 1
    if partie_fractionnaire >= 0.5:
        return partie_entiere + 1
    else:
        return partie_entiere

def tri_selection(liste):
    n = len(liste)

    for i in range(n - 1):
        indice_min = i
        for j in range(i + 1, n):
            if liste[j] < liste[indice_min]:
                indice_min = j

        # Échanger les éléments
        liste[i], liste[indice_min] = liste[indice_min], liste[i]

# Liste donnée
liste_nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondir les nombres dans la liste
liste_arrondie = [arrondir_nombre(nombre) for nombre in liste_nombres]

# Trier la liste arrondie
tri_selection(liste_arrondie)

# Afficher le résultat
print("Liste arrondie et triée :", liste_arrondie)
