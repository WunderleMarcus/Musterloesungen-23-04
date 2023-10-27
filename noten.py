mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

# 1. Durchschnittsnote berechnen
durchschnitt_mathematik = sum(mathematik) / len(mathematik)
durchschnitt_physik = sum(physik) / len(physik)
durchschnitt_chemie = sum(chemie) / len(chemie)

# 2. Beste und schlechteste Note finden
beste_mathematik = max(mathematik)
schlechteste_mathematik = min(mathematik)
beste_physik = max(physik)
schlechteste_physik = min(physik)
beste_chemie = max(chemie)
schlechteste_chemie = min(chemie)

# 3. Gesamtdurchschnittsnote berechnen
gesamtdurchschnitt = (durchschnitt_mathematik + durchschnitt_physik + durchschnitt_chemie) / 3

# 4. Notenstatistik
anzahl_schüler_mit_90_in_mathematik = len([note for note in mathematik if note >= 90])
anzahl_schüler_mit_90_in_physik = len([note for note in physik if note >= 90])
anzahl_schüler_mit_90_in_chemie = len([note for note in chemie if note >= 90])

# 5. Notenverteilung anzeigen
notenverteilung_mathematik = {note: mathematik.count(note) for note in set(mathematik)}
notenverteilung_physik = {note: physik.count(note) for note in set(physik)}
notenverteilung_chemie = {note: chemie.count(note) for note in set(chemie)}

print("Durchschnittsnote in Mathematik:", durchschnitt_mathematik)
print("Durchschnittsnote in Physik:", durchschnitt_physik)
print("Durchschnittsnote in Chemie:", durchschnitt_chemie)

print("Beste Note in Mathematik:", beste_mathematik)
print("Schlechteste Note in Mathematik:", schlechteste_mathematik)
print("Beste Note in Physik:", beste_physik)
print("Schlechteste Note in Physik:", schlechteste_physik)
print("Beste Note in Chemie:", beste_chemie)
print("Schlechteste Note in Chemie:", schlechteste_chemie)

print("Gesamtdurchschnittsnote über alle Fächer:", gesamtdurchschnitt)

print("Anzahl der Schüler mit mindestens 90 in Mathematik:", anzahl_schüler_mit_90_in_mathematik)
print("Anzahl der Schüler mit mindestens 90 in Physik:", anzahl_schüler_mit_90_in_physik)
print("Anzahl der Schüler mit mindestens 90 in Chemie:", anzahl_schüler_mit_90_in_chemie)

print("Notenverteilung in Mathematik:", notenverteilung_mathematik)
print("Notenverteilung in Physik:", notenverteilung_physik)
print("Notenverteilung in Chemie:", notenverteilung_chemie)
