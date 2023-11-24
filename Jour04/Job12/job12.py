def tri_selection(liste):
    n = len(liste)

    for i in range(n - 1):
        indice_min = i
        for j in range(i + 1, n):
            if liste[j] < liste[indice_min]:
                indice_min = j

        # Échanger les éléments
        liste[i], liste[indice_min] = liste[indice_min], liste[i]

# Exemple d'utilisation
ma_liste = [64, 25, 12, 22, 11]

# Afficher la liste avant le tri
print("Liste avant le tri :", ma_liste)

# Appeler la fonction pour trier la liste
tri_selection(ma_liste)

# Afficher la liste après le tri
print("Liste après le tri :", ma_liste)
