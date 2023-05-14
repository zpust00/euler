stevilo = 2000000
#stevilo = 10
resitev = 0

#za majse kot 2 dodamo 2, ker 1 ni prastevilo, ,katerega bi program tudi uposteval, prav tako pa se ognemo problema deljenja s samim seboj
if stevilo > 2:
    resitev += 2

for stevilka in range(3, stevilo, 2): #jemljemo po dva, skrajsamo cas za polovico
    prastevilo = True
    for delitelj in range(3, int(stevilka**0.5)+1, 2):
        if stevilka % delitelj == 0:
            prastevilo = False
            break
    if prastevilo:
        resitev += stevilka
        print(stevilka)

print(resitev)
