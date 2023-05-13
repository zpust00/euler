
prastevila = range(1, 21)
num1 = 2

def resitev(stevilo):
    for prastevilo in prastevila:
        if stevilo % prastevilo != 0:
            return False
    return True
while not resitev(num1):
    num1 += 1

print(num1)