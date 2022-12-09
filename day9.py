"""resolve day8"""


def parse_positions(file):
    """parses positions into a dict"""
    positions = []
    lines = file.readlines()
    for line in lines:
        splitted_line = line.strip().split(" ")
        positions.append((splitted_line[0], int(splitted_line[1])))
    return positions


def is_adjacent(head, tail):
    """check if the head and tail are adjacents"""
    xdiff = abs(head[0] - tail[0])
    ydiff = abs(head[1] - tail[1])
    return xdiff <= 1 and ydiff <= 1


def resolve_moves_p1(positions):
    """resolves moves of the tail"""
    visited = {(0, 0)}
    head = tail = (0, 0)
    for tupl in positions:
        for step in range(1, tupl[1] + 1):
            if tupl[0] == "U":
                head = (head[0], head[1] + 1)
                if not is_adjacent(head, tail):
                    tail = (head[0], head[1] - 1)
                    visited.add(tail)
            elif tupl[0] == "R":
                head = (head[0] + 1, head[1])
                if not is_adjacent(head, tail):
                    tail = (head[0] - 1, head[1])
                    visited.add(tail)
            elif tupl[0] == "D":
                head = (head[0], head[1] - 1)
                if not is_adjacent(head, tail):
                    tail = (head[0], head[1] + 1)
                    visited.add(tail)
            else:
                head = (head[0] - 1, head[1])
                if not is_adjacent(head, tail):
                    tail = (head[0] + 1, head[1])
                    visited.add(tail)

    unique_visited = len(visited)

    # print(f"positions visited = {visited}")
    print(f"unique visited = {unique_visited}")

    return unique_visited


def resolve_p1():
    """resolve p1."""
    with open("day9.txt", "r", encoding="utf-8") as content:
        head_positions = parse_positions(content)
        resolve_moves_p1(head_positions)

def move_knot(prev, curr):
    """move a knot"""

    # left/right
    if curr[0] > prev[0]:
        curr = (curr[0] - 1, curr[1])
    if curr[0] < prev[0]:
        curr = (curr[0] + 1, curr[1])

    # up/down
    if curr[1] > prev[1]:
        curr = (curr[0], curr[1] - 1)
    if curr[1] < prev[1]:
        curr = (curr[0], curr[1] + 1)

    return curr

def resolve_moves_p2(positions):
    """resolves moves of te tail"""
    visited = [(0, 0)]
    knots = [(0, 0) for _ in range(0, 10)]
    for tupl in positions:
        for _ in range(0, tupl[1]):
            if tupl[0] == "U":
                knots[0] = (knots[0][0], knots[0][1] + 1)
                for i in range(0, 9):
                    if not is_adjacent(knots[i], knots[i + 1]):
                        knots[i + 1] = move_knot(knots[i], knots[i + 1])
                        if i + 1 == 9:
                            visited.append(knots[9])
            elif tupl[0] == "R":
                knots[0] = (knots[0][0] + 1, knots[0][1])
                for i in range(0, 9):
                    if not is_adjacent(knots[i], knots[i + 1]):
                        knots[i + 1] = move_knot(knots[i], knots[i + 1])
                        if i + 1 == 9:
                            visited.append(knots[9])
            elif tupl[0] == "D":
                knots[0] = (knots[0][0], knots[0][1] - 1)
                for i in range(0, 9):
                    if not is_adjacent(knots[i], knots[i + 1]):
                        knots[i + 1] = move_knot(knots[i], knots[i + 1])
                        if i + 1 == 9:
                            visited.append(knots[9])
            else:
                knots[0] = (knots[0][0] - 1, knots[0][1])
                for i in range(0, 9):
                    if not is_adjacent(knots[i], knots[i + 1]):
                        knots[i + 1] = move_knot(knots[i], knots[i + 1])
                        if i + 1 == 9:
                            visited.append(knots[9])

    unique_visited = len(set(visited))

    print(f"unique visited = {unique_visited}")

    return unique_visited


def resolve_p2():
    """resolve p2."""
    with open("day9.txt", "r", encoding="utf-8") as content:
        head_positions = parse_positions(content)
        resolve_moves_p2(head_positions)

if __name__ == '__main__':
    resolve_p1()
    resolve_p2()
