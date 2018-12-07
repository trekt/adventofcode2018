filename = "day1.txt";
frequencyArray = [0];
total = 0;

while 1:
    file = open(filename, "r")
    for line in file:
        total += int(float(line))
        if total in frequencyArray:
            print("first frequency duplicate: ", total);
            exit();
        if total not in frequencyArray:
            frequencyArray.append(total);
            print("appending", total);