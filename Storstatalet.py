störstatal = 0
lista = []
print("Hur mångra siffror är det i listan?")
antal = int(input(""))
for x in range(antal):
    tal = int(input("Skriv ett tal: "))
    lista.append(tal)
print(lista)
for g in lista:
    if g > störstatal:
        störstatal = g
print("största talet är: ", störstatal)