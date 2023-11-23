def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:  # Éviter la division par zéro
            return num1 / num2
        else:
            return "Division by zero is undefined"
    elif operator == "%":
        if num2 != 0:  # Éviter le modulo par zéro
            return num1 % num2
        else:
            return "Modulo by zero is undefined"
    else:
        return "Invalid operator"

# Exemples d'appels de la fonction
result1 = calcule(5, "+", 3)
result2 = calcule(10, "*", 2)
result3 = calcule(8, "/", 2)

# Affichage des résultats
print(result1)
print(result2)
print(result3)
