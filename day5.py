"""
"""
import re


class CargoCrane:
    def __init__(self, cargo_str: str):
        cargo = list(map(lambda s: s[1::2], reversed(cargo_str)))  # cutting out excess spaces and reversing the order
        self.level_str = cargo.pop(0)
        self.col_n = len(self.level_str.split())
        self.cargo = []
        for stack_n, i in enumerate(range(0, len(self.level_str), 2)):  # dude, c'mon, enumerating the range XD
            self.cargo.append([])
            for row in cargo:
                if row[i] != ' ':
                    self.cargo[stack_n].append(row[i])

    def move_cargo_simple(self, how_much, _from, _to):
        for _ in range(how_much):
            self.cargo[_to].append(self.cargo[_from].pop())

    def move_cargo_batch(self, how_much, _from, _to):
        self.cargo[_to].extend(self.cargo[_from][how_much * -1:])
        self.cargo[_from] = self.cargo[_from][:how_much * -1]

    def safe_get_from_stack(self, stack_n, index):
        try:
            return self.cargo[stack_n][index]
        except IndexError:
            return ' '

    def print_cargo(self):
        longest = max(self.cargo, key=len)
        for stack_index in range(len(longest) - 1, -1, -1):
            lvl = []
            for stack_number in range(self.col_n):
                lvl.append(f"[{self.safe_get_from_stack(stack_number, stack_index)}]")
            print(' '.join(lvl))
        print(' '.join([f" {stack_number + 1} " for stack_number in range(self.col_n)]))

    def execute_instruction(self, inst, batch=False):
        how_much, _from, _to = map(int, re.search(r'move\s+(\d+)\s+from\s+(\d+)\s+to\s+(\d+)', inst).groups())
        if batch:
            self.move_cargo_batch(how_much, _from - 1, _to - 1)  # translating from 1 based to 0 based counting
        else:
            self.move_cargo_simple(how_much, _from - 1, _to - 1)  # translating from 1 based to 0 based counting

    def get_last_inserted_items(self) -> str:
        items = ''
        for stack in self.cargo:
            try:
                items += stack[-1]
            except IndexError:
                continue
        return items


def get_input():
    with open('inputs/day5.txt') as f:
        raw_cargo, raw_instructions = f.read().split('\n\n')
        cargo = raw_cargo.split('\n')
        instructions = raw_instructions.split('\n')
    return cargo, instructions


def part1():
    """
    """
    cargo_inpt, instructions_inpt = get_input()
    crane = CargoCrane(cargo_inpt)
    for inst in instructions_inpt:
        crane.execute_instruction(inst)
    return crane.get_last_inserted_items()


def part2():
    """
    """
    cargo_inpt, instructions_inpt = get_input()
    crane = CargoCrane(cargo_inpt)
    for inst in instructions_inpt:
        crane.execute_instruction(inst, batch=True)
    return crane.get_last_inserted_items()


if __name__ == '__main__':
    print(part1())
    print(part2())
