def verifier_positif_negatif(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("nul")

# Appels de la fonction avec des paramètres différents
verifier_positif_negatif(5)
verifier_positif_negatif(-3)
verifier_positif_negatif(0)
