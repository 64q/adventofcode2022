"""resolve day3"""

data = []

def equiv_score(val):
    print(val)
    if val.isupper():
        return ord(val) - 38
    return ord(val) - 96

def calculate_score(data: list) -> int:
    """calculate score"""
    return sum(map(equiv_score, data))

def resolve_p1():
    """resolve p1."""
    with open("day3.txt", "r", encoding="utf-8") as content:
        lines = content.readlines()
        for line in lines:
            first_half = [*line.strip()][:len(line)//2]
            second_half = [*line.strip()][len(line)//2:]
            intersect = [value for value in first_half if value in second_half]
            data.extend(list(dict.fromkeys(intersect)))

    score = calculate_score(data)
    print(f"score = {score}")
    return score


def resolve_p2():
    """resolve p2."""
    with open("day3.txt", "r", encoding="utf-8") as content:
        lines = iter(content.readlines())
        for line in lines:
            first_line = [*line.strip()]
            second_line = [*next(lines).strip()]
            third_line = [*next(lines).strip()]
            intersect = [value for value in first_line if value in second_line and value in third_line]
            # print(intersect)
            data.extend(list(dict.fromkeys(intersect)))

    print(data)
    score = calculate_score(data)
    print(f"score = {score}")
    return score

if __name__ == '__main__':
    # resolve_p1()
    resolve_p2()