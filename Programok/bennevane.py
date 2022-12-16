# szoveg = "ez egy szöveg"
# if "v" in szoveg:
#     print("benne van")
# else: print("nincs") 

# szoveg = "ez egy szöveg"
# beker = input("Kérem a betűt!")
# if beker in szoveg:
#     print(f"{beker} betű benne van a szövegben")
# else: print(f"{beker} betű nincs a szövegben")

# szoveg = "KEDD"
# print = (szoveg.lower())


# hetnapjai = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap" ]

# beker = input("Kérem a napot! ").lower()

# if beker in hetnapjai:
#     print(f"{beker} nap benne van a listában")
# else:
#     print(f"{beker} nap nincs van a listában")

karakterek = ["Fremy Speeddraw", "Adlet Mayer", "Hans Humpty", "Mora Chester", "Chamo Rosso", "Kirigaya Kazuto", "Asuna Yuuki", "Yuuki Asuna", "Natsuki Subaru", "Kurumi Tokisaki", "Nao Tomori", "Eris Boreas Greyrat", "Rudeus Greyrat", "Roxy Migurdia", "Sylphiette", "Ichirou Satou", "Ryouko Satou"]

# karakterek_nagybetu = [item.lower() for item in karakterek]
# karakterek_kisbetu = [item.upper() for item in karakterek]


# beker = input("Kérem a karakter nevét!: ")

# if beker in karakterek:
#     print(f"{beker} benne van a listában")
# else:
#     print(f"{beker} nincs benne a listában")

#print(karakterek[1][0:11])
for i in range(len(karakterek)):
    if "o" in karakterek[i]:
        print(karakterek[i])