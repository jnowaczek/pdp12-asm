pseudo_ops = [
    'asmifz',
    'asmifn',
    'asmifm',
    'asmskp',
    'decimal',
    'eject',
    'field',
    'indirect',
    'list',
    'listape',
    'lmode',
    'lodsym',
    'nolist',
    'octal',
    'page',
    'pmode',
    'savsym',
    'segmnt',
    'text',
    'zero_page',
]

pmode_instructions = {
    ###########################
    # PDP-8 Mode Instructions #
    ###########################

    # Reference page C-7 of "LAP6-DIAL Programmer's Reference Manual"
    # Memory Reference Instructions
    'and': 0o0000,
    'tad': 0o1000,
    'isz': 0o2000,
    'dca': 0o3000,
    'jms': 0o4000,
    'jmp': 0o5000,

    # Group 1 Operate Microinstructions
    'nop': 0o7000,
    'iac': 0o7001,
    'ral': 0o7004,
    'rtl': 0o7006,
    'rar': 0o7010,
    'rtr': 0o7012,
    'cml': 0o7020,
    'cma': 0o7040,
    'cll': 0o7100,
    'cla': 0o7200,

    # Group 2 Operate Microinstructions
    'hlt': 0o7402,
    'osr': 0o7404,
    'skp': 0o7410,
    'snl': 0o7420,
    'szl': 0o7430,
    'sza': 0o7440,
    'sna': 0o7450,
    'sma': 0o7500,
    'spa': 0o7510,

    # Combined Operate Microinstructions
    'cia': 0o7041,
    'stl': 0o7120,
    'glk': 0o7204,
    'sta': 0o7240,
    'las': 0o7604,

    # IOT Microinstructions
    'ion': 0o6001,
    'iof': 0o6002,
    'ksf': 0o6031,
    'kcc': 0o6032,
    'krs': 0o6034,
    'krb': 0o6036,
    'tsf': 0o6041,
    'tcf': 0o6042,
    'tpc': 0o6044,
    'tls': 0o6046,
    'clsk': 0o6131,
    'cllr': 0o6132,
    'clab': 0o6133,
    'clen': 0o6134,
    'clsa': 0o6135,
    'clba': 0o6136,
    'clca': 0o6137,
    'cdf': 0o6201,
    'cif': 0o6202,
    'rdf': 0o6204,
    'rif': 0o6224,
    'rmf': 0o6244,
    'rib': 0o6234,
    'linc': 0o6141,
}

lmode_instructions = {
    ##########################
    # LINC Mode Instructions #
    ##########################

    # Reference page C-9 of DEC-12-SE2D-D "LAP6-DIAL Programmer's Reference Manual"
    # Reference page A-1 of DEC-12-SRZC-D "PDP-12 System Reference Manual"
    # Add
    'add': {'opcode': 0o2000, 'class': 'L_DIRECT'},
    'ada': {'opcode': 0o1100, 'class': 'L_BETA'},
    'adm': {'opcode': 0o1140, 'class': 'L_BETA'},
    'lam': {'opcode': 0o1200, 'class': 'L_BETA'},

    # Multiply
    'mul': {'opcode': 0o1240, 'class': 'L_BETA'},

    # Load
    'lda': {'opcode': 0o1000, 'class': 'L_BETA'},
    'ldh': {'opcode': 0o1300, 'class': 'L_BETA'},

    # Store
    'stc': {'opcode': 0o4000, 'class': 'L_DIRECT'},
    'sta': {'opcode': 0o1040, 'class': 'L_BETA'},
    'sth': {'opcode': 0o1340, 'class': 'L_BETA'},

    # Shift/Rotate
    'rol': {'opcode': 0o0240, 'class': 'L_ALPHA_I_0o17'},
    'ror': {'opcode': 0o0300, 'class': 'I_ALPHA_I_0o17'},
    'scr': {'opcode': 0o0340, 'class': 'I_ALPHA_I_0o17'},

    # Operate
    'hlt': {'opcode': 0o0000, 'class': 'L_BASIC'},
    'nop': {'opcode': 0o0016, 'class': 'L_BASIC'},
    'clr': {'opcode': 0o0011, 'class': 'L_BASIC'},
    'set': {'opcode': 0o0040, 'class': 'L_ALPHA'},
    'jmp': {'opcode': 0o6000, 'class': 'L_DIRECT'},
    'djr': {'opcode': 0o0006, 'class': 'L_BASIC'},
    'esf': {'opcode': 0o0004, 'class': 'L_BASIC'},
    'sfa': {'opcode': 0o0024, 'class': 'L_BASIC'},
    'qac': {'opcode': 0o0005, 'class': 'L_BASIC'},

    # Logical Operations
    'bcl': {'opcode': 0o1540, 'class': 'L_BETA'},
    'bse': {'opcode': 0o1600, 'class': 'L_BETA'},
    'bco': {'opcode': 0o1640, 'class': 'L_BETA'},
    'com': {'opcode': 0o0017, 'class': 'L_BASIC'},

    # Skip
    'sae': {'opcode': 0o1440, 'class': 'L_BETA'},
    'shd': {'opcode': 0o1400, 'class': 'L_BETA'},
    'sns': {'opcode': 0o0440, 'class': 'L_ALPHA_I_0o5'},
    'skp': {'opcode': 0o0456, 'class': 'L_ALPHA_I'},
    'aze': {'opcode': 0o0450, 'class': 'L_ALPHA_I'},
    'apo': {'opcode': 0o0451, 'class': 'L_ALPHA_I'},
    'lze': {'opcode': 0o0452, 'class': 'L_ALPHA_I'},
    'flo': {'opcode': 0o0454, 'class': 'L_ALPHA_I'},
    'qlz': {'opcode': 0o0455, 'class': 'L_ALPHA_I'},
    'sxl': {'opcode': 0o0400, 'class': 'L_ALPHA_I_0o17'},
    'kst': {'opcode': 0o0415, 'class': 'L_ALPHA_I'},
    'sro': {'opcode': 0o1500, 'class': 'L_BETA'},
    'xsk': {'opcode': 0o0200, 'class': 'L_ALPHA_I_0o17'},
    'std': {'opcode': 0o0416, 'class': 'L_ALPHA_I'},

    # Input/Output
    'atr': {'opcode': 0o0014, 'class': 'L_BASIC'},
    'rta': {'opcode': 0o0015, 'class': 'L_BASIC'},
    'sam': {'opcode': 0o0100, 'class': 'L_ALPHA_0o17'},
    'dis': {'opcode': 0o0140, 'class': 'L_ALPHA_I_0o17'},
    'dsc': {'opcode': 0o1740, 'class': 'L_BETA_DSC'},
    'rsw': {'opcode': 0o0516, 'class': 'L_BASIC'},
    'lsw': {'opcode': 0o0517, 'class': 'L_BASIC'},
    'iob': {'opcode': 0o0500, 'class': 'L_BASIC'},
    'pdp': {'opcode': 0o0002, 'class': 'L_BASIC'},

    # Memory
    'lif': {'opcode': 0o0600, 'class': 'L_ALPHA_0o37'},
    'ldf': {'opcode': 0o0640, 'class': 'L_ALPHA_0o37'},

    # IOB
    'rif': {'opcode': 0o6224, 'class': 'L_IOB'},
    'rdf': {'opcode': 0o6214, 'class': 'L_IOB'},
    'rib': {'opcode': 0o6234, 'class': 'L_IOB'},
    'rmf': {'opcode': 0o6244, 'class': 'L_IOB'},

    # LINC Tape
    'rde': {'opcode': 0o0702, 'class': 'L_TAPE'},
    'rdc': {'opcode': 0o0700, 'class': 'L_TAPE'},
    'rcg': {'opcode': 0o0701, 'class': 'L_TAPE'},
    'wri': {'opcode': 0o0706, 'class': 'L_TAPE'},
    'wrc': {'opcode': 0o0704, 'class': 'L_TAPE'},
    'wcg': {'opcode': 0o0705, 'class': 'L_TAPE'},
    'chk': {'opcode': 0o0707, 'class': 'L_TAPE'},
    'mtb': {'opcode': 0o0703, 'class': 'L_TAPE'},
    'axo': {'opcode': 0o0001, 'class': 'L_BASIC'},
    'xoa': {'opcode': 0o0021, 'class': 'L_BASIC'},
    'tac': {'opcode': 0o0003, 'class': 'L_BASIC'},
    'tma': {'opcode': 0o0023, 'class': 'L_BASIC'},
    'msc': {'opcode': 0o0000, 'class': 'L_BASIC'},
}
