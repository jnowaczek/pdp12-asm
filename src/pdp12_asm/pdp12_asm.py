import argparse
import textwrap

from __init__ import __version__


def rim_format(assembly):
    raise NotImplementedError()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PDP-12 LAP6-DIAL Assembler',
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-v', '--version', help='print the version number and exit', action='version',
                        version='%(prog)s {}'.format(__version__))
    parser.add_argument('-f', metavar='FORMAT',
                        help=textwrap.dedent(
                            '''\
                            select output file format
                              lst    program listing [default]
                              rim    RIM tape format
                              bin    BIN tape format
                            '''),
                        choices=['lst', 'rim', 'bin'],
                        default='lst')
    parser.add_argument('filename')
    parser.add_argument('-o', dest='outfile', help='write output to outfile')
    args = parser.parse_args()

    # lexer = lap6_lex()
    #
    # with open(args.in_file) as asm:
    #     lexer.input(asm.read())
    #
    #     user_symbols = {}
    #
    #     for token in lexer:  # First pass
    #         if token.type == 'SYMBOL':
    #             if token.value.lower() not in pdp12_perm_sym.all_perm_sym:
    #                 if token.value.lower() not in user_symbols:
    #                     user_symbols[token.value] = {None}
