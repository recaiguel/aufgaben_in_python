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

""" def stopNgo(ampel):
    signal = {
        "rot": "Stehen bleiben",
        "gelb": "Achtung",
        "grün": "Los gehts"
    }

    ampelSignal = signal.get(ampel.lower())

    if ampelSignal:
        print(ampelSignal)
    else:
        print("Ungültige Eingabe")

stopNgo(input("Was sagt die ampel?\n")) """

# Aufgabe 7

""" 
def funTageszeit(tageszeit):

    if tageszeit >= 0 and tageszeit <= 5:
        print("Nacht")
    elif tageszeit >= 6 and tageszeit <= 11:
        print("Morgen")
    elif tageszeit >= 12 and tageszeit <= 17:
        print("Nachmittag")
    elif tageszeit >= 18 and tageszeit <= 23:
        print("Abend")
    else:
        print("Ungültige Eingabe")
        
funTageszeit(int(input("Gib eine volle Uhrzeit ein: "))) """

# Aufgabe 8

""" 
def wochentag(tag):

    Wochentage = {
        1: "Montag",
        2: "Dienstag",
        3: "Mittwoch",
        4: "Donnerstag",
        5: "Freitag",
        6: "Samstag",
        7: "Sonntag",
    }

    tag = Wochentage.get(tag)

    if tag:
        print(tag)
    else:
        print("Ungültige Eingabe")

wochentag(int(input("Gib eine Zahl für ein Wochentag ein: ")))
 """

# Aufgabe 9

""" try:
    def besucher(alter):
        if alter >= 16 and alter < 18:
            print("Nur FSK16 Filme für dich!")
        elif alter >= 18:
            print("FSK18 erlaubt!")
        elif alter >= 1 and alter < 16:
            print("Du bist zu Jung für FSK16!")
        else:
            print("Gib eine gültige Zahl ein!")

    besucher(int(input("Wie alt bist du?\n\n")))
except ValueError:
    print("Gib eine gültige Zahl ein!\n") """

###############

# zwischenaufgaben

""" Zahl = 1
liste = []
while Zahl <= 10:
    neuer_wert = Zahl * Zahl
    liste.append(neuer_wert)
    Zahl += 1
print(liste)
 """

###############

""" 
meinWort = "Ananas"

count = 0

for char in meinWort.lower():
    if char == "a":
        count += 1
        
print(count)

 """

###############

""" 
arr = [4, 3, 8, 9, 10, 17, 6, 25, 8, 10]

summe = 0

for num in arr:
    summe += num
print(summe)

 """

###############

""" 
arr = [4, 3, 8, 9, 10, 17, 6, 25, 8, 10]

maxRecord = 0

for num in arr:
    if num > maxRecord:
        maxRecord = num
print(maxRecord) """


###############


# Aufgabe 10

""" 
try:
    mitglied = input("Bist du Mitglied bei uns? y/n:\n")
    try:
        if mitglied is "y":
            mitglied = True
            alter = int(input("Wie alt bist du?"))
        elif mitglied is "n":
            mitglied = False
        else:
            print("Ungültige Eingabe")
    except ValueError:
        print("Ungültige Eingabe")
except ValueError:
    print("Ungültige Eingabe")

if mitglied is True:
    print("Als Mitglied bei uns erhälst du ein Rabatt.")
    if alter < 18:
        print("Du bekommst ein Jugendrabatt.")
    else:
        print("Du bekommst ein Mitgliedsrabatt")
else:
    print("Für ein Rabatt musst du mindestens Mitglied sein!")
 """

# Algorithmische Übungen 2
# Einfache Schleifen

# 1 
""" 
i = 0
for i in range(10):
    print(i+1) 
"""

# 2

""" 
zutaten = ["Eier", "Salz", "Mehl", "Hefe"]

for i in zutaten:
    print(i)
"""

# 3

""" 
num = 10

while num > 0:
    print(num)
    num -= 1
else:
    print("Start")
 """

# 4

""" 
countdown = 5

while countdown > 0:
    print("Hallo Python")
    countdown -= 1
 """

# 5

""" 
wort = input("Gib ein Wort ein.\n")

for i in wort:
    print(i)
 """

# 6

""" 
def einmalEins(num):
    multiplier = 0

    while multiplier < 10:
        multiplier += 1
        print(num * multiplier)

einmalEins(int(input("Welche Zahl willst du multiplizieren?: ")))
 """

# 7

""" 
kosten = [2.50, 4.40, 3, 9, 2.10]

summe = 0
for i in kosten:
    summe += i
    i += 1
print(summe)
 """

# 8

""" 
def printRange(start, stop):

    for i in range(start, stop):
        print(i)
    print(stop)
printRange(int(input("Start: ")), int(input("Stop: ")))
 """

# 9

""" 
for i in range(1, 19):
    if i % 2 == 0:
        print(i)
 """

# 10

""" 
wort = input("Gib ein wort ein: ")
i = 0

for char in wort:
    i += 1
print(i)
 """


# Arrays

# 1

""" 
fruits = ["Apfel", "Banane", "Orange", "Ananas", "Erdbeere"]

print(fruits[0], fruits[2], fruits[3]) """

# 2

""" 
liste = []

liste.append("Hans")
liste.append("Jürgen")
liste.append("Peter")

print(liste)
# 3
print(len(liste))
 """

# 4

""" 
orte = ["Köln", "Düsseldorf", "Duisburg", "Essen", "Mülheim"]

orte.reverse()
print(orte)
 """

# 5 

""" 
farben = ["Grün", "Lila", "Cyan"]

farben[1] = "Blau"

print(farben) """

# 6

""" 
werte = [7, 3, 4, 0, 1, 6, 8]

werte.sort()
print(werte)
print(min(werte))
print(max(werte))
 """

# 7
""" 
werte = [7, 3, 4, 0, 1, 6, 8]

letztesWert = werte.pop()

print(letztesWert)
print(werte)
 """

# 8
""" 
werte = [7, 3, 4, 0, 1, 6, 8]

werteVerdoppelt = []

for i in werte:
    
    verdoppelung = i * 2

    werteVerdoppelt.append(verdoppelung)

print(werte)
print(werteVerdoppelt)
 """

# 9
""" 
teilnehmer = ["Hans", "Jörg", "Anna", "Bernd"]

checkIfContains = "Anna"

if checkIfContains in teilnehmer:
    print("Yes")
else:
    print("No")
 """

# 10
""" 
listeA = [1,2,3,4,5]
listeB= [6,7,8,9,10]

listeC = listeA + listeB

print(listeC)

 """

# Aufgabe aus Folie GrundlagenProgrammierung_2

""" 
multiplikationstabelle = []

for i in range(1, 6):
    row = []
    print()
    for j in range(1, 6):
        row.append(i * j)
    multiplikationstabelle.append(row)
print(multiplikationstabelle)
 """

#########################

""" damago_laptop = {
    "Prozessor": "Core i5-8350U",
    "Grafik": "Intel UHD-Graphics 620",
    "Arbeitsspeicher GB": 16,
    "Festplatte GB": 512,
    "Betriebssystem": "Windows"
}   


print(damago_laptop)
print()


damago_laptop["Betriebssystem"] = "Kali Linux"
damago_laptop["Externe SSD GB"] = 1024

print(damago_laptop)
print()

for key, value in damago_laptop.items():
    print(key,":", value) """

# Mehrdimensionale Arrays

# 1

""" matrix = []

for i in range(2):
    liste = []
    matrix.append(liste)
print(matrix)
 """

# 2

""" matrix = [
    ["Hund", "Katze", "Maus"],
    ["Haus", "Hof", "Garten"],
    ["Baum", "Blume", "Wiese"]
        ]

print(matrix[0][2]) # Maus
print(matrix[1][0]) # Haus
print(matrix[2][2]) # Wiese
print(matrix[1][2]) # Garten
 """

# 3

#Gegeben ist folgendes fehlerhaftes Mehrdimensionales Array:

""" matrix = [
    ["Schulung", "Dozent", "Teilnehmer"],
    ["PC", "Beamer", "Monitor"]
    ["Variablen", "Funktionen", "Schleifen"],
    ]
 """
#Wieso ist es fehlerhaft?
# Es fehlt ein Komma

# 4

""" matrix = [
    [4, 8],
    [9, 6]
]

matrix[1][1] = 4

print(matrix) """

# 5

""" matrix = [
    [True, False],
    [False, True]
]

matrix.append([339, "Eving"])

print(matrix)
 """


# Fortgeschrittene Schleifen

# 1

""" arr = []

onlyEvenNumbers = int(input("Gib eine Zahl ein: "))

for i in range(onlyEvenNumbers):
    if i % 2 == 0:
        arr.append(i)
print(arr) """

# 2

""" liste = [1, 2, 3, 4, 5]
zweiteListe = []

for i in liste:
    x = i * i
    zweiteListe.append(x)
print(zweiteListe) """

# 3

""" preise = [2.80, 4.70, 3.20, 6.30, 7]
preiseUmgekehrt = []

for i in range(len(preise) - 1, -1, - 1):
    preiseUmgekehrt.append(preise[i])
print(preiseUmgekehrt)
 """

# 4
""" 
zahlenreihe = [1, 7, 3, 4, 3, 6, 1, 2, 7, 3, 5, 6, 3]

count = 0
checkNum = int(input("Gib eine Zahl ein: "))

for i in range(len(zahlenreihe)):
    if checkNum == zahlenreihe[i]:
        count += 1
print(count) """

#5
""" 
werte = [4, 6, 8, 9, 10, 4, 3]

total = 0
for i in range(len(werte)):
    total += werte[i]

print(total) """

#6

