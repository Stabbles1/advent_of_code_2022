from tree import Tree


def populate_forest(input):
    forest = []
    for line in input:
        tree_line = []
        for num in line:
            tree_line.append(Tree(height=int(num)))
        forest.append(tree_line)
    return forest


def number_of_trees_sideways(tree_line, tree, start, stop, step):
    print(tree, start, stop, step)
    num_of_trees = 0
    try:
        max_height = -1
        for comp_x in range(start, stop, step):
            print(f"Comparing with {tree_line[comp_x].height=}")
            if tree_line[comp_x].height > max_height:
                max_height = tree_line[comp_x].height
                num_of_trees += 1
                print("+1")
            else:
                print("Failed comparison")
            if tree_line[comp_x].height == 9 or tree_line[comp_x].height == tree.height:
                print("breaking")
                break  # Finish early
    except IndexError:
        print("IndexError")
        return num_of_trees
    return num_of_trees


def set_scenic_score(forest, x, y):
    # Sideways
    trees_to_left = number_of_trees_sideways(forest[y], forest[x][y], x, 0, -1)
    trees_to_right = number_of_trees_sideways(
        forest[y], forest[x][y], x + 1, len(forest), 1
    )
    # trees_above =
    print(f"{forest[x][y]=} {trees_to_left=} {trees_to_right=}")


def find_scenic_scores(forest):
    for x in range(len(forest[0])):
        for y in range(len(forest)):
            set_scenic_score(forest, x, y)
            return

    # Vertical
    for x in range(len(forest[0])):
        for start, stop, step in [(0, len(forest), 1), (len(forest) - 1, 0, -1)]:
            max_height = -1
            y = 0
            for y in range(start, stop, step):
                if forest[y][x].height > max_height:
                    forest[y][x].visible = True
                    max_height = forest[y][x].height


def main(input):
    forest = populate_forest(input)
    find_scenic_scores(forest)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(main(f.read().splitlines()))
