from paprika import *
@to_string

class Calisan:
    def __init__(self, isim, maas):
        self.isim = isim
        self.maas = maas


calisan1 = Calisan("selam", 1234)
print(calisan1.__str__())