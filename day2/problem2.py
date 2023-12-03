def read_lines():
    with open("inputs/problem2.txt", "r") as file:
        for line in file:
            yield line.strip()


def get_min_power(cubes):
    color_powers = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }

    red, green, blue = 0, 0, 0
    for hit in cubes.split(";"):
        for hit_cube in hit.split(","):
            num, color = hit_cube.split()
            color_powers[color] = max(color_powers[color], int(num))

    return color_powers["red"] * color_powers["blue"] * color_powers["green"]


def get_power_sum():
    total = 0
    for line in read_lines():
        _, cubes = line.split(":")
        total += get_min_power(cubes)

    return total


print(get_power_sum())
