
number1 = 1
number2 = 1

def sestevanje(prejsnji, trenutni):
    rezultat = prejsnji + trenutni
    return rezultat

vsota = 0
while sestevanje(number1, number2)<4000000:
    naslednji = sestevanje(number1, number2)
    print(naslednji)
    number1 = number2
    number2 = naslednji 
    if naslednji % 2 == 0:
        vsota += naslednji
        print(vsota)
        print()
