from dataclasses import dataclass


@dataclass
class Tree:
    height: int
    visible: bool = False
