"""
x = "awesome"

def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)
    print(id(x))

myfunc()
print(id(x))

print("Python is " + x)
"""

if __name__ == '__main__':
    haftaici = ["pazartesi", "sali", "carsamba", "persembe","cuma"]
    haftasonu = ["cumartesi", "pazar"]
    param = str(input("Gun giriniz:")).lower()
    match param:
        case param if param in haftaici:
            print("Hafta içindeyiz.")
        case param if param in haftasonu:
            print("Hafta sonundayız.")
        case _:
            print("Gecersiz Gün Girdiniz. Lütfen aşağıdakilerden birini giriniz.\n",haftaici, haftasonu)
