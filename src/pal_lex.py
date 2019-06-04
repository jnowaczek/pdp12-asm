import ply.lex as lex

tokens = (
    # PAL-III Punctuation
    'PLUS',
    'MINUS',
    'COMMA',
    'EQUALS',
    'ASTERISK',
    'SEMICOLON',
    'DOLLAR_SIGN',
    'POINT',
    'SLASH',
    # Pseudo-operations
    'DECIMAL',
    'OCTAL',
    'PAUSE',
    'FIELD',
    'EXPUNGE',
    'FIXTAB',
    'FIXMRI',
    'INDIRECT',
    'PAGE_ZERO',
    # Other
    'NUMBER',
    'SYMBOL',
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_COMMA = r'\,'
t_EQUALS = r'\='
t_ASTERISK = r'\*'
t_SEMICOLON = r'\;'
t_DOLLAR_SIGN = r'\$'
t_POINT = r'\.'
t_SLASH = r'\/'

t_DECIMAL = r'DECIMAL'
t_OCTAL = r'OCTAL'
t_PAUSE = r'PAUSE'
t_FIELD = r'FIELD'
t_EXPUNGE = r'EXPUNGE'
t_FIXTAB = r'FIXTAB'
t_FIXMRI = r'FIXMRI'
t_INDIRECT = r'\bI\b'
t_PAGE_ZERO = r'\bZ\b'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_SYMBOL = r'[a-zA-Z][a-zA-Z0-9]*'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' `\t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


if __name__ == '__main__':
    lexer = lex.lex()
    with open('../test/test.pal') as listing:
        lexer.input(listing.read())

    for token in lexer:
        print(token)
