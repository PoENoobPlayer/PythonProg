magassag = int(input("Mekkora a legyen a karácsonyfa?: "))
for i in range(magassag):
    for j in range(magassag-i):
        print(' ',end=' ')
    for k in range(2*i+1):
        print('*', end=' ')
    print()


for i in range(magassag):
    for j in range(magassag-1):
        print(' ', end=' ')
    print('* * *')

