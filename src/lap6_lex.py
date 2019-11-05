import ply.lex as lex

import pdp12_perm_sym


def lap6_lex():
    tokens = (
        'COMMA',
        'ASTERISK',
        'SEMICOLON',
        'EQUALS',
        'PLUS',
        'MINUS',
        'DOT',
        'TAPE_DIRECTION',
        'AMPERSAND',
        'EXCLAMATION',
        'BACKSLASH',

        'NUMBER',
        'SYMBOL',
        'INSTRUCTION',

        'ASMIFZ',
        'ASMIFN',
        'ASMIFM',
        'ASMSKP',
        'DECIMAL',
        'EJECT',
        'FIELD',
        'I',
        'LIST',
        'LISTAPE',
        'LMODE',
        'LODSYM',
        'NOLIST',
        'OCTAL',
        'PAGE',
        'PMODE',
        'SAVSYM',
        'SEGMNT',
        'TEXT',
        'Z',
    )

    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_EXCLAMATION = r'\!'
    t_COMMA = r'\,'
    t_EQUALS = r'\='
    t_SEMICOLON = r'\;'
    t_ASTERISK = r'\*'
    t_DOT = r'\.'

    def t_COMMENT(t):
        r"""\/[^\r\n|\r|\n]*"""

    def t_NUMBER(t):
        r"""\d+"""
        return t

    def t_SYMBOL(t):
        r"""[a-zA-Z][a-zA-Z0-9]*"""
        if t.value.lower() in pdp12_perm_sym.all_instructions:
            t.type = 'INSTRUCTION'
        elif t.value.lower() in pdp12_perm_sym.all_pseudo_op:
            t.type = t.value.upper()
        return t

    def t_NEWLINE(t):
        r"""\n|\r|\r\n|\f"""
        t.lexer.lineno += 1

    t_ignore = ' \t;'

    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    instance = lex.lex()
    return instance


if __name__ == '__main__':
    lexer = lap6_lex()
    with open('../test/FRQANA') as listing:
        lexer.input(listing.read())

    for token in lexer:
        print(token)
