
num1 = 10001 # zaporedna stevilka zeljenega prafaktorja
i = 0
stevilke = 2

while i < num1:
    ab = stevilke // 2
    if all(stevilke % i != 0 for i in range(2, ab+1)):
        i += 1
    stevilke += 1

print(stevilke-1)
