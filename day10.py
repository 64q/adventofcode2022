"""day10"""

def parse_positions(file):
    """parses positions into a dict"""
    instructions = []
    lines = file.readlines()
    for line in lines:
        splitted_line = line.strip().split(" ")
        if splitted_line[0] == "noop":
            instructions.append((splitted_line[0], 0))
        else:
            instructions.append((splitted_line[0], int(splitted_line[1])))

    return instructions


def generate_ope(instr):
    """generate an operation"""
    if instr[0] == "noop":
        return [instr]
    return [("noop", 0), instr]

def resolve_p1():
    """resolve p1."""
    X = 1
    cycle = 1
    acc = 0
    intersting_cycles = [20, 60, 100, 140, 180, 220]
    with open("day10.txt", "r", encoding="utf-8") as content:
        instructions = parse_positions(content)
        operations = [] + generate_ope(instructions.pop(0))

        while len(operations) > 0:
            ope = operations.pop(0)
            if len(instructions) > 0:
                operations += generate_ope(instructions.pop(0))
            
            if cycle in intersting_cycles:
                print(f"cycle={cycle} and X={X}")
                acc += (cycle * X)
            
            if ope[0] == "addx":
                X += ope[1]
            
            cycle += 1
    
    print(f"X={X}")
    print(f"Sum={acc}")

def resolve_p2():
    """resolve p2."""
    X = 1
    cycle = 0
    with open("day10.txt", "r", encoding="utf-8") as content:
        instructions = parse_positions(content)
        operations = [] + generate_ope(instructions.pop(0))

        while len(operations) > 0:
            ope = operations.pop(0)
            if len(instructions) > 0:
                operations += generate_ope(instructions.pop(0))
            
            remainder = cycle % 40

            if remainder == 0:
                print()
            
            if X == remainder - 1 or X == remainder or X == remainder + 1:
                print("#", end="")
            else:
                print(".", end="")
            
            if ope[0] == "addx":
                X += ope[1]
            
            cycle += 1

if __name__ == '__main__':
    resolve_p1()
    resolve_p2()
