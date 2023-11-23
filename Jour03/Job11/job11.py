def time_to_text(minutes):
    if not isinstance(minutes, int) or minutes < 0:
        print("Veuillez entrer un nombre entier positif.")
        return
    
    heures = minutes // 60
    minutes_restantes = minutes % 60

    if heures == 0:
        print(f"{minutes} minutes")
    elif heures == 1 and minutes_restantes == 0:
        print("1 heure")
    elif heures == 1:
        print(f"1 heure et {minutes_restantes} minutes")
    elif minutes_restantes == 0:
        print(f"{heures} heures")
    else:
        print(f"{heures} heures et {minutes_restantes} minutes")

# Tester la fonction avec différentes valeurs
time_to_text(75)   # 1 heure et 15 minutes
time_to_text(120)  # 2 heures
time_to_text(45)   # 45 minutes
time_to_text(-30)  # Message d'erreur
