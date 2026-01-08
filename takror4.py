with open("data.txt","r") as file:
    f = file.read()
    print(len(f.split()))