# Fonction pour afficher à l'envers utiliser def pour declarer la fontion et le slicing pour pour lire dans le sens inverse.
def afficher_alphabet_a_lenvers():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_envers = alphabet[::-1]
    print(alphabet_envers)

#pour appeller la fonction
afficher_alphabet_a_lenvers()