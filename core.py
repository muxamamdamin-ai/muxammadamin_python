print("="*30)
print("Xush kelibsiz!")
print("="*30)
products = {
    "mahsulot turlari":["Meva","Sabzvot","Ichimlik","Mahsulot"],
    "mahsulotlar":[
        {
            "nomi":"Olma",
            "unit":"KG",
            "cost":50000,
            "qushiladigan foyda":5,
            "turi":0
    },
    {
        "nomi":"Rediska",
        "unit":"KG",
        "cost":10000,
        "qushiladigan foyda":5,
        "turi":1
    },
    {
        "nomi":"Pepsi 2.0L",
        "unit":"dona",
        "cost":17000,
        "qushiladigan foyda":5,
        "turi":2
    }
    ]
}
while True:
    kerak_buladi = []
    print("="*30)
    print("Mahsulot turini tanglang")
    for idx,turlar in enumerate(products["mahsulot turlari"]):
        print(f"{idx+1}){turlar}")
    print("="*30)
    tur_inp = int(input(">>>"))
    print("=" * 30)
    print("Siz tanlagan turga oyit bulgan mahsulotlar:")
    i = 0
    for mahsulot in products["mahsulotlar"]:
        if mahsulot["turi"] == tur_inp -1:
            print(f"{i+1}){mahsulot["nomi"]}-{mahsulot["cost"]}so'm")
            kerak_buladi.append([mahsulot,i+1])
    print("="*30)
    mahsulot_inp = int(input(">>>"))
    for kerak in kerak_buladi:
        if kerak[1] == mahsulot_inp:
            print(f"Siz sotib oldingiz {kerak[0]["nomi"]}ni")
            print("Sotib olganingiz uchun rahmat!")
            print()
            print()
            print()
