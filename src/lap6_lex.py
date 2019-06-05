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
        'PLUS',
        'MINUS',
        'DOT',
        'COMMENT',
        'TAPE_DIRECTION',
        'SEMICOLON',
        'SPACE',
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

        ###########################
        # PDP-8 Mode Instructions #
        ###########################

        # Reference page C-7 of "LAP6-DIAL Programmer's Reference Manual"
        # Memory Reference Instructions
        'P_AND',
        'P_TAD',
        'P_ISZ',
        'P_DCA',
        'P_JMS',
        'P_JMP',

        # Group 1 Operate Microinstructions
        'P_NOP',
        'P_IAC',
        'P_RAL',
        'P_RTL',
        'P_RAR',
        'P_RTR',
        'P_CML',
        'P_CMA',
        'P_CLL',
        'P_CLA',

        # GrouP 2 Operate Microinstructions
        'P_HLT',
        'P_OSR',
        'P_SKP',
        'P_SNL',
        'P_SZL',
        'P_SZA',
        'P_SNA',
        'P_SMA',
        'P_SPA',

        # Combined Operate Microinstructions
        'P_CIA',
        'P_STL',
        'P_GLK',
        'P_STA',
        'P_LAS',

        # IOT Microinstructions
        'P_ION',
        'P_IOF',
        'P_KSF',
        'P_KCC',
        'P_KRS',
        'P_KRB',
        'P_TSF',
        'P_TCF',
        'P_TPC',
        'P_TLS',
        'P_CLSK',
        'P_CLLR',
        'P_CLAB',
        'P_CLEN',
        'P_CLSA',
        'P_CLBA',
        'P_CLCA',
        'P_CDF',
        'P_CIF',
        'P_RDF',
        'P_RIF',
        'P_RMF',
        'P_RIB',
        'P_LINC',

        ##########################
        # LINC Mode Instructions #
        ##########################

        # Reference page C-9 of "LAP6-DIAL Programmer's Reference Manual"
        # Add
        'L_ADD',
        'L_ADA',
        'L_ADM',
        'L_LAM',

        # Multiply
        'L_MUL',

        # Load
        'L_LDA',
        'L_LDH',

        # Store
        'L_STC',
        'L_STA',
        'L_STH',

        # Shift/Rotate
        'L_ROL',
        'L_ROR',
        'L_SCR',

        # Operate
        'L_HLT',
        'L_NOP',
        'L_CLR',
        'L_SET',
        'L_JMP',
        'L_QAC',

        # Logical Operations
        'L_BCL',
        'L_BSE',
        'L_BCO',
        'L_COM',

        # Skip
        'L_SAE',
        'L_SHD',
        'L_SNS',
        'L_SKP',
        'L_AZE',
        'L_APO',
        'L_LZE',
        'L_FLO',
        'L_QLZ',
        'L_SXL',
        'L_KST',
        'L_SRO',
        'L_XSK',
        'L_STD',

        # Input/Output
        'L_ATR',
        'L_RTA',
        'L_SAM',
        'L_DIS',
        'L_DSC',
        'L_PDP',
        'L_RSW',
        'L_LSW',
        'L_IOB',

        # Memory
        'L_LIF',
        'L_LDF',

        # LINC Tape
        'L_RDE',
        'L_RDC',
        'L_RCG',
        'L_WRI',
        'L_WRC',
        'L_WCG',
        'L_CHK',
        'L_MTB',
        'L_XOA',

        # Extended Operations
        'L_ESF',
        'L_TAC',
        'L_TMA',
        'L_AXO',
        'L_DJR',
        'L_MSC',
        'L_SFA',
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
        r'\/[^\r\n|\r|\n]*'
        t.lexer.push_state('comment')
        return t

    def t_comment_newline(t):
        r'[\r\n|\r|\n]+'
        t.lexer.lineno += len(t.value)
        t.lexer.pop_state()

    t_BACKSLASH = r'\\'
    t_AMPERSAND = r'\&'

    t_lmode_PMODE = r'\bPMODE\b'
    t_pmode_LMODE = r'\bLMODE\b'
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
        r'\d+'
        if number_format == 'octal':
            t.value = int(t.value, base=8)
        elif number_format == 'decimal':
            t.value = int(t.value, base=10)
        return t

    t_SYMBOL = r'[a-zA-Z][a-zA-Z0-9]*'

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ANY_ignore = ' \t'

    def t_ANY_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    ###########################
    # PDP-8 Mode Instructions #
    ###########################

    # Reference page C-7 of "LAP6-DIAL Programmer's Reference Manual"

    # Memory Reference Instructions
    t_pmode_P_AND = r'\bAND\b'
    t_pmode_P_TAD = r'\bTAD\b'
    t_pmode_P_ISZ = r'\bISZ\b'
    t_pmode_P_DCA = r'\bDCA\b'
    t_pmode_P_JMS = r'\bJMS\b'
    t_pmode_P_JMP = r'\bJMP\b'

    # Group 1 Operate Microinstructions
    t_pmode_P_NOP = r'\bNOP\b'
    t_pmode_P_IAC = r'\bTAC\b'
    t_pmode_P_RAL = r'\bRAL\b'
    t_pmode_P_RTL = r'\bRTL\b'
    t_pmode_P_RAR = r'\bRAR\b'
    t_pmode_P_RTR = r'\bRTR\b'
    t_pmode_P_CML = r'\bCML\b'
    t_pmode_P_CMA = r'\bCMA\b'
    t_pmode_P_CLL = r'\bCLL\b'
    t_pmode_P_CLA = r'\bCLA\b'

    # Group 2 Operate Microinstructions
    t_pmode_P_HLT = r'\bHLT\b'
    t_pmode_P_OSR = r'\bOSR\b'
    t_pmode_P_SKP = r'\bSKP\b'
    t_pmode_P_SNL = r'\bSNL\b'
    t_pmode_P_SZL = r'\bSZL\b'
    t_pmode_P_SZA = r'\bSZA\b'
    t_pmode_P_SNA = r'\bSNA\b'
    t_pmode_P_SMA = r'\bSMA\b'
    t_pmode_P_SPA = r'\bSPA\b'

    # Combined Operate Microinstructions
    t_pmode_P_CIA = r'\bCIA\b'
    t_pmode_P_STL = r'\bSTL\b'
    t_pmode_P_GLK = r'\bGLK\b'
    t_pmode_P_STA = r'\bSTA\b'
    t_pmode_P_LAS = r'\bLAS\b'

    # IOT Microinstructions
    t_pmode_P_ION = r'\bION\b'
    t_pmode_P_IOF = r'\bIOF\b'
    t_pmode_P_KSF = r'\bKSF\b'
    t_pmode_P_KCC = r'\bKCC\b'
    t_pmode_P_KRS = r'\bKRS\b'
    t_pmode_P_KRB = r'\bKRB\b'
    t_pmode_P_TSF = r'\bTSF\b'
    t_pmode_P_TCF = r'\bTCF\b'
    t_pmode_P_TPC = r'\bTPC\b'
    t_pmode_P_TLS = r'\bTLS\b'
    t_pmode_P_CLSK = r'\bCLSK\b'
    t_pmode_P_CLLR = r'\bCLLR\b'
    t_pmode_P_CLAB = r'\bCLAB\b'
    t_pmode_P_CLEN = r'\bCLEN\b'
    t_pmode_P_CLSA = r'\bCLSA\b'
    t_pmode_P_CLBA = r'\bCLBA\b'
    t_pmode_P_CLCA = r'\bCLCA\b'
    t_pmode_P_CDF = r'\bCDF\b'
    t_pmode_P_CIF = r'\bCIF\b'
    t_pmode_P_RDF = r'\bRDF\b'
    t_pmode_P_RIF = r'\bRIF\b'
    t_pmode_P_RMF = r'\bRMF\b'
    t_pmode_P_RIB = r'\bRIB\b'
    t_pmode_P_LINC = r'\bLINC\b'

    ##########################
    # LINC Mode Instructions #
    ##########################

    # Reference page C-9 of "LAP6-DIAL Programmer's Reference Manual"
    # Add
    t_lmode_L_ADD = r'\bADD\b'
    t_lmode_L_ADA = r'\bADA\b'
    t_lmode_L_ADM = r'\bADM\b'
    t_lmode_L_LAM = r'\bLAM\b'

    # Multiply
    t_lmode_L_MUL = r'\bMUL\b'

    # Load
    t_lmode_L_LDA = r'\bLDA\b'
    t_lmode_L_LDH = r'\bLDH\b'

    # Store
    t_lmode_L_STC = r'\bSTC\b'
    t_lmode_L_STA = r'\bSTA\b'
    t_lmode_L_STH = r'\bSTH\b'

    # Shift/Rotate
    t_lmode_L_ROL = r'\bROL\b'
    t_lmode_L_ROR = r'\bROR\b'
    t_lmode_L_SCR = r'\bSCR\b'

    # Operate
    t_lmode_L_HLT = r'\bHLT\b'
    t_lmode_L_NOP = r'\bNOP\b'
    t_lmode_L_CLR = r'\bCLR\b'
    t_lmode_L_SET = r'\bSET\b'
    t_lmode_L_JMP = r'\bJMP\b'
    t_lmode_L_QAC = r'\bQAC\b'

    # Logical Operations
    t_lmode_L_BCL = r'\bBCL\b'
    t_lmode_L_BSE = r'\bBSE\b'
    t_lmode_L_BCO = r'\bBCO\b'
    t_lmode_L_COM = r'\bCOM\b'

    # Skip
    t_lmode_L_SAE = r'\bSAE\b'
    t_lmode_L_SHD = r'\bSHD\b'
    t_lmode_L_SNS = r'\bSNS\b'
    t_lmode_L_SKP = r'\bSKP\b'
    t_lmode_L_AZE = r'\bAZE\b'
    t_lmode_L_APO = r'\bAPO\b'
    t_lmode_L_LZE = r'\bLZE\b'
    t_lmode_L_FLO = r'\bFLO\b'
    t_lmode_L_QLZ = r'\bQLZ\b'
    t_lmode_L_SXL = r'\bSXL\b'
    t_lmode_L_KST = r'\bKST\b'
    t_lmode_L_SRO = r'\bSRO\b'
    t_lmode_L_XSK = r'\bXSK\b'
    t_lmode_L_STD = r'\bSTD\b'

    # Input/Output
    t_lmode_L_ATR = r'\bATR\b'
    t_lmode_L_RTA = r'\bRTA\b'
    t_lmode_L_SAM = r'\bSAM\b'
    t_lmode_L_DIS = r'\bDIS\b'
    t_lmode_L_DSC = r'\bDSC\b'
    t_lmode_L_PDP = r'\bPDP\b'
    t_lmode_L_RSW = r'\bRSW\b'
    t_lmode_L_LSW = r'\bLSW\b'
    t_lmode_L_IOB = r'\bIOB\b'

    # Memory
    t_lmode_L_LIF = r'\bLIF\b'
    t_lmode_L_LDF = r'\bLDF\b'

    # LINC Tape
    t_lmode_L_RDE = r'\bRDE\b'
    t_lmode_L_RDC = r'\bRDC\b'
    t_lmode_L_RCG = r'\bRCG\b'
    t_lmode_L_WRI = r'\bWRI\b'
    t_lmode_L_WRC = r'\bWRC\b'
    t_lmode_L_WCG = r'\bWCG\b'
    t_lmode_L_CHK = r'\bCHK\b'
    t_lmode_L_MTB = r'\bMTB\b'
    t_lmode_L_XOA = r'\bXOA\b'

    # Extended Operations
    t_lmode_L_ESF = r'\bESF\b'
    t_lmode_L_TAC = r'\bTAC\b'
    t_lmode_L_TMA = r'\bTMA\b'
    t_lmode_L_AXO = r'\bAXO\b'
    t_lmode_L_DJR = r'\bDJR\b'
    t_lmode_L_MSC = r'\bMSC\b'
    t_lmode_L_SFA = r'\bSFA\b'

    instance = lex.lex()
    instance.begin('pmode')
    return instance


if __name__ == '__main__':
    lexer = lap6_lex()
    with open('../test/FRQANA') as listing:
        lexer.input(listing.read())

    for token in lexer:
        print(token)
