produkte = [
    ("Laptop", 899.99, 4.6, True),
    ("Smartphone", 549.99, 4.2, True),
    ("Tablet", 299.99, 3.9, False),
    ("Kopfhörer", 149.99, 4.8, True),
    ("Maus", 19.99, 4.1, True),
]

# 1. Liste mit den verfügbaren Produkten erstellen
verfuegbare_produkte = [produkt[0] for produkt in produkte if produkt[3] == True]

# 2. Liste mit Produkten unter 50 Euro und Bewertung von mindestens 4 Sternen erstellen
guenstige_gute_produkte = [produkt[0] for produkt in produkte if produkt[1] < 50 and produkt[2] >= 4]

# 3. Durchschnittspreis aller Produkte berechnen
durchschnittspreis = sum(produkt[1] for produkt in produkte) / len(produkte)

# 4. Das teuerste Produkt finden
teuerstes_produkt = max(produkte, key=lambda x: x[1])

# Ergebnisse ausgeben
print("Verfügbare Produkte:", verfuegbare_produkte)
print("Günstige Produkte mit hoher Bewertung:", guenstige_gute_produkte)
print("Durchschnittspreis aller Produkte:", durchschnittspreis)
print("Teuerstes Produkt:", teuerstes_produkt[0], "Preis:", teuerstes_produkt[1])
