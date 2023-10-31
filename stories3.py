import random

# Listen von Wörtern und Phrasen in verschiedenen Kategorien
subjects = ["Ein gruener Dinosaurier", "Ein frecher Pinguin", "Ein furchtloser Astronaut"]
verbs = ["tanzt", "fliegt", "lacht ueber"]
objects = ["eine Banane", "einen Regenbogen", "eine Tasse Kaffee"]
places = ["auf dem Mond", "im Dschungel", "in der Wueste"]

# Listen für die Einführung, Handlungen, Höhepunkte und das Ende der Geschichte
introductions = ["In einer fernen Galaxie", "In einer geheimen Welt", "An einem sonnigen Tag"]
actions = ["entdeckte", "erkundete", "traf"]
highlights = ["einen Schatz", "eine geheime Tuer", "einen ausserirdischen Freund"]
endings = ["und lebte glücklich bis ans Ende seiner Tage.", "aber kehrte schliesslich nach Hause zurueck.", "und schrieb ein Buch über das Abenteuer."]

# Funktion zur Generierung einer zufälligen Geschichte
def generate_story():
    introduction = random.choice(introductions)
    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    place = random.choice(places)
    highlight = random.choice(highlights)
    ending = random.choice(endings)
    
    story = f"{introduction}, {subject} {action} {obj} {place}. Unterwegs entdeckte es {highlight}. Schliesslich kehrte es nach Hause zurück {ending}"
    return story

print("Willkommen zum verbesserten Zufallsgeschichten-Generator!")
num_stories = int(input("Geben Sie die Anzahl der Geschichten ein, die Sie generieren möchten: "))

# Erstellen und schreiben Sie die Geschichten in eine Textdatei
with open("generierte_geschichten.txt", "w") as file:
    for _ in range(num_stories):
        generated_story = generate_story()
        file.write("\nHier ist deine zufaellige Geschichte:\n")
        file.write(generated_story)
        file.write("\n")

print(f"{num_stories} Geschichten wurden in 'generierte_geschichten.txt' gespeichert.")
