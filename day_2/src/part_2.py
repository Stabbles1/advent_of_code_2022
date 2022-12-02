from enum import Enum


class GameMoves(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0


def get_my_move(their_move: GameMoves, outcome: Outcome) -> GameMoves:
    if outcome == Outcome.DRAW:
        return their_move
    elif outcome == Outcome.WIN:
        if their_move == GameMoves.ROCK:
            return GameMoves.PAPER
        elif their_move == GameMoves.PAPER:
            return GameMoves.SCISSORS
        elif their_move == GameMoves.SCISSORS:
            return GameMoves.ROCK
    elif outcome == Outcome.LOSE:
        if their_move == GameMoves.ROCK:
            return GameMoves.SCISSORS
        elif their_move == GameMoves.PAPER:
            return GameMoves.ROCK
        elif their_move == GameMoves.SCISSORS:
            return GameMoves.PAPER


def main():
    their_move_decoder = {
        "A": GameMoves.ROCK,
        "B": GameMoves.PAPER,
        "C": GameMoves.SCISSORS,
    }

    outcome_decoder = {
        "X": Outcome.LOSE,
        "Y": Outcome.DRAW,
        "Z": Outcome.WIN,
    }

    with open("input.txt", "r") as f:
        games = f.read().splitlines()

    score = 0
    for game in games:
        their_move, outcome = game.split(" ")
        their_move = their_move_decoder[their_move]
        outcome = outcome_decoder[outcome]
        score += get_my_move(their_move, outcome).value + outcome.value

    print(score)


if __name__ == "__main__":
    main()
