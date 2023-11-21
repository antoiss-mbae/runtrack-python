def est_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def type_triangle(a, b, c):
    if a == b == c:
        return "équilatéral"
    elif a == b or b == c or c == a:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
            return "rectangle isocèle"
        else:
            return "isocèle"
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return "rectangle"
    else:
        return "quelconque"

# Saisie des longueurs
a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

# Vérification s'il est possible de construire un triangle
if est_triangle(a, b, c):
    print("Il est possible de construire un triangle.")

    # Détermination du type de triangle
    type_tri = type_triangle(a, b, c)
    print(f"Le triangle est de type {type_tri}.")
else:
    print("Il n'est pas possible de construire un triangle avec ces longueurs.")
