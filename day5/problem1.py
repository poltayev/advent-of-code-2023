def read_lines():
    with open("inputs/problem1.txt", "r") as file:
        for line in file:
            yield line.strip()


def get_mapping(lines):
    mapping = {}
    for line in lines:
        if not line:
            break

        start_y, start_x, range_length = line.split()
        mapping[(int(start_x), int(range_length))] = int(start_y)

    return mapping


def get_locations():
    lines = read_lines()
    _, input_data = next(lines).split(':')
    source = input_data.split()

    for line in lines:
        if not line:
            continue

        splitted = line.split(':')
        if splitted:
            mapping = get_mapping(lines)
            converter = Converter(source, mapping)
            source = converter.convert()

    return source


class Converter:
    def __init__(self, source, mapping) -> None:
        self.source = source
        self.mapping = mapping

    def convert(self):
        for i, item in enumerate(self.source):
            for start, range_length in self.mapping:
                end = start + range_length - 1
                start_y = self.mapping[(start, range_length)]
                if start <= int(item) <= end:
                    self.source[i] = start_y + (int(item) - start)

        return self.source


print(min(get_locations()))
