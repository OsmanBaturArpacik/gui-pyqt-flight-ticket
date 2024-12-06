class BankaHesabi:
    def __init__(self, hesap_sahibi, bakiye=0):
        self.hesap_sahibi = hesap_sahibi
        self.__bakiye = bakiye

    def bakiye_getir(self):
        return self.__bakiye

    def para_yatir(self, miktar):
        self.__bakiye += miktar

hesap1 = BankaHesabi("Osman", 1000)
print(hesap1.hesap_sahibi)
print(hesap1._BankaHesabi__bakiye)

hesap1.para_yatir(10)

print(hesap1._BankaHesabi__bakiye)

