from tree import Tree


def populate_forest(input):
    forest = []
    for line in input:
        tree_line = []
        for num in line:
            tree_line.append(Tree(height=int(num)))
        forest.append(tree_line)
    return forest


def find_visible_trees(forest):
    # Sideways
    for tree_line in forest:
        for direction in (1, -1):
            max_height = -1
            for tree in tree_line[::direction]:
                if tree.height > max_height:
                    tree.visible = True
                    max_height = tree.height
                if tree.height == 9:
                    break  # Finish early
    # Vertical
    for x in range(len(forest[0])):
        for start, stop, step in [(0, len(forest), 1), (len(forest) - 1, 0, -1)]:
            max_height = -1
            y = 0
            for y in range(start, stop, step):
                if forest[y][x].height > max_height:
                    forest[y][x].visible = True
                    max_height = forest[y][x].height


def count_visible_trees(forest):
    count = 0
    for tree_line in forest:
        for tree in tree_line:
            if tree.visible:
                count += 1
    return count


def main(input):
    forest = populate_forest(input)
    find_visible_trees(forest)
    return count_visible_trees(forest)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(main(f.read().splitlines()))
