from enum import Enum


class GameMoves(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def get_score(their_move: GameMoves, my_move: GameMoves):
    if their_move == my_move:
        print(f"Tie, they chose {their_move} I chose {my_move}")
        return my_move.value + 3
    if (
        (their_move == GameMoves.ROCK and my_move == GameMoves.PAPER)
        or (their_move == GameMoves.PAPER and my_move == GameMoves.SCISSORS)
        or (their_move == GameMoves.SCISSORS and my_move == GameMoves.ROCK)
    ):
        print(f"Won, they chose {their_move} I chose {my_move}")
        return my_move.value + 6
    print(f"Lost, they chose {their_move} I chose {my_move}")
    return my_move.value


def main():
    decoder = {
        "A": GameMoves.ROCK,
        "B": GameMoves.PAPER,
        "C": GameMoves.SCISSORS,
        "X": GameMoves.ROCK,
        "Y": GameMoves.PAPER,
        "Z": GameMoves.SCISSORS,
    }

    with open("input.txt", "r") as f:
        games = f.read().splitlines()

    score = 0
    for game in games:
        their_move, my_move = game.split(" ")
        score += get_score(decoder[their_move], decoder[my_move])

    print(score)


if __name__ == "__main__":
    main()
