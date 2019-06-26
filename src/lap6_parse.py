import ply.yacc as yacc

import pdp12_perm_sym
from lap6_lex import lap6_lex

tokens = list(lap6_lex().lextokens)

user_symbols = {}

mode = 'lmode'
radix = 'octal'

precedence = (
    ('left', 'PLUS', 'MINUS'),
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
    """program : program machine_code"""
    p[0] = p[1] + '\n' + format(p[2], 'o').zfill(4)


def p_program_machine_code(p):
    """program : machine_code"""
    p[0] = format(p[1], 'o').zfill(4)


def p_lmode_class_basic(p):
    """machine_code : L_BASIC"""
    p[0] = symbol_lookup(p[1])


def p_lmode_class_direct(p):
    # TODO: Check expression value and error case
    """machine_code : L_DIRECT expression"""
    p[0] = symbol_lookup(p[1]) + p[2]


def p_lmode_class_beta(p):
    # TODO: Check expression value and error case
    """machine_code : L_BETA expression
                    | L_BETA I expression"""
    p[0] = symbol_lookup(p[1]) + p[2]
    if p[3]:
        p[0] += p[3]


def p_lmode_class_beta_dsc(p):
    # TODO: Check expression value and error case
    """machine_code : L_BETA_DSC expression
                    | L_BETA_DSC I expression"""
    p[0] = symbol_lookup(p[1]) + p[2]
    if p[3]:
        p[0] += p[3]


def p_lmode_class_alpha(p):
    # TODO: Check expression value and error case
    """machine_code : L_ALPHA expression"""
    p[0] = p[1] + p[2]


def p_lmode_class_alpha_0o17(p):
    # TODO: Check expression value and error case
    """machine_code : L_ALPHA_0o17 expression"""
    p[0] = symbol_lookup(p[1]) + symbol_lookup(p[2])


def p_lmode_class_alpha_0o37(p):
    # TODO: Check expression value and error case
    """machine_code : L_ALPHA_0o37 expression"""
    p[0] = symbol_lookup(p[1]) + symbol_lookup(p[2])


def p_lmode_class_alpha_i(p):
    """machine_code : L_ALPHA_I I
                    | L_ALPHA_I"""
    p[0] = symbol_lookup(p[1])
    if p[2]:
        p[0] += symbol_lookup(p[2])


def p_lmode_class_alpha_i_0o5(p):
    # TODO: Check expression value and error case
    """machine_code : L_ALPHA_I_0o5 I expression
                    | L_ALPHA_I_0o5 expression"""
    p[0] = symbol_lookup(p[1]) + symbol_lookup(p[2])
    if p[3]:
        p[0] += symbol_lookup(p[3])


def p_lmode_class_alpha_i_0o17(p):
    # TODO: Check expression value and error case
    """machine_code : L_ALPHA_I_0o17 I expression
                    | L_ALPHA_I_0o17 expression"""
    p[0] = symbol_lookup(p[1]) + symbol_lookup(p[2])
    if p[3]:
        p[0] += symbol_lookup(p[3])


# def p_lmode_class_iob(p):
#     # TODO: Figure out how to handle 2 word instructions
#     """machine_code : L_IOB"""
#     p[0] = symbol_lookup(p[1]) + symbol_lookup(p[2])
#     if p[3]:
#         p[0] += symbol_lookup(p[3])


def p_lmode_class_tape(p):
    # TODO: Check unit value and error case
    """machine_code : L_TAPE I expression
                    | L_TAPE expression"""
    if p[3]:
        p[0] += symbol_lookup(p[1]) + symbol_lookup(p[2]) + (p[3] & 0o0001)
    else:
        p[0] = symbol_lookup(p[1]) + (p[2] & 0o0001)


def p_pseudo_decimal(p):
    """empty : DECIMAL"""
    radix = 'decimal'


def p_pseudo_octal(p):
    """empty : OCTAL"""
    radix = 'octal'


def p_pseudo_lmode(p):
    """empty : LMODE"""
    mode = 'lmode'


def p_pseudo_pmode(p):
    """empty : PMODE"""
    mode = 'pmode'


def p_expression_plus(p):
    """expression : expression PLUS term"""
    global mode
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
    """term : NUMBER"""
    if radix == 'octal':
        p[0] = int(p[1], 8)
    if radix == 'decimal':
        p[0] = int(p[1], 10)


def p_error(p):
    print("Illegal symbol '%s'" % p)


if __name__ == '__main__':
    lexer = lap6_lex()
    with open('../test/FRQANA') as listing:
        lexer.input(listing.read())
    tokens = list(lexer.lextokens)
    parser = yacc.yacc()

    while True:
        try:
            s = input('pdp12-asm > ')
            result = parser.parse(s, debug=False)
            print(result)
        except EOFError:
            break
        if not s:
            continue
