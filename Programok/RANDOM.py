import random


lista = []

#feltöltjük a listát random számokkal
for i in range(10): #10 db szám lesz a listában
    lista.append(random.randint(1,100))
# print(lista)

#Feladat
#Írjuk ki a 10-nél nagyobb számokat
for i in range(len(lista)):
    if lista[i] >= 10:
        print(lista[i])
#Írjuk ki a 10-nél kisebb számokat
for i in range(len(lista)):
    if lista[i] < 10:
        print(lista[i])