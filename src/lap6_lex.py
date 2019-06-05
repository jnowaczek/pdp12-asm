import ply.lex as lex


def lap6_lex():
    number_format = 'octal'

    states = (
        ('lmode', 'inclusive'),
        ('pmode', 'inclusive'),
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
        'PLUS',
        'MINUS',
        'DOT',
        'SLASH',
        'TAPE_DIRECTION',
        'INDIRECT',
        'SEMICOLON',
        'SPACE',
        'AMPERSAND',
        'EXCLAMATION',
        'BACKSLASH',

        #####################
        # Pseudo-operations #
        #####################

        # Reference page C-2 of "LAP6-DIAL Programmer's Reference Manual"

        'PMODE',
        'LMODE',
        'SEGMNT',
        'FIELD',
        'PAGE',
        'LISTAPE',
        'DECIMAL',
        'OCTAL',
        'NOLIST',
        'LIST',
        'TEXT',
        'EJECT',
        'ASMIFZ',
        'ASMIFN',
        'ASMIFM',
        'ASMSKP',
        'SAVSYM',
        'LODSYM',
        'ZERO_PAGE',

        # Other
        'NUMBER',
        'SYMBOL',

        ###########################
        # PDP-8 Mode Instructions #
        ###########################

        # Reference page C-7 of "LAP6-DIAL Programmer's Reference Manual"
        # Memory Reference Instructions
        'AND',
        'TAD',
        'ISZ',
        'DCA',
        'JMS',
        'JMP',

        # Group 1 Operate Microinstructions
        'NOP',
        'IAC',
        'RAL',
        'RTL',
        'RAR',
        'RTR',
        'CML',
        'CMA',
        'CLL',
        'CLA',

        # Group 2 Operate Microinstructions
        'HLT',
        'OSR',
        'SKP',
        'SNL',
        'SZL',
        'SZA',
        'SNA',
        'SMA',
        'SPA',

        # Combined Operate Microinstructions
        'CIA',
        'STL',
        'GLK',
        'STA',
        'LAS',

        # IOT Microinstructions
        'ION',
        'IOF',
        'KSF',
        'KCC',
        'KRS',
        'KRB',
        'TSF',
        'TCF',
        'TPC',
        'TLS',
        'CLSK',
        'CLLR',
        'CLAB',
        'CLEN',
        'CLSA',
        'CLBA',
        'CLCA',
        'CDF',
        'CIF',
        'RDF',
        'RIF',
        'RMF',
        'RIB',
        'LINC',

        ##########################
        # LINC Mode Instructions #
        ##########################

        # Reference page C-9 of "LAP6-DIAL Programmer's Reference Manual"
    )

    t_ANY_PLUS = r'\+'
    t_ANY_MINUS = r'\-'
    t_ANY_EXCLAMATION = r'\!'
    t_ANY_COMMA = r'\,'
    t_ANY_EQUALS = r'\='
    t_ANY_SEMICOLON = r'\;'
    t_ANY_ASTERISK = r'\*'
    t_ANY_DOT = r'\.'
    t_ANY_BACKSLASH = r'\\'
    t_ANY_SLASH = r'\/'
    t_ANY_AMPERSAND = r'\&'

    t_lmode_PMODE = r'\bPMODE\b'
    t_pmode_LMODE = r'\bLMODE\b'
    t_ANY_SEGMNT = r'\bSEGMNT\b'
    t_ANY_FIELD = r'\bFIELD\b'
    t_ANY_PAGE = r'\bPAGE\b'
    t_ANY_LISTAPE = r'\bLISTAPE\b'
    t_ANY_DECIMAL = r'\bDECIMAL\b'
    t_ANY_OCTAL = r'\bOCTAL\b'
    t_ANY_NOLIST = r'\bNOLIST\b'
    t_ANY_LIST = r'\bLIST\b'
    t_ANY_TEXT = r'\bTEXT\b'
    t_ANY_EJECT = r'\bEJECT\b'
    t_ANY_ASMIFZ = r'\bASMIFZ\b'
    t_ANY_ASMIFN = r'\bASMIFN\b'
    t_ANY_ASMIFM = r'\bASMIFM\b'
    t_ANY_ASMSKP = r'\bASMSKP\b'
    t_ANY_SAVSYM = r'\bSAVSYM\b'
    t_ANY_LODSYM = r'\bLODSYM\b'
    t_pmode_INDIRECT = r'\bI\b'
    t_pmode_ZERO_PAGE = r'\bZ\b'

    def t_ANY_NUMBER(t):
        r'\d+'
        if number_format == 'octal':
            t.value = int(t.value, base=8)
        elif number_format == 'decimal':
            t.value = int(t.value, base=10)
        return t

    t_SYMBOL = r'[a-zA-Z][a-zA-Z0-9]*'

    def t_ANY_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = ' `\t'

    def t_ANY_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    ###########################
    # PDP-8 Mode Instructions #
    ###########################

    # Reference page C-7 of "LAP6-DIAL Programmer's Reference Manual"

    # Memory Reference Instructions
    t_pmode_AND = r'\bAND\b'
    t_pmode_TAD = r'\bTAD\b'
    t_pmode_ISZ = r'\bISZ\b'
    t_pmode_DCA = r'\bDCA\b'
    t_pmode_JMS = r'\bJMS\b'
    t_pmode_JMP = r'\bJMP\b'

    # Group 1 Operate Microinstructions
    t_pmode_NOP = r'\bNOP\b'
    t_pmode_IAC = r'\bTAC\b'
    t_pmode_RAL = r'\bRAL\b'
    t_pmode_RTL = r'\bRTL\b'
    t_pmode_RAR = r'\bRAR\b'
    t_pmode_RTR = r'\bRTR\b'
    t_pmode_CML = r'\bCML\b'
    t_pmode_CMA = r'\bCMA\b'
    t_pmode_CLL = r'\bCLL\b'
    t_pmode_CLA = r'\bCLA\b'

    # Group 2 Operate Microinstructions
    t_pmode_HLT = r'\bHLT\b'
    t_pmode_OSR = r'\bOSR\b'
    t_pmode_SKP = r'\bSKP\b'
    t_pmode_SNL = r'\bSNL\b'
    t_pmode_SZL = r'\bSZL\b'
    t_pmode_SZA = r'\bSZA\b'
    t_pmode_SNA = r'\bSNA\b'
    t_pmode_SMA = r'\bSMA\b'
    t_pmode_SPA = r'\bSPA\b'

    # Combined Operate Microinstructions
    t_pmode_CIA = r'\bCIA\b'
    t_pmode_STL = r'\bSTL\b'
    t_pmode_GLK = r'\bGLK\b'
    t_pmode_STA = r'\bSTA\b'
    t_pmode_LAS = r'\bLAS\b'

    # IOT Microinstructions
    t_pmode_ION = r'\bION\b'
    t_pmode_IOF = r'\bIOF\b'
    t_pmode_KSF = r'\bKSF\b'
    t_pmode_KCC = r'\bKCC\b'
    t_pmode_KRS = r'\bKRS\b'
    t_pmode_KRB = r'\bKRB\b'
    t_pmode_TSF = r'\bTSF\b'
    t_pmode_TCF = r'\bTCF\b'
    t_pmode_TPC = r'\bTPC\b'
    t_pmode_TLS = r'\bTLS\b'
    t_pmode_CLSK = r'\bCLSK\b'
    t_pmode_CLLR = r'\bCLLR\b'
    t_pmode_CLAB = r'\bCLAB\b'
    t_pmode_CLEN = r'\bCLEN\b'
    t_pmode_CLSA = r'\bCLSA\b'
    t_pmode_CLBA = r'\bCLBA\b'
    t_pmode_CLCA = r'\bCLCA\b'
    t_pmode_CDF = r'\bCDF\b'
    t_pmode_CIF = r'\bCIF\b'
    t_pmode_RDF = r'\bRDF\b'
    t_pmode_RIF = r'\bRIF\b'
    t_pmode_RMF = r'\bRMF\b'
    t_pmode_RIB = r'\bRIB\b'
    t_pmode_LINC = r'\bLINC\b'

    instance = lex.lex()
    instance.begin('pmode')
    return instance


if __name__ == '__main__':
    lexer = lap6_lex()
    with open('../test/test.pal') as listing:
        lexer.input(listing.read())

    for token in lexer:
        print(token)
