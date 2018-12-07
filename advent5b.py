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

def remove_values_from_list(the_list, val):
       return [value for value in the_list if value != val]

currentLetter = 97
currentUpperCaseLetter = 65
currentLowest = 50000
j = 0

while j < 26:
    deletedElementList = dataArray.copy()
    deletedElementList = remove_values_from_list(deletedElementList, chr(currentLetter))
    deletedElementList = remove_values_from_list(deletedElementList, chr(currentUpperCaseLetter))

    print("Length of array after deletion ", len(deletedElementList))

    size = activateReactions(deletedElementList)
    print("Size after reactions ", size)
    if size < currentLowest:
        currentLowest = size

    currentLetter += 1
    currentUpperCaseLetter += 1
    j += 1
print(currentLowest)


