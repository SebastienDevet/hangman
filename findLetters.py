
def findLetters(myWord, myLetter):
    myList = []
    for i, c in enumerate(myWord):
        if c == myLetter:
            myList.append(i)

    return myList
