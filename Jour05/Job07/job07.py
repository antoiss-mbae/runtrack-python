def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        if note < 40:
            # L'étudiant échoue au test, pas besoin d'arrondir
            notes_arrondies.append(note)
        else:
            # Arrondir la note aux multiples de 5 si nécessaire
            multiple_de_5_superieur = ((note + 4) // 5) * 5
            if multiple_de_5_superieur - note < 3:
                notes_arrondies.append(multiple_de_5_superieur)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

# Exemple d'utilisation
notes_eleves = [83, 72, 56, 91, 38, 67]
notes_arrondies = arrondir_notes(notes_eleves)

# Affichage des résultats
for note, note_arrondie in zip(notes_eleves, notes_arrondies):
    print(f"Note initiale : {note}, Note arrondie : {note_arrondie}")
