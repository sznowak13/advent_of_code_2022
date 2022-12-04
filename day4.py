"""
--- Day 4: Camp Cleanup ---

Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been
assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a
range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the
assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big
list of the section assignments for each pair (your puzzle input).
"""


def get_input():
    with open('inputs/day4.txt') as f:
        processed_inpt = [s.split(',') for s in f.read().split('\n')]
    return processed_inpt


class Sector:
    def __init__(self, sector_str: str):
        self.start, self.end = map(int, sector_str.split('-'))

    def __str__(self):
        return f"<Sector object [{self.start}-{self.end}]>"

    def __contains__(self, other):
        if self.start >= other.start and self.end <= other.end:
            return True
        return False

    def __and__(self, other):
        if self.end >= other.start and self.start <= other.end:
            return True
        return False


def part1():
    """
    For example, consider the following list of section assignment pairs:

    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8

    For the first few pairs, this list means:

        Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the
        second Elf was assigned sections 6-8 (sections 6, 7, 8). The Elves in the second pair were each assigned two
        sections. The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7,
        while the other also got 7, plus 8 and 9.

    This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger
    numbers. Visually, these pairs of section assignments look like this:

    .234.....  2-4
    .....678.  6-8

    .23......  2-3
    ...45....  4-5

    ....567..  5-7
    ......789  7-9

    .2345678.  2-8
    ..34567..  3-7

    .....6...  6-6
    ...456...  4-6

    .23456...  2-6
    ...45678.  4-8

    Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully
    contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other,
    one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem
    like the most in need of reconsideration. In this example, there are 2 such pairs.

    In how many assignment pairs does one range fully contain the other?
    """
    inpt = get_input()

    fully_overlapping_pairs = 0
    for sector1, sector2 in inpt:
        s1 = Sector(sector1)
        s2 = Sector(sector2)
        if s1 in s2 or s2 in s1:
            fully_overlapping_pairs += 1

    return fully_overlapping_pairs


def part2():
    """
    It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the
    number of pairs that overlap at all.

    In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (
    5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

        5-7,7-9 overlaps in a single section, 7.
        2-8,3-7 overlaps all of the sections 3 through 7.
        6-6,4-6 overlaps in a single section, 6.
        2-6,4-8 overlaps in sections 4, 5, and 6.

    So, in this example, the number of overlapping assignment pairs is 4.

    In how many assignment pairs do the ranges overlap?

    """

    inpt = get_input()

    overlapping_pairs = 0
    for sector1, sector2 in inpt:
        s1 = Sector(sector1)
        s2 = Sector(sector2)
        if s1 & s2:
            overlapping_pairs += 1

    return overlapping_pairs


if __name__ == '__main__':
    print(part1())
    print(part2())