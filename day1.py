"""resolve day1"""


def resolve_p1():
    """resolve p1."""
    data = []

    with open("day1.txt", "r", encoding="utf-8") as content:
        lines = content.readlines()
        acc = 0
        for line in lines:
            if line != "\n":
                acc += int(line)
            else:
                data.append(acc)
                acc = 0

    data.sort(reverse=True)
    print(f"Total p1 = {data[0]}")
    return data


def resolve_p2(data):
    """resolve p2."""
    cals = sum(data[0:3])
    print(f"Total p2 = {cals}")
    return cals


if __name__ == '__main__':
    sums = resolve_p1()
    resolve_p2(sums)
