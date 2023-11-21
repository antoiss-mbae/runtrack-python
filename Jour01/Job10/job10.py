# Initialisation des variables
montant_initial = 10000  # Montant initial de l'investissement en euros
taux_rendement_annuel = 5  # Taux de rendement annuel en pourcentage

# Calcul du gain annuel initial
gain_annuel_initial = (taux_rendement_annuel / 100) * montant_initial

# Affichage du gain annuel initial
print("Gain annuel initial :", gain_annuel_initial, "euros")

# Augmentation du capital de l'investisseur et du taux de rendement
montant_initial += 5000
taux_rendement_annuel += 2

# Calcul du nouveau gain annuel
gain_annuel_nouveau = (taux_rendement_annuel / 100) * montant_initial

# Affichage du nouveau gain annuel
print("\nNouveau gain annuel après augmentation :", gain_annuel_nouveau, "euros")

# Retrait de 10% du montant total et diminution du rendement de 1%
montant_initial -= (10 / 100) * montant_initial
taux_rendement_annuel -= 1

# Calcul du montant final de l'investissement
montant_final = montant_initial + gain_annuel_nouveau

# Affichage du montant final et du nouveau gain
print("\nMontant final de l'investissement après retrait et diminution du rendement :", montant_final, "euros")