class Araba:
    def __init__(self, marka, model, hiz=0):
        self.marka = marka
        self.model = model
        self.hiz = hiz
    def hizlan(self, miktar):
        self.hiz += miktar
        print(f"{self.model} hizlaniyor: Sunki hiz {self.hiz} km/s")

    def yavasla(self, miktar):
        self.hiz -= miktar
        print(f"{self.model} yavasliyor: Sunki hiz {self.hiz} km/s")


car1 = Araba("Toyota", "Corolla")
car2 = Araba("Ford", "Focus", 100)

print(car1.marka)
print(car1.hiz)

print(car2.marka)
print(car2.hiz)

car1.hizlan(50)
car2.yavasla(20)
