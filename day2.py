"""resolve day2"""

equiv = {
    'X': 'A', 'Y': 'B', 'Z': 'C'
}

scores = {
    'A': 1, 'B': 2, 'C': 3
}


def calc_score(opp, me):
    """calculate the score."""
    if opp == "A" and me == "C":
        return scores[me]
    if me == "A" and opp == "C":
        return 6 + scores[me]

    if me > opp:
        return 6 + scores[me]
    if me == opp:
        return 3 + scores[me]
    return scores[me]


def resolve_p1():
    """resolve p1."""
    with open("day2.txt", "r", encoding="utf-8") as content:
        lines = content.readlines()
        acc = 0
        for line in lines:
            splitted = line.strip().split(" ")
            acc += calc_score(splitted[0], equiv[splitted[1]])

    print(f"Total p1 = {acc}")
    return acc


def calc_score_p2(opp, outcome):
    """calc score p2."""
    # win
    if outcome == "Z":
        if opp == "C":
            return calc_score(opp, "A")
        return calc_score(opp, chr(ord(opp) + 1))
    # draw
    if outcome == "Y":
        return calc_score(opp, opp)
    # lose
    if opp == "A":
        return calc_score(opp, "C")
    return calc_score(opp, chr(ord(opp) - 1))

def resolve_p2():
    """resolve p2."""
    with open("day2.txt", "r", encoding="utf-8") as content:
        lines = content.readlines()
        acc = 0
        for line in lines:
            splitted = line.strip().split(" ")
            acc += calc_score_p2(splitted[0], splitted[1])

    print(f"Total = {acc}")
    return acc

if __name__ == '__main__':
    score = resolve_p1()
    score2 = resolve_p2()
