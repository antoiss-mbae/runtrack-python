def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            # Première et dernière ligne : affiche des '-' sur toute la largeur
            print('-' * width)
        else:
            # Lignes intérieures : '|' aux extrémités et des espaces au milieu
            print('|' + ' ' * (width - 2) + '|')

# Exemple d'utilisation avec width=10 et height=3
draw_rectangle(10, 3)
