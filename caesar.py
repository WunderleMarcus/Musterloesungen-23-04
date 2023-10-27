def caesar_verschluesseln(text, schluessel):
    # Diese Funktion verschlüsselt einen Text mithilfe des Caesar-Verschlüsselungsalgorithmus.

    # Initialisiere eine leere Zeichenkette, um den verschlüsselten Text zu speichern.
    verschluesselter_text = ""

    # Iteriere über jeden Buchstaben im Text.
    for char in text:
        # Überprüfe, ob der Buchstabe ein Buchstabe des Alphabets ist.
        if char.isalpha():
            if char.islower():
                # Wenn es ein Kleinbuchstabe ist, verschiebe ihn um den Schlüsselwert im Alphabet nach rechts.
                verschluesselter_text += chr(((ord(char) - ord('a') + schluessel) % 26) + ord('a'))
            else:
                # Wenn es ein Großbuchstabe ist, verschiebe ihn um den Schlüsselwert im Alphabet nach rechts.
                verschluesselter_text += chr(((ord(char) - ord('A') + schluessel) % 26) + ord('A'))
        else:
            # Wenn der Buchstabe kein Alphabetbuchstabe ist, füge ihn unverändert hinzu.
            verschluesselter_text += char

    # Gib den verschlüsselten Text zurück.
    return verschluesselter_text

def caesar_entschluesseln(verschluesselter_text, schluessel):
    # Diese Funktion entschlüsselt einen Text mithilfe des Caesar-Verschlüsselungsalgorithmus.

    # Die Entschlüsselung erfolgt, indem die Verschlüsselungsfunktion mit dem negativen Schlüssel aufgerufen wird.
    return caesar_verschluesseln(verschluesselter_text, -schluessel)

def main():
    # Diese Funktion ist die Hauptfunktion des Programms, die die Benutzerinteraktion steuert.

    while True:
        print("Willkommen zum Caesar-Verschlüsselungstool!")
        nachricht = input("Geben Sie die Nachricht ein: ")
        schluessel = int(input("Geben Sie den Verschlüsselungsschlüssel ein (-25 bis 25): "))
        mode = input("Möchten Sie verschlüsseln (E) oder entschlüsseln (D)?: ").upper()

        if -25 <= schluessel <= 25:
            if mode == "E":
                # Wenn der Benutzer die Verschlüsselung ausgewählt hat, rufe die Verschlüsselungsfunktion auf.
                verschluesselter_text = caesar_verschluesseln(nachricht, schluessel)
                print("Verschlüsselte Nachricht:", verschluesselter_text)
            elif mode == "D":
                # Wenn der Benutzer die Entschlüsselung ausgewählt hat, rufe die Entschlüsselungsfunktion auf.
                entschluesselter_text = caesar_entschluesseln(nachricht, schluessel)
                print("Entschlüsselte Nachricht:", entschluesselter_text)
            else:
                print("Ungültiger Modus. Bitte E für Verschlüsselung oder D für Entschlüsselung eingeben.")
        else:
            print("Ungültiger Schlüssel. Der Schlüssel muss im Bereich von -25 bis 25 liegen.")

        weitere_nachricht = input("Möchten Sie eine weitere Nachricht verschlüsseln/entschlüsseln? (J/N): ").upper()
        if weitere_nachricht != "J":
            print("Vielen Dank für die Nutzung des Caesar-Verschlüsselungstools!")
            break

if __name__ == "__main__":
    main()
