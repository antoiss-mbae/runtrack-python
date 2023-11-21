chaine = "abcdefghijklmnopqrstuvwxyz"
n = 10

# Affichage de la suite pyramidale
for i in range(1, n + 1):
    espace = " " * (n - i)
    segment = chaine[:i]
    ligne = espace + segment + segment[-2::-1]
    print(ligne)
