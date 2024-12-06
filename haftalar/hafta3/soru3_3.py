"""if __name__ == '__main__':
    girilen = str(input("sifre giriniz: "))
    password = "12345"
    if password == girilen:
        print("hg")
    else:
        print("bb")
"""
# etkinlik ücreti hesaplama sistemi

if __name__ == '__main__':
    yas = int(input("Yas giriniz: "))
    ogrenciMi = str(input("Ogrenci misiniz? EVET/HAYIR: "))
    gelirDurumu = float(input("Gelir durumunuzu girin: "))

    biletFiyat = 100.0

    toplam = 0
    indirimOrani = 0

    if yas < 18:
        indirimOrani += 50
        print("18 yaşından altındasınız %50 indirim")
    elif 25 < yas < 40 and ogrenciMi.lower() == "evet":
        print("Öğrenci ve 25-40 yaş arasında olduğunuzdan %40 indirim")
        indirimOrani += 40
    elif yas >= 65:
        print("65 yaş üstü katılımcılara %30 indirim")
        indirimOrani += 30
    else:
        print("%10 indirim")
        indirimOrani += 10

    # ek indirim
    if gelirDurumu < 3000:
        print("Gelir durumu 3000 tl altında olduğundan %20 indirim")
        indirimOrani += 20
    else:
        pass

    toplam = biletFiyat - biletFiyat * (indirimOrani/100)

    print(f"Etkinlik Ücreti: {biletFiyat}TL")
    print(f"İndirim Oranı: {indirimOrani}%")
    print(f"Ödenecek Ücret: {toplam:.2f}TL")

    # toplam indirim orani