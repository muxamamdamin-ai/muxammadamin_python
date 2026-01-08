suz = input(">>>")
suzlar = 0
with open("data.txt","r") as file:
    fi = file.read()
    fe = fi.split()
    for f in fe:
        if f == suz:
            suzlar += 1
print(suzlar)