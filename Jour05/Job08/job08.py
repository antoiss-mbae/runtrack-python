def my_sort(arr):
    sorted = False  # Initialisation de la variable de tri

    # Initialisation du compteur de coups
    count = 0

    # Boucle principale pour le tri
    while not sorted:
        sorted = True  # On suppose que la liste est triée
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                # Échange des éléments adjacents
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False  # La liste n'est pas encore triée
                count += 1  # Augmentation du compteur de coups

    # Affichage du nombre total de coups nécessaires
    print(f"Nombre total de coups nécessaires pour trier la liste : {count}")

    return arr

# Exemple d'utilisation
liste_non_triee = [5, 3, 8, 1, 7, 2]
liste_triee = my_sort(liste_non_triee.copy())  # Utilisation de copy() pour ne pas modifier la liste d'origine
print("Liste triée :", liste_triee)
