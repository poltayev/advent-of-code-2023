def read_lines():
    with open("inputs/problem1.txt", "r") as file:
        for line in file:
            yield line.strip()


def get_races():
    lines = read_lines()
    _, times = next(lines).split(':')
    _, distances = next(lines).split(':')

    return list(zip(times.strip().split(), distances.strip().split()))


def count_ways_of_wins(race):
    counter = 0
    time, distance = map(int, race)
    for holding_time in range(time + 1):
        passed_distance = holding_time * (time - holding_time)
        if passed_distance > distance:
            counter += 1

    return counter


def multiplied_ways_of_wins():
    ans = 1
    races = get_races()
    for race in races:
        ans *= count_ways_of_wins(race)

    return ans


print(multiplied_ways_of_wins())
