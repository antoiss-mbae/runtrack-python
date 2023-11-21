# Définition des variables du produit
nom_produit = "Ordinateur portable"
prix_unitaire = 1000.0
quantite_stock = 50

# Affichage des informations du produit
print("Produit :", nom_produit)
print("Prix unitaire :", prix_unitaire)
print("Quantité en stock :", quantite_stock)

# Demande à l'utilisateur de saisir la quantité à acheter
quantite_acheter = int(input("Entrez la quantité que vous souhaitez acheter : "))

# Mise à jour du stock
quantite_stock -= quantite_acheter

# Augmentation du prix en raison de l'inflation
prix_unitaire *= 1.1  # Augmentation de 10%

# Affichage des informations mises à jour
print("\nInformations mises à jour après l'achat :")
print("Produit :", nom_produit)
print("Nouveau prix unitaire (avec inflation) :", prix_unitaire)
print("Nouvelle quantité en stock :", quantite_stock)