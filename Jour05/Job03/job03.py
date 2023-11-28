def draw_triangle(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        if i == 0:
            # Première ligne : affiche '_' au centre
            print(spaces + '_')
        elif i == height - 1:
            # Dernière ligne : affiche '\' et '/' sur toute la largeur
            print('/' + '_' * (2 * i - 1) + '\\')
        else:
            # Lignes intermédiaires : affiche '\' au début, '_' au centre et '/' à la fin
            print(spaces + '/' + ' ' * (2 * i - 1) + '\\')

# Exemple d'utilisation avec une hauteur de 5
draw_triangle(5)
