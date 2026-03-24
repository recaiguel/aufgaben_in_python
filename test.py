# Variablen

# Aufgabe 1

""" 
a = "Hallo"
b = "Welt"

print(a + ' ' + b) """

# Aufgabe 2

""" 
a = "Hallo"
b = input("Wie heißt du?\n")

print(a + ' ' + b) """

# Aufgabe 3

""" 
a = 4
b = 7

ergebnisA = (a + b)
print(f"{a} + {b} = {ergebnisA}")

ergebnisB = (a - b)
print(f"{a} - {b} = {ergebnisB}")

ergebnisC = (a * b)
print(f"{a} * {b} = {ergebnisC}")

ergebnisD = (a / b)
print(f"{a} / {b} = {ergebnisD}") """

# Aufgabe 4

""" a = 8
b = 5

c = b
b = a
a = c

print(a, b) """

# Aufgabe 5

""" 
minuten = 5

sekunden = minuten * 60

print(sekunden) """

# Aufgabe 6

""" 
länge = 25
breite = 30
umfang = 2 * (länge + breite)

print(f"{umfang}qm")
 """

# Aufgabe 7

""" a = 2
b = 4
c = 6

daten = [a, b, c]

durchschnitt = sum(daten) / len(daten)

print(durchschnitt)
 """

# Aufgabe 8

""" 
a = 5

quadrierung = a * a

print(quadrierung)
 """

# 9 

""" 
km = 25
meileProKm = 0.621
kmInMeilen = km * meileProKm

print(kmInMeilen)
 """

# 10

""" 
a = 47
b = 8
remaining = a % b

print(remaining)
 """


# Funktionen

# Aufgabe 1

""" 
def meinName():

    name = input("Wie heißt du?\n")
    print(f"Hallo {name}")

meinName()
 """

# Aufgabe 2

""" 
def linie():
    print("---------------------")

linie()
 """

# Aufgabe 3

""" 
def rechteck():
    print("****************\n****************\n****************\n****************\n")

rechteck() """

# Aufgabe 4

""" 
def begruessung(vorname):

    print(f"Wilkommen, {vorname}")
    
begruessung(input("Wie heißt du?\n"))
 """

# Aufgabe 5

""" 
def altern(alter):

    print(f"In 10 Jahren bist du {alter+10} Jahre alt!\n")

try:
    altern(int(input("Wie alt bist du?\n")))
except ValueError:
    print("Bitte gib dein gültigen Alter an. Also nur ganze Zahlen!\n")
"""

# Aufgabe 6

""" 
def quadrieren(x):

    print(f"Das Quadrat von {x} ist {x*x}.")

while True:
    try:
        quadrieren(int(input("Welche Zahl möchtest du quadrieren?\n")))
    except ValueError:
        print("Bitte gib ein gültige Zahl ein.\n")
    else:
        break
"""

# Aufgabe 7

""" 
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
 """

# Aufgabe 8 

""" 
def flaecheninhalt(laenge, breite):

    print(laenge * breite)

flaecheninhalt(int(input("Länge: ")), int(input("Breite: "))) 
"""

# Aufgabe 9

""" 
def flaecheninhalt(z1, z2):

    return(z1 + z2)

flaecheninhalt(int(input("Erster Wert: ")), int(input("Zweiter Wert: ")))
 """

# Aufgabe 10

""" 
def steuer(brutto, steuersatz):

    steuerwert = brutto * (steuersatz/100)
    print(f"{brutto:.2f} €, {steuersatz:.2f} %, {steuerwert:.2f} €")

steuer(float(input("Brutto: ")), float(input("Steuersatz: ")))
 """


# Bedingte Verzweigung

# Aufgabe 1

""" 
try:
    alter = int(input("Alter: "))
    if alter >= 18:
        print("Du bist alt genug.")
    elif alter <= 0:
        print("Ungültige Eingabe!")
    else:
        print("Du bist zu jung!")
except ValueError:
    print("Ungültige Eingabe!") """

# Aufgabe 2

""" 
try:
    zahl = int(input("Gib eine Zahl ein!: "))

    if zahl > 0:
        print("Zahl ist positiv.")
    elif zahl == 0:
        print("Zahl ist null.")
    else:
        print("Zahl ist negativ")
except ValueError:
    print("Ungültige Eingabe!") 
"""

# Aufgabe 3

""" 
passwort = "srspsswrd123"

pswrdInput = input("Gib das Passwort ein.\n")

if passwort == pswrdInput:
    print("Anmeldung erfolgreich!")
else:
    print("Anmeldung fehlgeschlagen!")
 """

# Aufgabe 4

""" try:
    verfügbareNoten = [1, 2, 3, 4, 5, 6]
    note = int(input("Gib deine Note ein: "))
    
    if note in verfügbareNoten:
        if note <= 4:
            print("Prüfung bestanden!")
        else:
            print("Prüfung nicht bestanden!")
    else:
        print("Diese Note kenne ich nicht!")
except ValueError:
    print("Ungültige Eingabe!") """
    
# Aufgabe 5

""" 
try:
    grad = int(input("Gib eine beliebige Temperatur ein: "))

    if grad < 0:
        print("Es friert")
    else:
        print("Kein Frost")

except ValueError:
    print("Gib eine gültige Zahl ein.") """

# Aufgabe 6