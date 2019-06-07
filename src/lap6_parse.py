import ply.yacc as yacc

from lap6_lex import lap6_lex

tokens = list(lap6_lex().lextokens)


# def p_program(p):
#     """program : expression"""
#     p[0] = p[1]


def p_expression(p):
    """expression : term"""
    p[0] = p[1]


def p_term(p):
    """term : SYMBOL
            | NUMBER"""
    p[0] = p[1]


def p_term_equals(p):
    """term : SYMBOL EQUALS term"""
    p[1] = p[3]

#
# def p_term_comma(p):
#     """"""


def p_expression_p_plus(p):
    """expression : expression P_PLUS term"""
    p[0] = p[1] + p[3]


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
        except EOFError:
            break
        if not s:
            continue
    result = parser.parse(s)
    print(result)
