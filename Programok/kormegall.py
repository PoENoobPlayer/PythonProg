kor = int(input("Hány éves vagy?: "))
felnott = 18
nyugdíjas = 65

if kor > nyugdíjas:
    print("Te már nyugdíjas vagy!")
elif kor == nyugdíjas:
    print("Nyugdíjas leszel mindjárt!")
elif kor < felnott:
    print("Te még kiskorú vagy!")
else:
    print("Te már felnőtt, vagy diák vagy!")