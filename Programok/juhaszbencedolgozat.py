import math

szamok = [10, 23, 24, 26, 11, 8, 54, 21]
szamok.insert(1, 62)

x = szamok.index(26)
print(x)
print("***********************************")
osszeg = 0
for i in range(len(szamok)):
    if szamok[i] % 2 != 0:
        print(szamok[i])
        osszeg = osszeg + szamok[i]
print(osszeg)

