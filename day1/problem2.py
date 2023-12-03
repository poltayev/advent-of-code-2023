def read_lines(filename):
    """A generator function to read a file line by line."""
    with open(f"inputs/{filename}", "r") as file:
        for line in file:
            yield line.strip()


def getNumber(s):
    n = len(s)
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    matches = {
        "o": ["one"],
        "t": ["two", "three"],
        "f": ["four", "five"],
        "s": ["six", "seven"],
        "e": ["eight"],
        "n": ["nine"],
    }

    is_num_word_found = False
    for i in range(n):
        if s[i].isdigit():
            x = int(s[i])
            break

        if s[i] in matches:
            m_digits = matches[s[i]]
            for digit in m_digits:
                v = s[i : i + len(digit)]
                if v in digits:
                    x = int(digits[v])
                    is_num_word_found = True
                    break

            if is_num_word_found:
                break

    is_num_word_found = False
    for i in range(n - 1, -1, -1):
        if s[i].isdigit():
            y = int(s[i])
            break

        if s[i] in matches:
            m_digits = matches[s[i]]
            for digit in m_digits:
                if i + len(digit) > len(s):
                    continue

                v = s[i : i + len(digit)]
                if v in digits:
                    y = int(digits[v])
                    is_num_word_found = True
                    break

            if is_num_word_found:
                break
    return x * 10 + y


def getSumOfCalibration():
    total = 0
    for line in read_lines("problem2.txt"):
        num = getNumber(line)
        total += num

    return total


print(getSumOfCalibration())
