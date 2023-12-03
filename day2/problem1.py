def read_lines():
    with open("inputs/problem1.txt", "r") as file:
        for line in file:
            yield line.strip()


given_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_game_possible(cubes):
    # 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    for hit in cubes.split(";"):
        for hit_cube in hit.split(","):
            num, color = hit_cube.split()
            if int(num) > given_cubes[color]:
                return False
    return True


def get_ids_sum():
    total = 0
    for line in read_lines():
        game, cubes = line.split(":")
        _, idx = game.split()

        if is_game_possible(cubes):
            total += int(idx)

    return total


print(get_ids_sum())
