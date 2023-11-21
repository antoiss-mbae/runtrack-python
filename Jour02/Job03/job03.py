# Boucle parcourant les nombres de 0 à 100 inclus
for nombre in range(101):
    # Vérification si le nombre est différent de 26, 37, et 88
    if nombre not in [26, 37, 88]:
        print(nombre)
