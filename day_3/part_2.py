import string

SCORES = {
    letter: value + 1
    for value, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)
}

ELF_GROUP_SIZE = 3


def group_backpacks(backpacks):
    grouped_backpacks = []
    i = 0
    while i + ELF_GROUP_SIZE <= len(backpacks):
        grouped_backpacks.append(backpacks[i : i + ELF_GROUP_SIZE])
        i = i + ELF_GROUP_SIZE
    return grouped_backpacks


def find_common_in_group(group):
    item_tracker = {}
    for backpack_number, backpack in enumerate(group):
        for item in backpack:
            if item not in item_tracker:
                item_tracker[item] = {backpack_number}
            else:
                item_tracker[item].add(backpack_number)
                if len(item_tracker[item]) == ELF_GROUP_SIZE:
                    return item


def main(input):
    priority_sum = 0
    grouped_backpacks = group_backpacks(input)
    for group in grouped_backpacks:
        common = find_common_in_group(group)
        priority_sum += SCORES[common]

    return priority_sum


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(main(f.read().splitlines()))
