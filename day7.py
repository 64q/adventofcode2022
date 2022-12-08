"""resolve day7"""



def sums_of_dirs():
    """sums of dirs"""
    current_directory = []
    directories = {}
    with open("day7.txt", "r", encoding="utf-8") as content:
        lines = content.readlines()
        for line in lines:
            instr = line.strip().split(" ")
            cmd = instr[1]
            cwd = "".join(current_directory)

            if cmd == "ls":
                print("listing files")
            elif cmd == "cd":
                if instr[2] == "..":
                    current_directory.pop()
                else:
                    if instr[2] == "/":
                        current_directory.append("/")
                    else:
                        current_directory.append(instr[2] + "/")
                    if directories.get(cwd) is None:
                        directories[cwd] = 0
            elif instr[0] == "dir":
                print("directory found")
            else:
                if directories.get(cwd) is None:
                    directories[cwd] = 0
                directories[cwd] = directories.get(cwd) + int(instr[0])

            # print(current_directory)

    sorted_dirs = dict(sorted(directories.items(), key=lambda x:len(x[0]), reverse=True))

    for key1, val1 in sorted_dirs.items():
        for key2, _ in sorted_dirs.items():
            if key1 != key2 and key1.startswith(key2):
                # print(f"merging {key1} and {key2}")
                sorted_dirs[key2] = sorted_dirs.get(key2) + val1
                break

    return sorted_dirs

def resolve_p1():
    """resolve p1."""
    sorted_dirs = sums_of_dirs()

    top_dirs = [v for _, v in sorted_dirs.items() if v <= 100000]
    print(f"total={sum(top_dirs)}")

    return top_dirs

def resolve_p2():
    """resolve p2."""
    smallest = [value for _, value in sums_of_dirs().items() \
        if (70000000 - 48518336 + value) >= 30000000]
    print(smallest[0])

if __name__ == '__main__':
    resolve_p1()
    resolve_p2()
