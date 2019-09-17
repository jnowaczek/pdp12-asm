import ply.yacc as yacc

import pdp12_perm_sym
from lap6_lex import lap6_lex

user_symbols = {}

mode = 'lmode'
radix = 8
mem_origin = 0o0000

precedence = (
)


def symbol_lookup(name):
    lower_name = name.lower()
    if mode == 'lmode':
        if lower_name in pdp12_perm_sym.lmode_instructions:
            return pdp12_perm_sym.lmode_instructions[lower_name]['opcode']
    if mode == 'pmode':
        if lower_name in pdp12_perm_sym.pmode_instructions:
            return pdp12_perm_sym.pmode_instructions[lower_name]['opcode']
    return user_symbols[name]


def p_program(p):
    """program : empty
               | program empty
               | program machine_code"""
    if len(p) == 3:
        if p[2] is None:
            p[0] = p[1]
        else:
            p[1].append(p[2])
            p[0] = p[1]
    if len(p) == 2:
        p[0] = []


def p_pseudo_op(p):
    """empty : pseudo_no_args"""


def p_pseudo_no_args(p):
    """pseudo_no_args : OCTAL
                      | DECIMAL
                      | PMODE
                      | LMODE"""
    global radix, mode
    if p[1] == 'OCTAL':
        radix = 8
    elif p[1] == 'DECIMAL':
        radix = 10
    elif p[1] == 'LMODE':
        mode = 'lmode'
    elif p[1] == 'PMODE':
        mode = 'pmode'
    p[0] = None


def p_machine_code(p):
    """machine_code : INSTRUCTION
                    | I INSTRUCTION
                    | INSTRUCTION NUMBER
                    | INSTRUCTION I NUMBER"""
    if mode == 'pmode':
        if len(p) == 2:
            p[0] = symbol_lookup(p[1])
        elif len(p) == 3:
            if p[1] == 'i':
                p[0] = symbol_lookup(p[2]) + 0o400
            else:
                p[0] = symbol_lookup(p[1]) + int(p[2], radix)
        elif len(p) == 4:
            p[0] = symbol_lookup(p[1]) + 0o400 + int(p[3], radix)
    elif mode == 'lmode':
        if len(p) == 2:
            p[0] = symbol_lookup(p[1])
        elif len(p) == 3:
            if p[1] == 'i':
                p[0] = symbol_lookup(p[2]) + 0o20
            else:
                p[0] = symbol_lookup(p[1]) + int(p[2], radix)
        elif len(p) == 4:
            p[0] = symbol_lookup(p[1]) + 0o20 + int(p[3], radix)


def p_set_origin(p):
    """empty : ASTERISK NUMBER"""
    global mem_origin
    mem_origin = int(p[2], base=radix)
    p[0] = None


def p_assignment(p):
    """empty : SYMBOL COMMA
             | SYMBOL EQUALS expression"""
    if p[1] not in user_symbols:
        if p[2] == ',':
            user_symbols.update({p[1]: mem_origin + p.lineno(1)})
        elif p[2] == '=':
            user_symbols.update({p[1]: p[3]})


def p_expression_plus(p):
    """expression : expression PLUS term"""
    if mode == 'lmode':
        p[0] = (p[1] + p[3]) & 0o1777
    if mode == 'pmode':
        p[0] = (p[1] + p[3]) & 0o7777


def p_expression_minus(p):
    """expression : expression MINUS term"""
    # Refer to page 3-5 in "LAP6-DIAL Programmer's Reference Manual"
    if mode == 'lmode':  # One's Complement
        p[0] = (p[1] + p[3]) & 0o1777 - 1
    if mode == 'pmode':  # Two's Complement
        p[0] = (p[1] + p[3]) & 0o7777


def p_expression_and(p):
    """expression : expression AMPERSAND term"""
    p[0] = p[1] & p[3]


def p_expression_or(p):
    """expression : expression EXCLAMATION term"""
    p[0] = p[1] | p[3]


def p_expression_or_symbol(p):
    """expression : term term"""
    p[0] = p[1] | p[2]


def p_expression_term(p):
    """expression : term"""
    p[0] = p[1]


def p_term(p):
    """term : NUMBER
            | DOT"""
    if p[1] == '.':
        return mem_origin + p.lineno(1)
    else:
        p[0] = int(p[1], radix)


def p_error(p):
    print("Illegal symbol '%s'" % p)


def parse(line):
    l = lap6_lex()
    l.input(line)
    tokens = list(l.lextokens)
    p = yacc.yacc()
    return p.parse(line, debug=False)


if __name__ == '__main__':
    lexer = lap6_lex()
    # with open('../test/FRQANA') as listing:
    #     lexer.input(listing.read())
    tokens = list(lexer.lextokens)
    parser = yacc.yacc()

    while True:
        try:
            s = input('pdp12-asm > ')
            result = parser.parse('PMODE\n AND I 300', debug=True)
            print(result)
        except EOFError:
            print('Memory Origin: 0o%04o' % mem_origin)
            print('User Symbols: %s' % user_symbols)
            break
        if not s:
            continue
