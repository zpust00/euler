
num1 = 100
num2 = 100
sestevek1 = 0
sestevek2 = 1
sestevek22 = 0
resitev = 0

for i in range(num1):
    i += 1
    sestevek1 = sestevek1 + i
    print(i)
    print(sestevek1)
    print()

sestevek1 = sestevek1*sestevek1
print(sestevek1)

for a in range(num2):
    a += 1
    print(a)
    sestevek22 = a*a + sestevek22
    print(sestevek2)
    print()
print(sestevek22)

resitev = sestevek1 - sestevek22
print(resitev)