import ply.lex as lex

import pdp12_asm.pdp12_perm_sym as pdp12_perm_sym


def lap6_lex():
    mode = 'lmode'

    tokens = (
        'COMMA',
        'ASTERISK',
        'STATEMENT_END',
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
        'P_OPERATE_1',
        'P_OPERATE_2',
        'P_EXTENDED_ARITHMETIC',
        'P_EXTENDED_ARITHMETIC_LONG',
        'P_CLA',

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
            # Not-so-pretty separation of "microcoded" instruction classes for special handling
            nonlocal mode
            t.type = 'INSTRUCTION'
            if mode == 'pmode' and pdp12_perm_sym.all_instructions[t.value.lower()]['class'] in ['P_OPERATE_1',
                                                                                                 'P_OPERATE_2',
                                                                                                 'P_EXTENDED_ARITHMETIC',
                                                                                                 'P_EXTENDED_ARITHMETIC_LONG',
                                                                                                 'P_CLA']:
                t.type = pdp12_perm_sym.all_instructions[t.value.lower()]['class']
        elif t.value.lower() in pdp12_perm_sym.all_pseudo_op:
            if t.value.lower() == 'pmode' or t.value.lower() == 'lmode':
                mode = t.value.lower()
            t.type = t.value.upper()
        return t

    def t_semicolon(t):
        r""";"""
        t.type = 'STATEMENT_END'
        return t

    def t_newline(t):
        r"""\n|\r|\r\n|\f"""
        t.lexer.lineno += 1
        t.type = 'STATEMENT_END'
        return t

    t_ignore = ' \t;'

    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    instance = lex.lex()
    return instance


if __name__ == '__main__':
    lexer = lap6_lex()
    with open('../test/RIMLOADER') as listing:
        lexer.input(listing.read())

    for token in lexer:
        print(token)
