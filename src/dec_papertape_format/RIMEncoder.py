import pdp12_asm.model as model


def _encode_address(address: int) -> bytes:
    if address > 0o7777:
        raise ValueError(f"Address out of range: {address}")
    # Take upper six bits of address, set the start-of-address bit
    upper = ((address >> 6) & 0x3f) | 0x40
    # Take lower six bits of address
    lower = address & 0x3f
    return bytes([upper, lower])


def _encode_opcode(opcode: int) -> bytes:
    if opcode > 0o7777:
        raise ValueError(f"Opcode out of range: {opcode}")
    # Take upper six bits of instruction
    upper = (opcode >> 6) & 0x3f
    # Take lower six bits of instruction
    lower = opcode & 0x3f
    return bytes([upper, lower])


def _encode_leader(length=1) -> bytes:
    return b'\x80' * length


def encode_instruction(entry: model.ProgramEntry) -> bytes:
    return _encode_address(entry.location) + _encode_opcode(entry.opcode)


class RIMEncoder:
    def __int__(self, leader_length=4):
        self.leader_length = leader_length

    def encode(self, program: model.Program) -> bytes:
        result = bytearray()

        result += _encode_leader(self.leader_length)

        for entry in program.entry_list:
            result += encode_instruction(entry)

        result += _encode_leader(self.leader_length)

        return bytes(result)
