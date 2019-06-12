import ply.yacc as yacc

from lap6_lex import lap6_lex

tokens = list(lap6_lex().lextokens)

user_symbols = {}

precedence = (
    ('left', 'PLUS', 'MINUS'),
)


def p_program(p):
    """program : empty
               | program statement SEMICOLON"""


def p_statement(p):
    """statement : empty"""


def p_statement_origin(p):
    """statement : ASTERISK expression"""


def p_equals(p):
    """equals : SYMBOL EQUALS NUMBER"""
    p[1] = p[2]


def p_expression(p):
    """expression : term"""


def p_expression_reduce(p):
    """expression : expression term"""


def p_expression_binary(p):
    """expression : expression PLUS expression
                  | expression MINUS expression"""
    if p[2] == 'PLUS':
        p[0] = p[1] + p[2]
    if p[2] == 'MINUS':
        p[0] = p[1] - p[2]


def p_expression_unary_minus(p):
    """expression : MINUS expression"""
    p[0] = - p[2]


def p_term(p):
    """term : NUMBER"""
    p[0] = p[1]

def p_term_symbol(p):
    """term : SYMBOL"""
    p[0] = p[1]


def p_term_dot(p):
    """term : DOT"""
    p[0] = p.lineno(1)


def p_term_equals(p):
    """term : SYMBOL EQUALS term"""
    p[1] = p[3]


def p_empty(p):
    """empty :"""
    pass


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
    result = parser.parse(s, debug=True)
    print(result)
