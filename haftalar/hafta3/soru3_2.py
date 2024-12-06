if __name__ == '__main__':


    sayi = int(input("puan giriniz: "))
    sonuc = "A" if sayi > 90 else ("B" if sayi > 80 else ("C" if sayi > 70 else ("D" if sayi > 60 else ("E" if sayi > 50 else "F"))))
    print(sonuc)