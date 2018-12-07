import re;

filename = "day4.txt";
file = open(filename, "r");
arrayOfTimes = [];
for line in file:
    arrayOfTimes.append(line);

#first sort the list by date and time
arrayOfTimes.sort();

#second find which guard sleeps the most
arrayOfGuards = []; #keep track of all guard numbers
arrayOfSleepTotals = []; #keep track of total hours slept, index of times should match arrayOfGuards

i = 0;
currentGuard = 0;
currentGuardIndex = 0;
startSleepTime = 0;
finishSleepTime = 0;
while i < len(arrayOfTimes):
    currentLine = arrayOfTimes[i];
    descriptionStart = 19; #text describing action starts at char19 of line
    if currentLine[descriptionStart] == "G":
        currentGuard = re.findall('(?<=#).*?\s', currentLine)[0];
        print(currentLine);
        print("Parsed guard:", currentGuard);
        if currentGuard not in arrayOfGuards:
            arrayOfGuards.append(currentGuard);
        currentGuardIndex = arrayOfGuards.index(currentGuard);
    if currentLine[descriptionStart] == "f":
        #start keeping track of time to add
        startSleepTime = int(float(currentLine[15:17]));
        print(currentLine);
        print("starts sleeping at ", startSleepTime);
    if currentLine[descriptionStart] == "w":
        #end time tracking
        finishSleepTime = int(float(currentLine[15:17]));
        print(currentLine);
        print("finishes sleeping at ", finishSleepTime, "total time: ", finishSleepTime-startSleepTime);
        if arrayOfSleepTotals[currentGuardIndex] is not None:
            arrayOfSleepTotals[currentGuardIndex] += (finishSleepTime - startSleepTime);
    i += 1;

