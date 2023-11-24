def afficher_deuxieme_element():
    fruits = ["pomme", "cerise", "orange"]
    
    if len(fruits) >= 2:
        deuxieme_element = fruits[1]
        print("Deuxième élément de la liste :", deuxieme_element)
    else:
        print("La liste ne contient pas suffisamment d'éléments.")

# Appeler la fonction
afficher_deuxieme_element()
