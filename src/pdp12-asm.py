import argparse

import pdp12_perm_sym
from asm_lexer import lap6_lex


def rim_format(assembly):
    return NotImplementedError()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PDP-12 LAP6-DIAL Assembler')
    parser.add_argument('in_file')
    parser.add_argument('out_file')
    args = parser.parse_args()

    lexer = lap6_lex()

    with open(args.in_file) as asm:
        lexer.input(asm.read())

        user_symbols = {}

        for token in lexer:  # First pass
            if token.type == 'SYMBOL':
                if token.value.lower() not in pdp12_perm_sym.all_perm_sym:
                    if token.value.lower() not in user_symbols:
                        user_symbols[token.value] = {None}
