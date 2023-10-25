# Erstelle eine Liste von Tupeln mit Studentennamen und -noten
studenten = [("Andreas", 92), ("Pablo", 88), ("Dennis", 95), ("Abi", 78), ("Evelyn", 97)]

# Sortiere die Liste der Studenten nach ihren Noten in absteigender Reihenfolge
# Verwende die sorted-Funktion und die key-Funktion, um die Sortierreihenfolge nach den Noten festzulegen
# Mit lambda x: x[1] wird jedes Tupel in der Liste nach dem zweiten Element (der Note) sortiert
# Mit reverse=True wird die Sortierung in absteigender Reihenfolge durchgeführt
sortierte_studenten = sorted(studenten, key=lambda x: x[1], reverse=True)

# Gib die besten drei Studenten aus
# Die Schleife durchläuft die ersten drei Elemente der sortierten Liste und gibt Namen und Noten aus
print("Die besten drei Studenten sind:")
for i, (name, note) in enumerate(sortierte_studenten[:3], start=1):
    print(f"{i}. {name}: {note} Punkte")
