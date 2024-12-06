if __name__ == '__main__':
    meyveler = ["elma", "muz", "armut"]
    for item in meyveler:
        print(item)

    dict = {"elma": 1, "muz": 2, "armut":3}
    for key, value in dict.items():
        print(key, value)

    for i in range(5):
        print(i)

    for i in range(2,7,2):
        print(i)

    for i in range(2,-10,-2):
        print(i)

    for i in "hello world":
        print(i, end=" ")

    for i in range(1,11):
        for j in range(1,11):
            print(f"{i} x {j} = {i*j}", end="\t")
        print()

    arr = [[1,2,3], [4,5,6], [7,8,9]]

    for i in range(0,len(arr)):
        print("|", end="\t")
        for j in range(0,len(arr[0])):
            print(f"{arr[i][j]}", end="\t")
        print("|", end="\n")

    for i in range(1,6):
        for j in range(1,6):
            print(j, end=" ")
        print()

    for i in range(1,6):
        print("* "*i, end="\n")

    for i in range(1,6):
        for j in range(0,i):
            print("*", end=" ")
        print()

    for i in range(1, 6):
        for j in range(0, i):
            print(f"{j+1}", end=" ")
        print()

    for i in range(0,5):
        for j in range(0, 5 - i - 1):
            print(" ", end="")
        for k in range(0, i * 2 + 1):
            print("*", end="")
        print()

    dict = {"ad": "ali", "yas": "18", "meslek": "muhendis"}
    for key, value in dict.items():
        print(f"{key} : {value}")

    liste = [1,2,3,4,5,6,7,8,9]
    tek = list()
    cift = list()

    for i in liste:
        if i % 2 == 0:
            cift.append(i)
        else:
            tek.append(i)

    print(f"TEK: {tek}, CIFT: {cift}")

    for i in range(10):
        if i == 2 or i == 4:
            continue
        if i == 5:
            break
        print(i)


