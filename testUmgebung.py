def tageszeit(name, zeit):

    begruessungen = {
            "morgens": "Guten Morgen",
            "mittags": "Guten Tag",
            "abends": "Guten Abend"
        }

    gruss = begruessungen.get(zeit.lower())
    
    if gruss:
        print(f"{gruss}, {name}.")
    else:
        print("Ungültige Eingabe.")

tageszeit(input("Wie heißt du?\n"), input("Ist es grad morgens, mittags oder abends?\n"))