
if __name__ == '__main__':
    ogrenci_isim = " "
    ogrenci_kulup_ismi = " "
    ogrenci_not_dict = dict()
    ogrenci_kulup_dict = dict()
    ogrenci_gecme_durumu = list()

    while True:
        print("====================================")

        ogrenci_isim = str(input("Ogrenci ismi (Cikis icin 0): "))

        if ogrenci_isim == "0":
            break
        ogrenci_not_dict[f"{ogrenci_isim}"] = {"notlari": []}
        for i in range(0,3):
            ogrenci_notu = int(input(f"Ogrenci not-{i+1}: "))
            ogrenci_not_dict[f"{ogrenci_isim}"]["notlari"].append(ogrenci_notu)

        sayac = 1
        ogrenci_kulup_dict[f"{ogrenci_isim}"] = {"kulup_adi": []}
        while True:
            ogrenci_kulup_ismi = str(input(f"Ogrencinin Uye Oldugu {sayac}. Kulup adini giriniz  (Cikis icin 0): ")).lower()
            if ogrenci_kulup_ismi == "0":
                break
            ogrenci_kulup_dict[f"{ogrenci_isim}"]["kulup_adi"].append(ogrenci_kulup_ismi)
            sayac += 1
    """
    ogrenci_not_dict = {
        "osman": {"notlari": [100, 99, 39]},
        "ali": {"notlari": [13,43,70]},
        "batur": {"notlari": [97, 9, 49]}
    }
    ogrenci_kulup_dict = {
        "osman": {"kulup_adi": ["mat", "fizik", "biyoloji"]},
        "ali": {"kulup_adi": ["resim", "satranc", "biyoloji"]},
        "batur": {"kulup_adi": []}
    }
    ogrenci_gecme_durumu = list(["GECTI", "KALDI", "GECTI"])
    """
    for name in ogrenci_not_dict.keys():
        print("------------------------------------", end="\n")
        print(f"isim: {name}", end="\t\t")
        # notlar
        ortalama = 0
        for key, value in ogrenci_not_dict[f"{name}"].items():
            print(f"ogrenci {key}: {value}", end="\t\t")
            # gecme kalma durumu
            for i in range(0,3):
                ortalama += value[i] / 3
            print("GECTI" if ortalama >= 50 else "KALDI", end="\t\t")
        # kulupler
        for key, value in ogrenci_kulup_dict[f"{name}"].items():
            print(f"ogrenci {key}: {value}", end="\n")

    print("------------------------------------", end="\n")
