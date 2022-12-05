class Stack:
    def __init__(self):
        self.crates = []

    def add_crates_to_top(self, letters: list[str], CrateMover_version=9000):
        if CrateMover_version <= 9000:
            letters.reverse()
        self.crates += letters

    def remove_crates_from_top(self, quantity):
        removed_crates = self.crates[-quantity:]
        self.crates = self.crates[:-quantity]
        return removed_crates

    def __repr__(self):
        return f"Crates:{self.crates}"
