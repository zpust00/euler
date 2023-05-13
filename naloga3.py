
stevilka = 600851475143
#stevilka = 13195
delitelj = 2
zmnozek = 1

for delitelj in range(1, stevilka + 1):
    if stevilka % delitelj == 0:
        print(delitelj)
        zmnozek = zmnozek * delitelj
        print(zmnozek)
        if zmnozek == stevilka:
            break

