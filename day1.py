import functools


def top3calories(processed_inpt: list):
    calorie_sums = [functools.reduce(lambda x, y: int(x) + int(y), calories, 0) for calories in processed_inpt]
    return sorted(calorie_sums, reverse=True)


def main1():
    with open('inputs/day1.txt') as f:
        processed_inpt = [s.split('\n') for s in f.read().split('\n\n')]

    sums = top3calories(processed_inpt)

    return max(sums)


def main2():
    with open('inputs/day1.txt') as f:
        processed_inpt = [s.split('\n') for s in f.read().split('\n\n')]

    sums = top3calories(processed_inpt)

    return sums[:3]


if __name__ == '__main__':
    print(main1())
    print(main2())
