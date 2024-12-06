
if __name__ == '__main__':
    myTuple = (0,2,3)

    myList = list(myTuple)
    myList[0] = 1
    myList.append(5)
    myList.remove(2)

    myTuple = tuple(myList)
    print(myTuple)