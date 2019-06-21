import ply.lex as lex
import pdp12_perm_sym


def lap6_lex():
    mode = 'lmode'

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

        'P_BASIC',
        'P_MEMORY_REFERENCE',
        'P_OPERATE',
        'P_OPERATE_1',
        'P_OPERATE_2',
        'P_EXTENDED_ARITHMETIC',
        'P_EXTENDED_ARITHMETIC_LONG',
        'P_IO_TRANSFER',
        'P_EXTENDED_MEMORY_0o7',

        'L_BASIC',
        'L_DIRECT',
        'L_ALPHA',
        'L_ALPHA_0o17',
        'L_ALPHA_I',
        'L_ALPHA_I_0o17',
        'L_ALPHA_I_0o5',
        'L_ALPHA_0o37',
        'L_BETA',
        'L_BETA_DSC',
        'L_IOB',
        'L_TAPE',
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
        val = t.value.lower()
        if val in pdp12_perm_sym.pseudo_ops:
            nonlocal mode
            if val == 'lmode':
                mode = 'lmode'
            if val == 'pmode':
                mode = 'pmode'
        if mode == 'lmode':
            if val in pdp12_perm_sym.lmode_instructions:
                t.type = pdp12_perm_sym.lmode_instructions[val]['class']
        if mode == 'pmode':
            if val in pdp12_perm_sym.lmode_instructions:
                t.type = pdp12_perm_sym.pmode_instructions[val]['class']
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
