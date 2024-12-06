
if __name__ == '__main__':
    ogrenci_isim = " "
    ogrenci_kulup_ismi = " "
    ogrenci_not_dict = dict()
    ogrenci_kulup_dict = dict()
    ogrenci_gecme_durumu = list()

    while True:
        print()

        ogrenci_isim = str(input("Ogrenci ismi (Cikis icin 0 veya ENTER'a basiniz): "))

        if ogrenci_isim == "0" or ogrenci_isim == "":
            break
        ogrenci_not_dict[f"{ogrenci_isim}"] = {"notlari": []}
        for i in range(0,3):
            ogrenci_notu = int(input(f"Ogrenci not-{i+1}: "))
            ogrenci_not_dict[f"{ogrenci_isim}"]["notlari"].append(ogrenci_notu)

        sayac = 1
        ogrenci_kulup_dict[f"{ogrenci_isim}"] = {"kulup_adi": []}
        while True:
            ogrenci_kulup_ismi = str(input(f"Ogrencinin Uye Oldugu {sayac}. Kulup adini giriniz  (Cikis icin 0 veya ENTER'a basiniz): "))
            if ogrenci_kulup_ismi == "0" or ogrenci_kulup_ismi == "":
                break
            ogrenci_kulup_dict[f"{ogrenci_isim}"]["kulup_adi"].append(ogrenci_kulup_ismi)
            sayac += 1
    print()

    for name in ogrenci_not_dict.keys():
        print(f"{name}", end=" - ")
        # notlar
        ortalama = 0
        for key, value in ogrenci_not_dict[f"{name}"].items():
            # gecme kalma durumu
            for i in range(0,3):
                ortalama += value[i] / 3
            print(f"Ortalama: {ortalama:.2f}", end=" - ")
            print("Durum: ", end="")
            print("Geçti" if ortalama >= 50 else "Kaldı", end="\n")

    print()

    for name in ogrenci_kulup_dict.keys():
        kulup_adlari = ogrenci_kulup_dict[f"{name}"]["kulup_adi"]
        print(f"{name} şu kulüplere katıldı: {", ".join(kulup_adlari)}" if kulup_adlari else f"{name} hiçbir kulübe katılmadı.", end="\n")
