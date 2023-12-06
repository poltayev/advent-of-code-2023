def read_lines():
    with open("inputs/problem2.txt", "r") as file:
        for line in file:
            yield line.strip()


def get_big_race():
    lines = read_lines()
    _, times = next(lines).split(':')
    _, distances = next(lines).split(':')

    time = int(''.join(times.strip().split()))
    distance = int(''.join(distances.strip().split()))

    return time, distance


def count_ways_of_wins(race):
    counter = 0
    time, distance = map(int, race)
    for holding_time in range(time + 1):
        passed_distance = holding_time * (time - holding_time)
        if passed_distance > distance:
            counter += 1

    return counter


def get_result():
    race = get_big_race()

    return count_ways_of_wins(race)


print(get_result())
