class ogrenci:
    def __init__(self,name,age,height,weight):
        print("Inside class __init__")
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        print("Object initialized")

    def __str__(self):
        return f'{self.name, self.age, self.height, self.weight}'

    def __del__(self):
        print("Inside class __del__")
        print("Object destroyed")


ogrenci1 = ogrenci('osman', '20', '180', '75')
print(ogrenci1.__str__())
ogrenci2 = ogrenci1
del ogrenci1
print(ogrenci2.__str__())
del ogrenci2
