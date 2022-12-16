pontszam = int(input("Kérem a dolgozatnál elért pontszámot:"))

if pontszam >= 85:
    print("ötös")
elif 70<=pontszam<85:
    print("négyes")
elif 60<=pontszam<70:
    print("hármas")
elif 50<=pontszam<60:
    print("kettes")
elif pontszam<50:
    print("egyes")
else:
    print("Nem jó számot adtál meg!")