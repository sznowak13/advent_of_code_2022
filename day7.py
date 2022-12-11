"""
"""


from pprint import pprint


class FileSystemInterpreter:
    def __init__(self):
        self.level_pointer = []
        self.file_system = {}

        # starts as an input, can change to 'output' when provided command is printing to console
        self.line_type = 'input'

    def interpret_from_file(self, file_path):
        with open(file_path) as f:
            inputs = f.read().split('\n')
        self.interpret(inputs)

    def interpret_from_str(self, str_):
        inputs = str_.split('\n')
        self.interpret(inputs)

    def interpret(self, command_list: list[str]):
        for command in command_list:
            cmd = command.split()
            if cmd[0] == '$':
                if cmd[1] == 'cd':
                    if cmd[2] == '..':
                        self.level_pointer.pop()
                    elif cmd[2] == '/':
                        self.level_pointer = []
                    else:
                        self.level_pointer.append(cmd[2])
            else:
                if cmd[0] == 'dir':
                    self.add_dir_to_current_location(cmd[1])
                else:
                    self.add_file_to_current_location(*cmd)

    def add_dir_to_current_location(self, dir_name: str):
        curr_location = self.file_system
        for path in self.level_pointer:
            curr_location = curr_location[path]
        curr_location[dir_name] = {}

    def add_file_to_current_location(self, file_size: str, file_name: str):
        curr_location = self.file_system
        for path in self.level_pointer:
            curr_location = curr_location[path]
        curr_location[file_name] = int(file_size)

    def print_working_directory(self):
        curr_location = self.file_system
        for path in self.level_pointer:
            curr_location = curr_location[path]
        print(curr_location)

    def print_file_system(self, indent_lvl: int = 2, curr_location=None):
        if curr_location is None:
            print("- / (dir)")
            curr_location = self.file_system
        for name, value in curr_location.items():
            if type(value) == dict:
                print(f"{' ' * indent_lvl}- {name} (dir)")
                self.print_file_system(indent_lvl + 2, value)
            else:
                print(f"{' ' * indent_lvl}- {name} (file, size: {value:_})")

    def get_dir_sizes(self, curr_location: dict = None, dir_name: str = '/', indent_lvl: int = 2) -> tuple[str, int]:
        str_builder = []
        if curr_location is None:
            str_builder.append("- / (dir)")
            curr_location = self.file_system
        sizes = {dir_name: 0}
        for name, value in curr_location.items():
            item_path = '/'.join([dir_name, name])
            if isinstance(value, dict):
                sub_dir_size, sub_str = self.get_dir_sizes(
                    value, item_path, indent_lvl + 2)
                sizes[dir_name] += sub_dir_size[item_path]
                if item_path in sizes:
                    print(f'{item_path=} eoeoeoeoeo')
                sizes.update(sub_dir_size)
                str_builder.append(
                    f"{' ' * indent_lvl}- {item_path} (dir, size: {sizes[item_path]:_})")
                str_builder.extend(sub_str)
            else:
                sizes[dir_name] += value
                str_builder.append(
                    f"{' ' * indent_lvl}- {name} (file, size: {value:_})")

        return sizes, str_builder


def get_input():
    with open('inputs/day7.txt') as f:
        inputs = f.read().split('\n')
    return inputs


def part1():
    """
    """
    inpt = get_input()
    fsi = FileSystemInterpreter()
    fsi.interpret(inpt)
    dir_sizes, _ = fsi.get_dir_sizes()
    d2 = {k: v for k, v in dir_sizes.items() if v <= 100_000}
    return sum(
        v for _, v in d2.items()
    )


def part2():
    """
    70_000_000
    30_000_000
    """
    inpt = get_input()
    fsi = FileSystemInterpreter()
    fsi.interpret(inpt)
    dir_sizes, _ = fsi.get_dir_sizes()
    total_disk_space = 70_000_000
    required_free_space = 30_000_000
    current_free_space = total_disk_space - dir_sizes['/']
    needed_free_space = required_free_space - current_free_space
    directory_candidates = {k: v for k,
                            v in dir_sizes.items() if v >= needed_free_space}
    return min(directory_candidates.values())


if __name__ == '__main__':
    print(part1())
    print(part2())
