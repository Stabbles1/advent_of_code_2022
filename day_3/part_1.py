import string

scores = {
    letter: value + 1
    for value, letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)
}


def find_misplaced_item(compartment_1, compartment_2):
    compartment_1_items = {item: 1 for item in compartment_1}
    for compartment_2_item in compartment_2:
        if compartment_2_item in compartment_1_items:
            return compartment_2_item
    raise Exception("Didn't find a duplicate")


def main(input):
    priority_sum = 0
    for backpack in input:
        compartment_1 = backpack[0 : int(len(backpack) / 2)]
        compartment_2 = backpack[int(len(backpack) / 2) :]
        misplaced_item = find_misplaced_item(compartment_1, compartment_2)
        priority_sum += scores[misplaced_item]
    return priority_sum


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(main(f.read().splitlines()))
