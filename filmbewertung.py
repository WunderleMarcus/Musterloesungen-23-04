# 1. Leeres Wörterbuch für Filmbewertungen erstellen
film_bewertungen = {}

# 2. Filmtitel und Bewertungen hinzufügen
film_bewertungen = {
    "Film A": 8,
    "Film B": 7,
    "Film C": 9,
    "Film D": 6,
    "Film E": 8,
}

# 3. Funktion für durchschnittliche Bewertung
def durchschnittliche_bewertung(wörterbuch):
    # Die Funktion nimmt ein Wörterbuch als Argument und berechnet den Durchschnitt
    # der Werte (Bewertungen) in diesem Wörterbuch.
    return sum(wörterbuch.values()) / len(wörterbuch)

# 4. Funktion für den Film mit der höchsten Bewertung
def höchste_bewertung(wörterbuch):
    # Die Funktion nimmt ein Wörterbuch als Argument und gibt den Schlüssel (Filmtitel)
    # mit dem höchsten Wert (Bewertung) im Wörterbuch zurück.
    return max(wörterbuch, key=wörterbuch.get)

# 5. Funktion für Filme mit Bewertung von 6 oder höher
def filme_ab_6(wörterbuch):
    # Die Funktion nimmt ein Wörterbuch als Argument und erstellt eine Liste der Filmtitel,
    # deren Bewertung 6 oder höher ist.
    return [film for film, bewertung in wörterbuch.items() if bewertung >= 6]

# 6. Einen weiteren Film hinzufügen
film_bewertungen["Film F"] = 7

# 7. Wörterbuch ausgeben
print("Aktualisiertes Wörterbuch:", film_bewertungen)

# 8. Ergebnisse ausgeben
print("Durchschnittliche Bewertung:", durchschnittliche_bewertung(film_bewertungen))
print("Film mit höchster Bewertung:", höchste_bewertung(film_bewertungen))
print("Filme mit Bewertung von 6 oder höher:", filme_ab_6(film_bewertungen))
