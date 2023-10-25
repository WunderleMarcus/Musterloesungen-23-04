def durchschnitt_schueler(noten):
    # Berechnet den Durchschnitt der Noten für einen Schüler
    if len(noten) == 0:
        return 0
    return sum(noten) / len(noten)

def durchschnitt_klasse(schueler):
    # Berechnet den Durchschnitt für die gesamte Klasse
    if len(schueler) == 0:
        return 0
    gesamtdurchschnitt = 0
    for schuel in schueler:
        gesamtdurchschnitt += durchschnitt_schueler(schuel["noten"])
    return gesamtdurchschnitt / len(schueler)

schueler = [
    {"name": "Max", "noten": [90, 85, 88, 92]},
    {"name": "Anna", "noten": [78, 92, 86, 94]},
    # Weitere Schüler hier hinzufügen
]

print("Durchschnittsnote pro Schüler:")
for schuel in schueler:
    durchschnitt = durchschnitt_schueler(schuel["noten"])
    print(f"{schuel['name']}: {durchschnitt}")

klasse_durchschnitt = durchschnitt_klasse(schueler)
print("\nDurchschnittsnote der gesamten Klasse:", klasse_durchschnitt)
