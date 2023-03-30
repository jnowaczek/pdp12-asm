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


def _encode_leader(length) -> bytes:
    return b'\x80' * length


def encode_instruction(entry: model.ProgramEntry) -> bytes:
    return _encode_address(entry.location) + _encode_opcode(entry.opcode)


def encode(program: model.Program) -> bytes:
    result = bytearray()

    for entry in program.entry_list:
        result += encode_instruction(entry)

    return bytes(result)


def pad_leader(data: bytes, leader_length: int) -> bytes:
    return bytes(_encode_leader(leader_length) + data + _encode_leader(leader_length))


def encode_and_pad(program: model.Program, leader_length: int = 4) -> bytes:
    return pad_leader(encode(program), leader_length)
