import random

# Zufällige Zahl zwischen 1 und 20 generieren
zufallszahl = random.randint(1, 20)

# Schleife, um den Benutzer raten zu lassen
versuche = 0
while True:
    versuche += 1
    eingabe = int(input("Rate eine Zahl zwischen 1 und 20: "))
    
    if eingabe < zufallszahl:
        print("Die geratene Zahl ist zu niedrig. Versuche es erneut.")
    elif eingabe > zufallszahl:
        print("Die geratene Zahl ist zu hoch. Versuche es erneut.")
    else:
        print(f"Herzlichen Glückwunsch! Du hast die richtige Zahl ({zufallszahl}) in {versuche} Versuchen erraten.")
        break
