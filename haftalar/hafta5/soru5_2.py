def hesapla(uzun_Kenar, kisa_kenar):
    cevresi = (uzun_Kenar+kisa_kenar)*2
    alani = uzun_Kenar*kisa_kenar

    print(f"Dikdortgenin cevresi {cevresi}, Alani {alani}")

if __name__ == '__main__':
    hesapla(10,2)