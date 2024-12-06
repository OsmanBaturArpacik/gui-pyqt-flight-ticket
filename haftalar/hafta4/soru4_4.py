if __name__ == '__main__':
    notlar_listesi = list()
    notlar_durumu = list() # gecti kaldi 50 den buyuk esit gecti
    not_sayisi = int(input("Girilecek not sayisi: "))

    sayac = 0
    while sayac < not_sayisi:
        ders_notu = int(input("Not gir: "))
        if ders_notu >= 50:
            notlar_listesi.append(ders_notu)
            notlar_durumu.append("GECTI")
        else:
            notlar_listesi.append(ders_notu)
            notlar_durumu.append("KALDI")
        sayac+=1

    for i in range(0, not_sayisi):
        print(f"Ders Notu:{notlar_listesi[i]}, Durum:{notlar_durumu[i]}")