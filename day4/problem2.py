def read_lines():
    with open("inputs/problem2.txt", "r") as file:
        for line in file:
            yield line.strip()


def get_matches(winning_numbers: set, having_numbers: list):
    count_winnings = 0
    for num in having_numbers:
        if num in winning_numbers:
            count_winnings += 1

    return count_winnings


result = {}


def get_total_points():
    total = 0
    for line in read_lines():
        card, data = line.split(":")
        winning_numbers, having_numbers = data.split("|")
        matches = get_matches(set(winning_numbers.split()), having_numbers.split())

        _, current_card_idx = card.split()
        card_id = int(current_card_idx)
        if card_id not in result:
            result[card_id] = 1

        for idx in range(card_id + 1, card_id + matches + 1):
            if idx not in result:
                result[idx] = 1

            result[idx] += result[card_id]

    total = 0
    for key in result:
        total += result[key]

    return total


print(get_total_points())
