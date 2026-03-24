try:
    grad = int(input("Gib eine beliebige Temperatur ein: "))

    if grad < 0:
        print("Es friert")
    else:
        print("Kein Frost")

except ValueError:
    print("Gib eine gültige Zahl ein.")