def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    
    # Vérifier si l'index 2 est valide
    if len(fruits) >= 3:
        fruits.insert(2, "Mangue")
        return fruits
    else:
        print("L'index 2 n'est pas valide pour la liste actuelle.")

# Appeler la fonction et afficher le résultat
resultat_fruits = ajouter_mangue()
if resultat_fruits:
    print(resultat_fruits)
