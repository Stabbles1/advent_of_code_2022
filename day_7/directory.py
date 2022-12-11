from file import File


class Directory:
    def __init__(self, name) -> None:
        self.name: str = name
        self.files: dict[str, File] = {}
        self.subdirectories: dict = {}

    def add_file(self, file: File):
        self.files[file.name] = file

    def add_subdirectory(self, directory):
        self.subdirectories[directory.name] = directory

    def get_size(self):
        total = 0
        for file in self.files.values():
            total += file.size
        for directory in self.subdirectories.values():
            total += directory.get_size()
        print(f"The size of {self.name} is {total}")
        return total

    def __repr__(self):
        return f"Directory:{self.name} files:{len(self.files)} subdirs:{len(self.subdirectories)}"
