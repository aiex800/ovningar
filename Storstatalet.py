störstaTal = 0 
lista = [] #gör en lista där alla siffror sparas
print("Hur mångra siffror är det i listan?") 
antal = int(input("")) #Skriver in hur mångra tal man ska ha i listan
for x in range(antal): #Kör kod stycket x antal gånger
    tal = int(input("Skriv ett tal: ")) #Skriver in talen
    lista.append(tal) #Lägger till talet man skriver in i listan
print(lista)
for g in lista: #Kör igenom alla tal
    if g > störstaTal: #om g är större en störstartal
        störstaTal = g 
print("största talet är: ", störstaTal)