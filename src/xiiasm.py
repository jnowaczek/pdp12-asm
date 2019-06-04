import argparse
import ply.yacc as yacc

from pal_lex import tokens





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PDP-12 PAL-III assembler')
    parser.add_argument('in_file')
    parser.add_argument('out_file')
    args = parser.parse_args()