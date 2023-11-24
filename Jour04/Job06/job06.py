def echanger_premiere_et_derniere(liste):
    if len(liste) > 1:
        # Échanger les valeurs de la première et de la dernière case
        liste[0], liste[-1] = liste[-1], liste[0]

# Exemple d'utilisation
ma_liste = [1, 2, 3, 4, 5]

# Afficher la liste avant l'échange
print("Avant l'échange :", ma_liste)

# Appeler la fonction pour échanger les valeurs
echanger_premiere_et_derniere(ma_liste)

# Afficher la liste après l'échange
print("Après l'échange :", ma_liste)
