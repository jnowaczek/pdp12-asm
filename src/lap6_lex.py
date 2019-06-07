import ply.lex as lex


def lap6_lex():
    number_format = 'octal'

    states = (
        ('lmode', 'inclusive'),
        ('pmode', 'inclusive'),
        ('comment', 'exclusive')
    )

    tokens = (
        #########################
        # LAP6-DIAL Punctuation #
        #########################

        # Reference Page C-10 "LAP6-DIAL Programmer's Reference Manual"
        # http://www.bitsavers.org/pdf/dec/pdp12/lap6-dial/DEC-12-SE2D-D_LAP6-DIAL.pdf

        'COMMA',
        'ASTERISK',
        'EQUALS',
        'L_PLUS',
        'P_PLUS',
        'L_MINUS',
        'P_MINUS',
        'DOT',
        'COMMENT',
        'TAPE_DIRECTION',
        'AMPERSAND',
        'EXCLAMATION',
        'BACKSLASH',

        #####################
        # Pseudo-operations #
        #####################

        # Reference page C-2 of "LAP6-DIAL Programmer's Reference Manual"

        'ASMIFZ',
        'ASMIFN',
        'ASMIFM',
        'ASMSKP',
        'DECIMAL',
        'EJECT',
        'FIELD',
        'INDIRECT',
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
        'ZERO_PAGE',

        # Other
        'NUMBER',
        'SYMBOL',
        'P_INSTR',
        'L_INSTR',
    )

    ###########################
    # PDP-8 Mode Instructions #
    ###########################

    # Reference page C-7 of "LAP6-DIAL Programmer's Reference Manual"
    p_mneumonic = [
        # Memory Reference Instructions
        'AND', 'TAD', 'ISZ', 'DCA', 'JMS', 'JMP',
        # Group 1 Operate Microinstructions
        'NOP', 'IAC', 'RAL', 'RTL', 'RAR', 'RTR', 'CML', 'CMA', 'CLL', 'CLA',
        # GrouP 2 Operate Microinstructions
        'HLT', 'OSR', 'SKP', 'SNL', 'SZL', 'SZA', 'SNA', 'SMA', 'SPA',
        # Combined Operate Microinstructions
        'CIA', 'STL', 'GLK', 'STA', 'LAS',
        # IOT Microinstructions
        'ION', 'IOF', 'KSF', 'KCC', 'KRS', 'KRB', 'TSF', 'TCF', 'TPC', 'TLS', 'CLSK', 'CLLR', 'CLAB', 'CLEN', 'CLSA',
        'CLBA', 'CLCA', 'CDF', 'CIF', 'RDF', 'RIF', 'RMF', 'RIB', 'LINC',
    ]

    ##########################
    # LINC Mode Instructions #
    ##########################

    # Reference page C-9 of "LAP6-DIAL Programmer's Reference Manual"
    l_mneumonic = [
        # Add
        'ADD', 'ADA', 'ADM', 'LAM',
        # Multiply
        'MUL',
        # Load
        'LDA', 'LDH',
        # Store
        'STC', 'STA', 'STH',
        # Shift/Rotate
        'ROL', 'ROR', 'SCR',
        # Operate
        'HLT', 'NOP', 'CLR', 'SET', 'JMP', 'QAC',
        # Logical Operations
        'BCL', 'BSE', 'BCO', 'COM',
        # Skip
        'SAE', 'SHD', 'SNS', 'SKP', 'AZE', 'APO', 'LZE', 'FLO', 'QLZ', 'SXL', 'KST', 'SRO', 'XSK', 'STD',
        # Input/Output
        'ATR', 'RTA', 'SAM', 'DIS', 'DSC', 'PDP', 'RSW', 'LSW', 'IOB',
        # Memory
        'LIF', 'LDF',
        # LINC Tape
        'RDE', 'RDC', 'RCG', 'WRI', 'WRC', 'WCG', 'CHK', 'MTB', 'XOA',
        # Extended Operations
        'ESF', 'TAC', 'TMA', 'AXO', 'DJR', 'MSC', 'SFA',
    ]

    t_lmode_L_PLUS = r'\+'
    t_pmode_P_PLUS = r'\+'
    t_lmode_L_MINUS = r'\-'
    t_pmode_P_MINUS = r'\-'
    t_EXCLAMATION = r'\!'
    t_COMMA = r'\,'
    t_EQUALS = r'\='
    # t_SEMICOLON = r'\;' "Terminates coding line"
    t_ASTERISK = r'\*'
    t_DOT = r'\.'

    def t_COMMENT(t):
        r"""\/[^\r\n|\r|\n]*"""
        t.lexer.push_state('comment')
        return t

    def t_comment_newline(t):
        r"""[\r\n|\r|\n]+"""
        t.lexer.lineno += len(t.value)
        t.lexer.pop_state()

    t_BACKSLASH = r'\\'
    t_AMPERSAND = r'\&'

    def t_lmode_PMODE(t):
        r"""\bPMODE\b"""
        t.lexer.begin('pmode')
        return t

    def t_pmode_LMODE(t):
        r"""\bLMODE\b"""
        t.lexer.begin('lmode')
        return t

    t_SEGMNT = r'\bSEGMNT\b'
    t_FIELD = r'\bFIELD\b'
    t_PAGE = r'\bPAGE\b'
    t_LISTAPE = r'\bLISTAPE\b'
    t_DECIMAL = r'\bDECIMAL\b'
    t_OCTAL = r'\bOCTAL\b'
    t_NOLIST = r'\bNOLIST\b'
    t_LIST = r'\bLIST\b'
    t_TEXT = r'\bTEXT\b'
    t_EJECT = r'\bEJECT\b'
    t_ASMIFZ = r'\bASMIFZ\b'
    t_ASMIFN = r'\bASMIFN\b'
    t_ASMIFM = r'\bASMIFM\b'
    t_ASMSKP = r'\bASMSKP\b'
    t_SAVSYM = r'\bSAVSYM\b'
    t_LODSYM = r'\bLODSYM\b'
    t_pmode_INDIRECT = r'\bI\b'
    t_pmode_ZERO_PAGE = r'\bZ\b'

    def t_NUMBER(t):
        r"""\d+"""
        if number_format == 'octal':
            t.value = int(t.value, base=8)
        elif number_format == 'decimal':
            t.value = int(t.value, base=10)
        return t

    def t_SYMBOL(t):
        r"""[a-zA-Z][a-zA-Z0-9]*"""
        if t.lexer.lexstate == 'lmode':
            if t.value in l_mneumonic:
                t.type = 'L_INSTR'
                return t
        if t.lexer.lexstate == 'pmode':
            if t.value in l_mneumonic:
                t.type = 'P_INSTR'
                return t
        return t

    def t_newline(t):
        r"""(\n|\\n)+"""
        t.lexer.lineno += len(t.value)

    t_ANY_ignore = ' \t;'

    def t_ANY_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    instance = lex.lex()
    instance.begin('pmode')
    return instance


if __name__ == '__main__':
    lexer = lap6_lex()
    with open('../test/FRQANA') as listing:
        lexer.input(listing.read())

    for token in lexer:
        print(token)
