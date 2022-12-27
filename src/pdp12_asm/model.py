class ProgramEntry:
    def __init__(self, location: int, opcode: int):
        self.location = location
        self.opcode = opcode

    def __repr__(self):
        return f'{self.location:0>4o} {self.opcode:0>4o}'

    def __eq__(self, other):
        if not isinstance(other, ProgramEntry):
            return False
        return self.location == other.location and self.opcode == other.opcode


class Program:
    def __init__(self):
        self.entry_list = []

    def append(self, entry: ProgramEntry):
        self.entry_list.append(entry)

    def __repr__(self):
        return "".join(repr(self.entry_list))

    def __eq__(self, other):
        if not isinstance(other, Program):
            return False
        return self.entry_list == other.entry_list
