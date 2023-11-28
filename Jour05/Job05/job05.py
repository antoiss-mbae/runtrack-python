def chiffrement_cesar(message, decalage):
    resultat = ""

    for char in message:
        if char.isalpha():
            # Gère les lettres majuscules
            if char.isupper():
                nouveau_char = chr((ord(char) - ord('A' ) + decalage) % 26 + ord('A'))
            # Gère les lettres minuscules
            else:
                nouveau_char = chr((ord(char) - ord('a' ) + decalage) % 26 + ord('a'))
        else:
            # Garde les caractères non alphabétiques inchangés
            nouveau_char = char

        resultat += nouveau_char

    return resultat

# Exemple d'utilisation
message_original = "Bonjour, Jules César!"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)

print(f"Message original: {message_original}")
print(f"Message chiffré : {message_chiffre}")
