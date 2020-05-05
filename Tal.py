print("Skriv ett tal")
tal = int(input(""))
print("Du valde", tal)
if tal < 10:
    print("du valde ett tal under 10")
elif tal > 10:
    print("du valde ett tal över 10")
else :
    print("varken eller")