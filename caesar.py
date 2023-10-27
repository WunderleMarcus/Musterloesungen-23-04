def caesar_verschluesseln(text, schluessel):
    verschluesselter_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                verschluesselter_text += chr(((ord(char) - ord('a') + schluessel) % 26) + ord('a'))
            else:
                verschluesselter_text += chr(((ord(char) - ord('A') + schluessel) % 26) + ord('A'))
        else:
            verschluesselter_text += char
    return verschluesselter_text

def caesar_entschluesseln(verschluesselter_text, schluessel):
    return caesar_verschluesseln(verschluesselter_text, -schluessel)

def main():
    while True:
        print("Willkommen zum Caesar-Verschlüsselungstool!")
        nachricht = input("Geben Sie die Nachricht ein: ")
        schluessel = int(input("Geben Sie den Verschlüsselungsschlüssel ein (-25 bis 25): "))
        mode = input("Möchten Sie verschlüsseln (E) oder entschlüsseln (D)?: ").upper()
        
        if -25 <= schluessel <= 25:
            if mode == "E":
                verschluesselter_text = caesar_verschluesseln(nachricht, schluessel)
                print("Verschlüsselte Nachricht:", verschluesselter_text)
            elif mode == "D":
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
