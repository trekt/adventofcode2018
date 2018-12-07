filename = "day2.txt";
numberof2s = 0;
numberof3s = 0;
file = open(filename, "r")
for line in file:
    alreadyCounted2 = False;
    alreadyCounted3 = False;
    countedLettersArray = [];
    i = 0;

    while i < len(line):
        if line[i] not in countedLettersArray:
            total = line.count(line[i]);
            countedLettersArray.append(line[i]);
            if total == 3 and alreadyCounted3 != True:
                numberof3s += 1
                alreadyCounted3 = True;
            if total == 2 and alreadyCounted2 != True:
                numberof2s += 1
                alreadyCounted2 = True;
        i += 1;

print(numberof2s * numberof3s);