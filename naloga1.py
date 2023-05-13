
vsota = 0
vsota2 = 0

for i in range(1000):
    print(i)
    vsota += i
    print(vsota)
    if i % 3 == 0 or i % 5 == 0:
        vsota2 += i
    print(vsota2)
    print()