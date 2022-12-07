"""resolve day5"""

# board = {
#     1: ['N', 'Z'],
#     2: ['D', 'C', 'M'],
#     3: ['P']
# }
board = {
    1: ['F', 'L', 'M', 'W'],
    2: ['F', 'M', 'V', 'Z', 'B'],
    3: ['Q', 'L', 'S', 'R', 'V', 'H'],
    4: ['J', 'T', 'M', 'P', 'Q', 'V', 'S', 'F'],
    5: ['W', 'S', 'L'],
    6: ['W', 'J', 'R', 'M', 'P', 'V', 'F'],
    7: ['F', 'R', 'N', 'P', 'C', 'Q', 'J'],
    8: ['B', 'R', 'W', 'Z', 'S', 'P', 'H', 'V'],
    9: ['W', 'Z', 'H', 'G', 'C', 'J', 'M', 'B']
}

def resolve_p1():
    """resolve p1."""
    board_mode = True
    with open("day5.txt", "r", encoding="utf-8") as content:
        lines = content.readlines()
        for line in lines:
            if line == "\n":
                board_mode = False
                continue

            if not board_mode:
                splitted_line = line.strip().split(" ")
                qty = int(splitted_line[1])
                from_d = int(splitted_line[3])
                to_d = int(splitted_line[5])

                for _ in range(1, qty+1):
                    elt = board.get(from_d).pop(0)
                    print(f"elt = {elt}, from={from_d} to={to_d}")
                    board.get(to_d).insert(0, elt)

    print(board)
    for _, val in board.items():
        print(val[0], end="")

def resolve_p2():
    """resolve p2."""
    board_mode = True
    with open("day5.txt", "r", encoding="utf-8") as content:
        lines = content.readlines()
        for line in lines:
            if line == "\n":
                board_mode = False
                continue

            if not board_mode:
                splitted_line = line.strip().split(" ")
                qty = int(splitted_line[1])
                from_d = int(splitted_line[3])
                to_d = int(splitted_line[5])

                for i in range(1, qty+1):
                    elt = board.get(from_d).pop(0)
                    print(f"elt = {elt}, from={from_d} to={to_d}")
                    board.get(to_d).insert(i - 1, elt)

    print(board)
    for _, val in board.items():
        print(val[0], end="")

if __name__ == '__main__':
    # resolve_p1()
    resolve_p2()