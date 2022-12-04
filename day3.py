"""
--- Day 3: Rucksack Reorganization ---

One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately,
that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.
"""
import string

priority_map = {
    letter: i for i, letter in enumerate(string.ascii_letters, start=1)
}


def get_input_part1():
    with open('inputs/day3.txt') as f:
        processed_inpt = [[s[0: len(s) // 2], s[len(s) // 2:]] for s in f.read().split('\n')]
    return processed_inpt


def get_input_part2():
    with open('inputs/day3.txt') as f:
        raw_inpt = f.read().split('\n')
    processed_inpt = [[raw_inpt[i], raw_inpt[i + 1], raw_inpt[i + 2]] for i in range(0, len(raw_inpt) - 1, 3)]
    return processed_inpt


def get_priority(symbol):
    return priority_map[symbol]


def part1():
    """
    Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two
    compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

    The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help
    finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer
    to different types of items).

    The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same
    number of items in each of its two compartments, so the first half of the characters represent items in the first
    compartment, while the second half of the characters represent items in the second compartment.

    For example, suppose you have the following list of contents from six rucksacks:

    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw

        The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items
        vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both
        compartments is lowercase p.
        The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in
        both compartments is uppercase L.
        The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
        The fourth rucksack's compartments only share item type v.
        The fifth rucksack's compartments only share item type t.
        The sixth rucksack's compartments only share item type s.

    To help prioritize item rearrangement, every item type can be converted to a priority:

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.

    In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p),
    38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

    Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item
    types?
    """
    inpt = get_input_part1()

    priority_sum = 0
    for rucksack in inpt:
        comp1 = set(rucksack[0])
        comp2 = set(rucksack[1])
        overlap = comp1 & comp2

        priority_sum += sum(map(get_priority, overlap))

    return priority_sum


def part2():
    """
    --- Part Two ---

    By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

    To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

    In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

    Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

    """
    inpt = get_input_part2()

    priority_sum = 0
    for rucksacks in inpt:
        r1, r2, r3 = map(set, rucksacks)
        overlap = r1 & r2 & r3
        priority_sum += sum(map(get_priority, overlap))

    return priority_sum


if __name__ == '__main__':
    print(part1())
    print(part2())
