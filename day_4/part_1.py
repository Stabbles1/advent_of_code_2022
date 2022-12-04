def create_chores(line):
    chores = []
    for chore in line.split(","):
        chores.append([int(chore) for chore in chore.split("-")])
    return chores


def order_chores_by_size(chores):
    if chores[0][1] - chores[0][0] <= chores[1][1] - chores[1][0]:
        return chores[0], chores[1]
    else:
        return chores[1], chores[0]


def main(input):
    full_overlaps = 0
    for line in input:
        smaller_chores, larger_chores = order_chores_by_size(create_chores(line))
        if min(smaller_chores) >= min(larger_chores) and max(smaller_chores) <= max(
            larger_chores
        ):
            full_overlaps += 1
    return full_overlaps


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(main(f.read().splitlines()))
