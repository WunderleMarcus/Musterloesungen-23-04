def umkehren_liste(lst):
    # Funktion, die die Liste umkehrt
    umgekehrte_liste = lst[::-1]  # Nutze Slicing, um die Liste umzukehren
    return umgekehrte_liste

def duplizieren_liste(lst):
    # Funktion, die die Liste dupliziert
    duplizierte_liste = []
    for element in lst:
        duplizierte_liste.extend([element, element])  # Füge jedes Element zweimal hinzu
    return duplizierte_liste

urspruengliche_liste = [1, 2, 3, 4, 5]

umgekehrte = umkehren_liste(urspruengliche_liste)
duplizierte = duplizieren_liste(umgekehrte)

print("Ursprüngliche Liste:", urspruengliche_liste)
print("Umgekehrte Liste:", umgekehrte)
print("Duplizierte Liste:", duplizierte)
