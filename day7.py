"""
"""


class FileSystemInterpreter:
    def __init__(self):
        self.level_pointer = []
        self.file_system = {}

        # starts as an input, can change to 'output' when provided command is printing to console
        self.line_type = 'input'

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
                print(f"{' ' * indent_lvl}- {name} (file, size: {value})")

    def get_dir_sizes(self, curr_location=None) -> tuple[str, int]:
        pass


def get_input():
    with open('inputs/day7_test.txt') as f:
        inputs = f.read().split('\n')
    return inputs


def part1():
    """
    """
    inpt = get_input()
    fsi = FileSystemInterpreter()
    fsi.interpret(inpt)
    fsi.print_file_system()
    return inpt


def part2():
    """
    """
    inpt = get_input()
    return inpt


if __name__ == '__main__':
    print(part1())
    print(part2())
