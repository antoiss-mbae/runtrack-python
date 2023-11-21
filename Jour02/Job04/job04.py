# Fonction de saisie sécurisée d'un entier supérieur à zéro
def saisir_entier_positif():
    while True:
        try:
            entier = int(input("Saisissez un entier supérieur à zéro : "))
            if entier > 0:
                return entier
            else:
                print("Veuillez saisir un entier supérieur à zéro.")
        except ValueError:
            print("Veuillez saisir un entier valide.")

# Saisie de N
N = saisir_entier_positif()

# Affichage des tables de multiplication de 1 à N
for i in range(1, N + 1):
    print(f"\nTable de multiplication de {i} :")
    for j in range(1, 11):
        produit = i * j
        print(f"{i} x {j} = {produit}")
