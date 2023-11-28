def draw_tapis_with_diagonal(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                # Affiche 'X' sur la diagonale
                print('X', end=' ')
            else:
                # Affiche '.' ailleurs
                print('.', end=' ')
        print()  # Passer à la ligne suivante après chaque rangée

# Exemple d'utilisation avec une taille de 10
taille = 10
draw_tapis_with_diagonal(taille)
