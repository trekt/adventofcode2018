filename = "day5.txt"
file = open(filename, "r")
dataString = ""
for line in file:
    dataString = line

dataArray = list(dataString)

def activateReactions(inputArray):
    anyReactions = True
    while anyReactions:
        anyReactions = False
        i = 0

        while i < len(inputArray):
            if i+1 < len(inputArray):
                currentElement = inputArray[i]
                currentElementIndex = i
                currentElementAscii = ord(currentElement)
                nextElement = inputArray[i+1]
                nextElementIndex = i+1
                nextElementAscii = ord(nextElement)

                if currentElementAscii < 93:
                    if currentElementAscii+32 == nextElementAscii:
                        anyReactions = True
                        del inputArray[nextElementIndex]
                        del inputArray[currentElementIndex]
                        break

                if currentElementAscii > 93:
                    if currentElementAscii-32 == nextElementAscii:
                        anyReactions = True
                        del inputArray[nextElementIndex]
                        del inputArray[currentElementIndex]
                        break
                
            i += 1

    return len(inputArray)

currentLetter = 97
currentUpperCaseLetter = 65
currentLowest = 50000
j = 26

while j > 0:
    deletedElementList = dataArray.copy()
    k = 0
    while k < len(deletedElementList):
        if ord(deletedElementList[k]) == currentUpperCaseLetter:
            deletedElementList.remove(chr(currentUpperCaseLetter))
        if ord(deletedElementList[k]) == currentLetter:
            deletedElementList.remove(chr(currentLetter))
        k += 1
    print("Length of array after deletion ", len(deletedElementList))

    size = activateReactions(deletedElementList)
    print("Size after reactions ", size)
    if size < currentLowest:
        currentLowest = size

    currentLetter += 1
    currentUpperCaseLetter += 1
    j -= 1
print(currentLowest)


