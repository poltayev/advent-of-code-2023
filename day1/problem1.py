def read_lines(filename):
    with open(f"inputs/{filename}", "r") as file:
        for line in file:
            yield line.strip()


def getNumber(line):
    x, y = 0, 0
    n = len(line)
    for i in range(n):
        if line[i].isdigit():
            x = int(line[i])
            break

    for i in range(n - 1, -1, -1):
        if line[i].isdigit():
            y = int(line[i])
            break

    return x * 10 + y


def getSumOfCalibration():
    total = 0
    for line in read_lines("problem1.txt"):
        total += getNumber(line)

    return total


print(getSumOfCalibration())
