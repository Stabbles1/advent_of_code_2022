from move import Move
from stack import Stack


def stacks_from_input(crates_input):
    ship = {}
    for line in crates_input[::-1]:  # Reverse the crates so we can pile them on top
        for index, char in enumerate(line[1:-1:4]):
            if index + 1 not in ship:
                ship[index + 1] = Stack()
            if char != " ":
                ship[index + 1].add_crates_to_top([char])
    return ship


def moves_from_input(moves_input):
    moves = []
    for move_input in moves_input:
        moves.append(Move(move_input))
    return moves


def execute_moves(stacks: dict[str, Stack], moves: list[Move]):
    for move in moves:
        removed = stacks[move.origin].remove_crates_from_top(move.quantity)
        stacks[move.destination].add_crates_to_top(removed, CrateMover_version=9001)


def get_top_crates(stacks: dict[str, Stack]):
    top_row = ""
    for stack in stacks.values():
        top_row += stack.crates[-1]
    return top_row


def main(crates_input, moves_input):
    stacks = stacks_from_input(crates_input)
    moves = moves_from_input(moves_input)
    execute_moves(stacks, moves)
    return get_top_crates(stacks)


if __name__ == "__main__":
    with open("crates_input.txt", "r") as f:
        crates_input = f.read().splitlines()
    with open("moves_input.txt", "r") as f:
        moves_input = f.read().splitlines()
    print(main(crates_input, moves_input))
