"""resolve day4"""

def resolve_p1():
    """resolve p1."""
    acc = 0
    with open("day4.txt", "r", encoding="utf-8") as content:
        lines = content.readlines()
        for line in lines:
            splitted_pair = list(map(lambda x: int(x), [val for inter in line.strip().split(",") for val in inter.split("-")]))
            if splitted_pair[0] >= splitted_pair[2] and splitted_pair[1] <= splitted_pair[3]:
                # elf 1 fully contains
                acc += 1
                continue
            if splitted_pair[2] >= splitted_pair[0] and splitted_pair[3] <= splitted_pair[1]:
                # elf 2 fully contains
                acc += 1

    print(f"Overlap1 = {acc}")

def resolve_p2():
    """resolve p2."""
    acc = 0
    with open("day4.txt", "r", encoding="utf-8") as content:
        lines = content.readlines()
        for line in lines:
            splitted_pair = list(map(lambda x: int(x), [val for inter in line.strip().split(",") for val in inter.split("-")]))

            if splitted_pair[0] >= splitted_pair[2] and splitted_pair[0] <= splitted_pair[3]:
                # elf 1 overlap with elf 2
                acc += 1
                continue
            
            if splitted_pair[2] >= splitted_pair[0] and splitted_pair[2] <= splitted_pair[1]:
                # elf 2 overlap with elf 1
                acc += 1

    print(f"Overlap2 = {acc}")

if __name__ == '__main__':
    resolve_p1()
    resolve_p2()