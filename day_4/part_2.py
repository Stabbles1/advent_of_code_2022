def create_chores(line):
    chores = []
    for chore in line.split(","):
        chores.append([int(chore) for chore in chore.split("-")])
    return chores


def order_chores_by_max_section(chores):
    if max(chores[0]) < max(chores[1]):
        return chores[0], chores[1]
    else:
        return chores[1], chores[0]


def main(input):
    overlaps = 0
    for line in input:
        lower_sections, higher_sections = order_chores_by_max_section(
            create_chores(line)
        )
        if max(lower_sections) >= min(higher_sections):
            overlaps += 1
    return overlaps


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(main(f.read().splitlines()))
