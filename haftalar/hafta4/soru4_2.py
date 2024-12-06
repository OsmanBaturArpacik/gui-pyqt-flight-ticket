"""
if __name__ == '__main__':
    x = int(input("pozitif sayi giriniz: "))

    while x <= 0:
        x = int(input("LUTFEN! POZITIF sayi giriniz: "))
"""

"""
if __name__ == '__main__':
    x = int(input("pozitif sayi giriniz: "))
    toplam = x
    while x != 0:
        x = int(input("sayi giriniz (Cikis icin \"0\"):"))
        toplam += x

    print(f"TOPLAM: {toplam}")
"""
"""
if __name__ == '__main__':
    parola = "1234"
    x = str(input("Parolanizi giriniz: "))
    while parola != x:
        x = str(input("Hatali giris yaptiniz. Parola giriniz: "))

    print(f"Giris yaptiniz.")
"""

"""
import random as rnd
if __name__ == '__main__':
    print("Sayi tahmin oyununa hos geldiniz.")
    print("******************************")
    rnd.seed(1)
    sayi = rnd.randint(0,11)
    hak = 3
    x = -1
    while hak > 0:
        if hak == 3:
            x = int(input("Sayi giriniz: "))            
        if x == sayi:
            print("Kazandiniz")
            hak-=1
            break
        print(f"Tahmin hakkiniz {hak}")
        x = int(input("Hatali tahmin yaptiniz Sayi giriniz: "))
        hak-=1

    if hak == 0 and sayi != x:
        print("Hakkiniz bitti")
    else:
        print("Kazandiniz")
"""

import random as rnd

if __name__ == '__main__':
    rnd.seed(1)

    sayi = rnd.randint(0,10)

    x = int(input("Sayi giriniz: "))

    while sayi != x:
        if x < sayi:
            print("IPUCU: Daha buyuk giriniz.")
        else:
            print("IPUCU: Daha kucuk giriniz.")
        x = int(input("Hatali tahmin yaptiniz Sayi giriniz: "))

    print("Dogru bildiniz")

