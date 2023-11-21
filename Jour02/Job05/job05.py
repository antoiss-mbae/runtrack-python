# Itération des nombres de 1 à 100
for nombre in range(1, 101):
    # Vérification des multiples de trois et cinq
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FizzBuzz")
    # Vérification des multiples de trois
    elif nombre % 3 == 0:
        print("Fizz")
    # Vérification des multiples de cinq
    elif nombre % 5 == 0:
        print("Buzz")
    # Affichage du nombre pour les autres cas
    else:
        print(nombre)
