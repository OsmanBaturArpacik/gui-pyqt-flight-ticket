import math

def hesapla_dikdortgen_cevre(uzun_Kenar, kisa_kenar):
    cevresi = (uzun_Kenar + kisa_kenar) * 2
    print(f"Dikdortgenin cevresi: {cevresi}")
def hesapla_dikdortgen_alan(uzun_Kenar, kisa_kenar):
    alani = uzun_Kenar * kisa_kenar
    print(f"Dikdortgenin alani: {alani}")

def hesapla_daire_cevre(yaricap):
    cevresi = 2*math.pi*yaricap
    print(f"Daire cevresi: {cevresi}")
def hesapla_daire_alan(yaricap):
    alani = 2*math.pi*(yaricap**2)
    print(f"Daire alani: {alani}")

def hesapla_kare_cevre(kenar):
    cevresi = kenar * 4
    print(f"Karenin cevresi: {cevresi}")
def hesapla_kare_alan(kenar):
    alani = kenar*kenar
    print(f"Karenin cevresi: {alani}")

if __name__ == '__main__':
    print("Hangi geometrik şeklin alanını hesaplamak istersiniz?\n1. Dikdörtgen\n2. Kare\n3. Daire")
    secim = int(input("Seçiminizi yapın (1,2,3) : "))

    match secim:
        case 1:
            print("Dikdörtgenin kenar uzunluklarini giriniz:")
            uzun = int(input("Uzun kenar: "))
            kisa = int(input("Kisa kenar: "))
            cevre = hesapla_dikdortgen_cevre(uzun, kisa)
            alan = hesapla_dikdortgen_alan(uzun, kisa)
            # print(form"Dikdörtgenin cevresi: {cevre}\nDikdörtgenin alani: {alan}")
        case 2:
            print("Kare kenar uzunluğunu giriniz:")
            kenar = int(input("Kenar: "))
            cevre = hesapla_kare_cevre(kenar)
            alan = hesapla_kare_alan(kenar)
            # print(form"Karenin cevresi: {cevre}\nKarenin alani: {alan}")
        case 3:
            print("Dairenin Yaricap uzunlugunu giriniz:")
            yaricap = int(input("Yaricap: "))
            cevre = hesapla_daire_cevre(yaricap)
            alan = hesapla_daire_alan(yaricap)
            # print(form"Dairenin cevresi {cevre}\nDairenin alani: {alan}")
        case _:
            print("Hatali giris")


