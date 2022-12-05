import re


class Move:
    def __init__(self, move_text):
        matches = re.search(r"move (\d+) from (\d+) to (\d+)", move_text)
        if matches is None:
            raise Exception("Invalid move input")
        self.quantity = int(matches.group(1))
        self.origin = int(matches.group(2))
        self.destination = int(matches.group(3))

    def __repr__(self):
        return f"{self.quantity=} {self.origin=} {self.destination=}"
