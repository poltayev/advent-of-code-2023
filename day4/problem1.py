def read_lines():
    with open("inputs/problem1.txt", "r") as file:
        for line in file:
            yield line.strip()


def get_points(winning_numbers: set, having_numbers: list):
    points = 0
    for num in having_numbers:
        if num in winning_numbers:
            if points == 0:
                points += 1
            else:
                points *= 2

    return points


def get_total_points():
    total = 0
    for line in read_lines():
        _, data = line.split(":")
        winning_numbers, having_numbers = data.split("|")
        points = get_points(set(winning_numbers.split()), having_numbers.split())

        total += points

    return total


print(get_total_points())
