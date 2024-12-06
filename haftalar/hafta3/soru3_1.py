if __name__ == '__main__':
    yas = int(input("Yasinizi giriniz: "))
    ehliyet = int(input("Ehliyetiniz var mı? "))

    if yas >= 18 and ehliyet:
        print("Arac sürebilirsiniz")
    else:
        print("Arac süremezsiniz")
