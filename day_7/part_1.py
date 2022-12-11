import re
from pathlib import PurePath

from directory import Directory
from file import File

current_location = PurePath("/")
filesystem = {}


def set_location(location):
    global current_location
    if location == "..":
        current_location = PurePath(current_location).parent
    else:
        current_location = current_location.joinpath(PurePath(location))
    print(f"{current_location=}")


def is_directory(line):
    return line[0:4] == "dir "


def add_resource_to_directory(line):
    print(line)
    if current_location not in filesystem:
        filesystem[current_location] = Directory(name=current_location)
        # print(f"Added a new directory: {filesystem[current_location]}")
    if is_directory(line):
        subdirectory = Directory(current_location.joinpath(line[4:]))
        filesystem[current_location.joinpath(line[4:])] = subdirectory
        filesystem[current_location].add_subdirectory(subdirectory)
    else:  # It's a file
        matches = re.search(r"(\d+) (.*)", line)
        if matches:
            filesystem[current_location].add_file(
                File(matches.group(2), int(matches.group(1)))
            )
        else:
            raise Exception(f"No files were found in {line}")


def populate_filesystem(input):
    line_no = 0
    while line_no < len(input):
        print(input[line_no])
        if input[line_no][0] == "$":
            if input[line_no][2:4] == "cd":
                set_location(input[line_no][5:])
            elif input[line_no][2:4] == "ls":
                while line_no + 1 < len(input):
                    if input[line_no + 1][0] == "$":
                        break
                    else:
                        add_resource_to_directory(input[line_no + 1])
                    line_no += 1
        line_no += 1


def get_size_of_filesystem(max_size=100000):
    total = 0
    for dir in filesystem.values():
        # print(dir)
        size = dir.get_size()
        if size <= max_size:
            total += size
    return total


def main(input):
    populate_filesystem(input)
    print(filesystem)
    return get_size_of_filesystem()


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(main(f.read().splitlines()))
