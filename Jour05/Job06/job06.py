def distance_to_toilettes(marches, hauteur_marche):
    # Calcul de la distance en centimètres
    distance_cm = marches * 2 * hauteur_marche
    # Conversion de la distance en mètres
    distance_m = distance_cm / 100.0
    # Calcul de la distance hebdomadaire
    distance_hebdo_m = distance_m * 5 * 2  # 5 allers-retours par jour pendant 7 jours

    return distance_hebdo_m

# Exemple d'utilisation
nombre_marches = 20
hauteur_marche = 15
resultat = distance_to_toilettes(nombre_marches, hauteur_marche)

# Affichage du résultat
print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {resultat:.2f} m par semaine.")
