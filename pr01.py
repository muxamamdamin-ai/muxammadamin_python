while True:
    print("\n--- Kontaktlar Menejeri ---")
    print("1) Kontaktlarni ko'rish")
    print("2) Kontakt yaratish")
    print("0) Chiqish")
    amal = input(">>>")

    if amal == "0":
        break
    if amal == "1":
        file = open("contacts.txt", "r")
        data = file.read().split("\n")
        file.close()

        yana = input("To'liq ma'lumot ko'rilsinmi? (1-ha, 0-yo'q): ")
        
        for qator in data:
            user = qator.split(",")
            ism = user[0]
            tel = user[1]
            email = user[2]
            manzil = user[3]

            if yana == "1":
                print(ism, "-", tel, "| Email:", email, "| Uy:", manzil)
            else:
                print(ism, "-", tel)
        print("-" * 20)
    elif amal == "2":
        file = open("contacts.txt", "r")
        data = file.read().split("\n")
        file.close()

        ism = input("Ismni kiriting: ")
        ism_band = False
        for qator in data:
            if qator != "":
                user = qator.split(",")
                if user[0] == ism:
                    ism_band = True
        if ism_band == True:
            print("Bu ism allaqachon bor!")
            print("Boshidan urinib kurig!")
            break

        telefon = input("Telefon raqam (9 ta raqam): ")
        for user in data:
            while len(telefon) != 9 or user[1] == telefon:
                print("Xato: Raqam noto'g'ri yoki Bu raqam bor!")
                telefon = input(">>>")

        savol = input("Qo'shimcha ma'lumot kiritasizmi? (1-ha, 0-yo'q): ")
        if savol == "1":
            email = input("Email kiriting: ")
            adres = input("Uy raqamini kiriting: ")
        else:
            email = "-"
            adres = "-"
        file = open("contacts.txt", "a")
        file.write(ism + "," + telefon + "," + email + "," + adres + "\n")
        file.close()
        print("Saqlandi!")