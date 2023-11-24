def remplacer_element_par_somme(L, index):
    if index >= 1 and index < len(L) - 1:
        L[index] = L[index - 1] + L[index + 1]

# Définir la liste initiale
fruits = ["pomme", "cerise", "Mangue", "orange", "Melon"]

# Afficher la deuxième valeur de la liste
deuxieme_valeur = fruits[1]
print("Deuxième valeur de la liste :", deuxieme_valeur)

# Appeler la fonction pour remplacer L[3] par la somme des cases voisines L[2] & L[4]
remplacer_element_par_somme(fruits, 3)

# Afficher le tableau mis à jour
print("Tableau après la modification :", fruits)

# Afficher la dernière valeur de la liste
derniere_valeur = fruits[-1]
print("Dernière valeur de la liste :", derniere_valeur)
