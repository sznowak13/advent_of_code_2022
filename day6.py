"""
"""
from collections import deque


def get_input():
    with open('inputs/day6.txt') as f:
        inputs = f.read().split('\n')
    return inputs


def part1():
    """
    """
    inpt = get_input()
    results = []
    distinct_chars_marker = 4
    for msg in inpt:
        bfr = deque(maxlen=distinct_chars_marker)
        for n, ch in enumerate(msg):
            bfr.append(ch)
            if len(set(bfr)) == distinct_chars_marker:
                results.append(n + 1)
                break

    return results


def part2():
    """
    """
    inpt = get_input()
    results = []
    distinct_chars_marker = 14
    for msg in inpt:
        bfr = deque(maxlen=distinct_chars_marker)
        for n, ch in enumerate(msg):
            bfr.append(ch)
            if len(set(bfr)) == distinct_chars_marker:
                results.append(n + 1)
                break

    return results


if __name__ == '__main__':
    print(part1())
    print(part2())
