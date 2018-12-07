filename = "day5.txt"
file = open(filename, "r")
dataString = ""
for line in file:
    dataString = line

dataArray = list(dataString)
anyReactions = True
while anyReactions:
    anyReactions = False
    i = 0
    #print(len(dataArray))

    while i < len(dataArray):
        if i+1 < len(dataArray):
            currentElement = dataArray[i]
            currentElementIndex = i
            currentElementAscii = ord(currentElement)
            nextElement = dataArray[i+1]
            nextElementIndex = i+1
            nextElementAscii = ord(nextElement)

            if currentElementAscii < 93:
                if currentElementAscii+32 == nextElementAscii:
                    anyReactions = True
                    del dataArray[nextElementIndex]
                    del dataArray[currentElementIndex]
                    break

            if currentElementAscii > 93:
                if currentElementAscii-32 == nextElementAscii:
                    anyReactions = True
                    del dataArray[nextElementIndex]
                    del dataArray[currentElementIndex]
                    break
            
        i += 1

print(len(dataArray))