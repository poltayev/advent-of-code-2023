def read_lines():
    with open("inputs/problem1.txt", "r") as file:
        for line in file:
            yield line.strip()


def has_symbol_neighbor(i, j, engine):
    def is_valid(x, y, engine):
        n, m = len(engine), len(engine[i])
        return 0 <= x < n and 0 <= y < m and engine[x][y] != "."

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]
    for dx, dy in directions:
        nx, ny = dx + i, dy + j
        if is_valid(nx, ny, engine) and not engine[nx][ny].isdigit():
            return True

    return False


def get_line_parts_sum(i, engine):
    total = 0
    j, n = 0, len(engine[i])
    while j < n:
        if not engine[i][j].isdigit():
            j += 1
            continue

        part = ""
        is_number = False
        while j < n and engine[i][j].isdigit():
            if not is_number:
                is_number = has_symbol_neighbor(i, j, engine)

            part += engine[i][j]
            j += 1

        number = int(part or 0)
        if is_number:
            total += number

    return total


def sum_part_numbers():
    lines = read_lines()
    engine, i = [next(lines)], 0
    total = 0
    while True:
        try:
            line = next(lines)
            engine.append(line)
            total += get_line_parts_sum(i, engine)
            i += 1
        except StopIteration:
            break

    total += get_line_parts_sum(i, engine)

    return total


print(sum_part_numbers())
