"""resolve day8"""

def is_on_edge(row, col, trees):
    """determine if a tree is on an edge"""
    return row == 0 or col == 0 or row == len(trees) - 1 or col == len(trees[0]) - 1

def compute_scenic_scores(trees: list) -> list:
    """compute the tree view"""
    nbrows = len(trees)
    scores = []
    for row in range(0, nbrows):
        nbcols = len(trees[row])
        for col in range(0, nbcols):
            edge = is_on_edge(row, col, trees)
            if not edge:
                up = 0
                for i in range(row - 1, -1, -1):
                    up += 1
                    if trees[row][col] <= trees[i][col]:
                        break
                down = 0
                for i in range(row + 1, len(trees)):
                    down += 1
                    if trees[row][col] <= trees[i][col]:
                        break
                left = 0
                for i in range(col - 1, -1, -1):
                    left += 1
                    if trees[row][col] <= trees[row][i]:
                        break
                right = 0
                for i in range(col + 1, len(trees[row])):
                    right += 1
                    if trees[row][col] <= trees[row][i]:
                        break
                scores.append(up * down * left * right)

    return scores

def count_taller_trees(trees: list) -> int:
    """count taller trees"""
    nbtaller = 0
    nbrows = len(trees)
    for row in range(0, nbrows):
        nbcols = len(trees[row])
        for col in range(0, nbcols):
            taller = True
            edge = is_on_edge(row, col, trees)
            if not edge:
                up = [i for i in range(0, row) if trees[row][col] <= trees[i][col]]
                down = [i for i in range(row + 1, len(trees)) if trees[row][col] <= trees[i][col]]
                left = [i for i in range(0, col) if trees[row][col] <= trees[row][i]]
                right = [i for i in range(col +1, len(trees[row])) if trees[row][col] <= trees[row][i]]

                if len(up) > 0 and len(down) > 0 and len(right) > 0 and len(left) > 0:
                    taller = False

            if taller:
                nbtaller += 1

    return nbtaller

def resolve_p1():
    """resolve p1."""
    trees = []
    with open("day8.txt", "r", encoding="utf-8") as content:
        lines = content.readlines()
        for line in lines:
            trees.append(list(map(int, [*line.strip()])))

        print(f"taller trees = {count_taller_trees(trees)}")

def resolve_p2():
    """resolve p2."""
    trees = []
    with open("day8.txt", "r", encoding="utf-8") as content:
        lines = content.readlines()
        for line in lines:
            trees.append(list(map(int, [*line.strip()])))

        scenic_scores = compute_scenic_scores(trees)
        print(f"max view = {max(scenic_scores)}")

if __name__ == '__main__':
    resolve_p1()
    resolve_p2()
