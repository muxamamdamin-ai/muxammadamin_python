ism = input("Ism kiriting:")
tel = input("Telefon raqamingizni kiriting")
yosh = int(input("Yoshingizni kiriting:"))
ob = {
    "ism":ism,
    "tel":tel,
    "yosh":yosh
}
with open("users.txt","a") as file:
    file.write(f"{ob}\n")