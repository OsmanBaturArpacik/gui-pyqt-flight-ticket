def hesapla(liste):
    cift_kareler =list()
    for x in liste:
        if x % 2 == 0:
            cift_kareler.append(x**2)
    print(cift_kareler)

if __name__ == '__main__':
    hesapla([1,2,3,4,5])

