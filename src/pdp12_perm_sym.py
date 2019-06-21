pseudo_ops = [
    'asmifz',
    'asmifn',
    'asmifm',
    'asmskp',
    'decimal',
    'eject',
    'field',
    'i',
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
    'z',
]

pmode_instructions = {
    ###########################
    # PDP-8 Mode Instructions #
    ###########################

    # Reference page C-7 of "LAP6-DIAL Programmer's Reference Manual"
    # Memory Reference Instructions
    'and': {'opcode': 0o0000, 'class': 'P_MEMORY_REFERENCE'},
    'tad': {'opcode': 0o1000, 'class': 'P_MEMORY_REFERENCE'},
    'isz': {'opcode': 0o2000, 'class': 'P_MEMORY_REFERENCE'},
    'dca': {'opcode': 0o3000, 'class': 'P_MEMORY_REFERENCE'},
    'jms': {'opcode': 0o4000, 'class': 'P_MEMORY_REFERENCE'},
    'jmp': {'opcode': 0o5000, 'class': 'P_MEMORY_REFERENCE'},

    # Group 1 Operate Microinstructions
    # Added to 0o7000
    'nop': {'opcode': 0o0000, 'class': 'P_OPERATE_1'},
    'iac': {'opcode': 0o0001, 'class': 'P_OPERATE_1'},
    'ral': {'opcode': 0o0004, 'class': 'P_OPERATE_1'},
    'rtl': {'opcode': 0o0006, 'class': 'P_OPERATE_1'},
    'rar': {'opcode': 0o0010, 'class': 'P_OPERATE_1'},
    'rtr': {'opcode': 0o0012, 'class': 'P_OPERATE_1'},
    'cml': {'opcode': 0o0020, 'class': 'P_OPERATE_1'},
    'cma': {'opcode': 0o0040, 'class': 'P_OPERATE_1'},
    'cll': {'opcode': 0o0100, 'class': 'P_OPERATE_1'},

    # Group 2 Operate Microinstructions
    # Added to 0o7400
    'hlt': {'opcode': 0o0002, 'class': 'P_OPERATE_2'},
    'osr': {'opcode': 0o0004, 'class': 'P_OPERATE_2'},
    'skp': {'opcode': 0o0010, 'class': 'P_OPERATE_2'},
    'snl': {'opcode': 0o0020, 'class': 'P_OPERATE_2'},
    'szl': {'opcode': 0o0030, 'class': 'P_OPERATE_2'},
    'sza': {'opcode': 0o0040, 'class': 'P_OPERATE_2'},
    'sna': {'opcode': 0o0050, 'class': 'P_OPERATE_2'},
    'sma': {'opcode': 0o0100, 'class': 'P_OPERATE_2'},
    'spa': {'opcode': 0o0110, 'class': 'P_OPERATE_2'},

    # Extended Arithmetic Element KE12 Microinstructions
    # Added to 0o7401
    'sca': {'opcode': 0o0040, 'class': 'P_EXTENDED_ARITHMETIC'},
    'scl': {'opcode': 0o0002, 'class': 'P_EXTENDED_ARITHMETIC_LONG'},
    'cam': {'opcode': 0o0220, 'class': 'P_EXTENDED_ARITHMETIC'},
    'mqa': {'opcode': 0o0100, 'class': 'P_EXTENDED_ARITHMETIC'},
    'mql': {'opcode': 0o0020, 'class': 'P_EXTENDED_ARITHMETIC'},
    'muy': {'opcode': 0o0004, 'class': 'P_EXTENDED_ARITHMETIC_LONG'},
    'dvi': {'opcode': 0o0006, 'class': 'P_EXTENDED_ARITHMETIC_LONG'},
    'shl': {'opcode': 0o0012, 'class': 'P_EXTENDED_ARITHMETIC_LONG'},
    'asr': {'opcode': 0o0014, 'class': 'P_EXTENDED_ARITHMETIC_LONG'},
    'lsr': {'opcode': 0o0016, 'class': 'P_EXTENDED_ARITHMETIC_LONG'},
    'nmi': {'opcode': 0o7411, 'class': 'P_BASIC'},  # Not microprogrammable

    # CLA Operate Microinstruction
    # Valid in Group 1, Group 2, or EAE
    'cla': {'opcode': 0o0200, 'class': 'P_CLA'},

    # Combined Operate Microinstructions
    'cia': {'opcode': 0o7041, 'class': 'P_BASIC'},
    'stl': {'opcode': 0o7120, 'class': 'P_BASIC'},
    'glk': {'opcode': 0o7204, 'class': 'P_BASIC'},
    'sta': {'opcode': 0o7240, 'class': 'P_BASIC'},
    'las': {'opcode': 0o7604, 'class': 'P_BASIC'},

    # IOT Microinstructions
    'ion': {'opcode': 0o6001, 'class': 'P_BASIC'},
    'iof': {'opcode': 0o6002, 'class': 'P_BASIC'},
    'linc': {'opcode': 0o6141, 'class': 'P_BASIC'},

    # Extended Memory
    'cdf': {'opcode': 0o6201, 'class': 'P_EXTENDED_MEMORY_0o7'},
    'cif': {'opcode': 0o6202, 'class': 'P_EXTENDED_MEMORY_0o7'},
    'rdf': {'opcode': 0o6204, 'class': 'P_BASIC'},
    'rif': {'opcode': 0o6224, 'class': 'P_BASIC'},
    'rmf': {'opcode': 0o6244, 'class': 'P_BASIC'},
    'rib': {'opcode': 0o6234, 'class': 'P_BASIC'},

    # Peripheral IOT Instructions
    # 'ksf': {'opcode': 0o6031, 'class': ''},
    # 'kcc': {'opcode': 0o6032, 'class': ''},
    # 'krs': {'opcode': 0o6034, 'class': ''},
    # 'krb': {'opcode': 0o6036, 'class': ''},
    # 'tsf': {'opcode': 0o6041, 'class': ''},
    # 'tcf': {'opcode': 0o6042, 'class': ''},
    # 'tpc': {'opcode': 0o6044, 'class': ''},
    # 'tls': {'opcode': 0o6046, 'class': ''},
    # 'clsk': {'opcode': 0o6131, 'class': ''},
    # 'cllr': {'opcode': 0o6132, 'class': ''},
    # 'clab': {'opcode': 0o6133, 'class': ''},
    # 'clen': {'opcode': 0o6134, 'class': ''},
    # 'clsa': {'opcode': 0o6135, 'class': ''},
    # 'clba': {'opcode': 0o6136, 'class': ''},
    # 'clca': {'opcode': 0o6137, 'class': ''},
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
    'ror': {'opcode': 0o0300, 'class': 'L_ALPHA_I_0o17'},
    'scr': {'opcode': 0o0340, 'class': 'L_ALPHA_I_0o17'},

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
