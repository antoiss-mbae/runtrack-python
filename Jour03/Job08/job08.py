def afficher_aliments(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("Artichaut, aubergine, navet")
    else:
        print("Combinaison type et saison non prise en charge")

# Appels de la fonction avec des paramètres différents
afficher_aliments("fruits", "hiver")
afficher_aliments("fruits", "ete")
afficher_aliments("legume", "hiver")
afficher_aliments("legume", "ete")
