"""day11"""

from math import floor, prod
import copy

# _state: dict = {
#     0: {
#         "items": [79, 98],
#         "op": lambda x: x * 19,
#         "test": lambda x: 2 if x % 23 == 0 else 3,
#         "seen": 0
#     },
#     1: {
#         "items": [54, 65, 75, 74],
#         "op": lambda x: x + 6,
#         "test": lambda x: 2 if x % 19 == 0 else 0,
#         "seen": 0
#     },
#     2: {
#         "items": [79, 60, 97],
#         "op": lambda x: x ** 2,
#         "test": lambda x: 1 if x % 13 == 0 else 3,
#         "seen": 0
#     },
#     3: {
#         "items": [74],
#         "op": lambda x: x + 3,
#         "test": lambda x: 0 if x % 17 == 0 else 1,
#         "seen": 0
#     }
# }

_state: dict = {
    0: {
        "items": [83, 97, 95, 67],
        "op": lambda x: x * 19,
        "test": lambda x: 2 if x % 17 == 0 else 7,
        "seen": 0
    },
    1: {
        "items": [71, 70, 79, 88, 56, 70],
        "op": lambda x: x + 2,
        "test": lambda x: 7 if x % 19 == 0 else 0,
        "seen": 0
    },
    2: {
        "items": [98, 51, 51, 63, 80, 85, 84, 95],
        "op": lambda x: x + 7,
        "test": lambda x: 4 if x % 7 == 0 else 3,
        "seen": 0
    },
    3: {
        "items": [77, 90, 82, 80, 79],
        "op": lambda x: x + 1,
        "test": lambda x: 6 if x % 11 == 0 else 4,
        "seen": 0
    },
    4: {
        "items": [68],
        "op": lambda x: x * 5,
        "test": lambda x: 6 if x % 13 == 0 else 5,
        "seen": 0
    },
    5: {
        "items": [60, 94],
        "op": lambda x: x + 5,
        "test": lambda x: 1 if x % 3 == 0 else 0,
        "seen": 0
    },
    6: {
        "items": [81, 51, 85],
        "op": lambda x: x * x,
        "test": lambda x: 5 if x % 5 == 0 else 1,
        "seen": 0
    },
    7: {
        "items": [98, 81, 63, 65, 84, 71, 84],
        "op": lambda x: x + 3,
        "test": lambda x: 2 if x % 2 == 0 else 3,
        "seen": 0
    }
}

def handle_items(state, mval, no_worry_mgmt=True, smod=96577):
    """handle items"""
    while len(mval["items"]):
        item = mval["items"].pop(0)
        item = mval["op"](item)
        if no_worry_mgmt:
            item = floor(item / 3)
        mval["seen"] += 1
        state[mval["test"](item)]["items"].append(item % smod)


def resolve_p1(state: dict):
    """resolve p1"""
    for _ in range(1, 21):
        for _, mval in state.items():
            handle_items(state, mval, smod=9699690)
    seens = [x["seen"] for _, x in state.items()]
    print(f"seens={seens}")
    seens.sort(reverse=True)
    print(f"result={prod(seens[:2])}")


def resolve_p2(state: dict):
    """resolve p1"""
    for _ in range(1, 10001):
        for _, mval in state.items():
            handle_items(state, mval, no_worry_mgmt=False, smod=9699690)
    seens = [x["seen"] for _, x in state.items()]
    seens.sort(reverse=True)
    print(f"seens={seens}")
    print(f"result={prod(seens[:2])}")


if __name__ == '__main__':
    resolve_p1(copy.deepcopy(_state))
    resolve_p2(copy.deepcopy(_state))
