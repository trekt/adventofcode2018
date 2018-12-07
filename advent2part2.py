filename = "day2.txt";
file = open(filename, "r");
arrayOfCodes = [];
for line in file:
    arrayOfCodes.append(line);

i = 0;
while i < len(arrayOfCodes) - 1:
    currentCode = arrayOfCodes[i];
    j = i + 1;
    while j < len(arrayOfCodes):
        comparingCode = arrayOfCodes[j];

        k = 0;
        NumLettersDifferent = 0;
        sameLetters = [];

        while k < len(currentCode) - 1:
            if currentCode[k] == comparingCode[k]:
                sameLetters.append(currentCode[k]);
            if currentCode[k] != comparingCode[k]:
                NumLettersDifferent += 1; 
            k += 1;
        if NumLettersDifferent < 2:
            print(''.join(sameLetters));

        j += 1;

    i += 1;