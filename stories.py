import random  # Importiere die random-Bibliothek, um zufällige Elemente auszuwählen

# Listen von Wörtern und Phrasen in verschiedenen Kategorien
subjects = ["Ein grüner Dinosaurier", "Ein frecher Pinguin", "Ein furchtloser Astronaut"]
verbs = ["tanzt", "fliegt", "lacht über"]
objects = ["eine Banane", "einen Regenbogen", "eine Tasse Kaffee"]
places = ["auf dem Mond", "im Dschungel", "in der Wüste"]

# Funktion zur Generierung einer zufälligen Geschichte
def generate_story(num_sentences):
    story = []  # Initialisiere eine leere Liste, um die Sätze der Geschichte zu speichern
    for _ in range(num_sentences):  # Wiederhole den folgenden Block "num_sentences"-mal
        subject = random.choice(subjects)  # Zufällige Auswahl eines Subjekts aus der Liste
        verb = random.choice(verbs)  # Zufällige Auswahl eines Verbs aus der Liste
        obj = random.choice(objects)  # Zufällige Auswahl eines Objekts aus der Liste
        place = random.choice(places)  # Zufällige Auswahl eines Ortes aus der Liste
        sentence = f"{subject} {verb} {obj} {place}."  # Kombiniere die Elemente, um einen Satz zu erstellen
        story.append(sentence)  # Füge den Satz zur Liste der Geschichte hinzu
    return " ".join(story)  # Verbinde die Sätze zu einer zusammenhängenden Geschichte

print("Willkommen zum Zufallsgeschichten-Generator!")

while True:  # Schleife, um dem Benutzer die Möglichkeit zu geben, mehrere Geschichten zu generieren
    num_sentences = int(input("Geben Sie die Anzahl der Sätze in der Geschichte ein: "))

    # Generiere und gib die Geschichte aus
    generated_story = generate_story(num_sentences)  # Verwende die Funktion, um die Geschichte zu generieren
    print("\nHier ist deine zufällige Geschichte:\n")
    print(generated_story)  # Gib die generierte Geschichte aus

    # Benutzerabfrage, ob er eine weitere Geschichte generieren möchte
    another_story = input("Möchtest du eine weitere Geschichte generieren? (Ja/Nein): ").strip().lower()
    if another_story != "ja":
        print("Vielen Dank für die Verwendung des Zufallsgeschichten-Generators. Auf Wiedersehen!")
        break  # Die Schleife wird beendet, wenn der Benutzer nicht "ja" eingibt
