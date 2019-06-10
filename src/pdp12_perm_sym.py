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

pmode_symbols = {
    ###########################
    # PDP-8 Mode Instructions #
    ###########################

    # Reference page C-7 of "LAP6-DIAL Programmer's Reference Manual"
    # Memory Reference Instructions
    'p_and': 0o0000,
    'p_tad': 0o1000,
    'p_isz': 0o2000,
    'p_dca': 0o3000,
    'p_jms': 0o4000,
    'p_jmp': 0o5000,

    # Group 1 Operate Microinstructions
    'p_nop': 0o7000,
    'p_iac': 0o7001,
    'p_ral': 0o7004,
    'p_rtl': 0o7006,
    'p_rar': 0o7010,
    'p_rtr': 0o7012,
    'p_cml': 0o7020,
    'p_cma': 0o7040,
    'p_cll': 0o7100,
    'p_cla': 0o7200,

    # GrouP 2 Operate Microinstructions
    'p_hlt': 0o7402,
    'p_osr': 0o7404,
    'p_skp': 0o7410,
    'p_snl': 0o7420,
    'p_szl': 0o7430,
    'p_sza': 0o7440,
    'p_sna': 0o7450,
    'p_sma': 0o7500,
    'p_spa': 0o7510,

    # Combined Operate Microinstructions
    'p_cia': 0o7041,
    'p_stl': 0o7120,
    'p_glk': 0o7204,
    'p_sta': 0o7240,
    'p_las': 0o7604,

    # IOT Microinstructions
    'p_ion': 0o6001,
    'p_iof': 0o6002,
    'p_ksf': 0o6031,
    'p_kcc': 0o6032,
    'p_krs': 0o6034,
    'p_krb': 0o6036,
    'p_tsf': 0o6041,
    'p_tcf': 0o6042,
    'p_tpc': 0o6044,
    'p_tls': 0o6046,
    'p_clsk': 0o6131,
    'p_cllr': 0o6132,
    'p_clab': 0o6133,
    'p_clen': 0o6134,
    'p_clsa': 0o6135,
    'p_clba': 0o6136,
    'p_clca': 0o6137,
    'p_cdf': 0o6201,
    'p_cif': 0o6202,
    'p_rdf': 0o6204,
    'p_rif': 0o6224,
    'p_rmf': 0o6244,
    'p_rib': 0o6234,
    'p_linc': 0o6141,
}

lmode_symbols = {
    ##########################
    # LINC Mode Instructions #
    ##########################

    # Reference page C-9 of "LAP6-DIAL Programmer's Reference Manual"
    # Add
    'l_add': 0o2000,
    'l_ada': 0o1100,
    'l_adm': 0o1140,
    'l_lam': 0o1200,

    # Multiply
    'l_mul': 0o1240,

    # Load
    'l_lda': 0o1000,
    'l_ldh': 0o1300,

    # Store
    'l_stc': 0o4000,
    'l_sta': 0o1040,
    'l_sth': 0o1340,

    # Shift/Rotate
    'l_rol': 0o0240,
    'l_ror': 0o0300,
    'l_scr': 0o0340,

    # Operate
    'l_hlt': 0o0000,
    'l_nop': 0o0016,
    'l_clr': 0o0011,
    'l_set': 0o0040,
    'l_jmp': 0o6000,
    'l_qac': 0o0005,

    # Logical Operations
    'l_bcl': 0o1540,
    'l_bse': 0o1600,
    'l_bco': 0o1640,
    'l_com': 0o0017,

    # Skip
    'l_sae': 0o1440,
    'l_shd': 0o1400,
    'l_sns': 0o0440,
    'l_skp': 0o0456,
    'l_aze': 0o0450,
    'l_apo': 0o0451,
    'l_lze': 0o0452,
    'l_flo': 0o0454,
    'l_qlz': 0o0455,
    'l_sxl': 0o0400,
    'l_kst': 0o0415,
    'l_sro': 0o1500,
    'l_xsk': 0o0200,
    'l_std': 0o0416,

    # Input/Output
    'l_atr': 0o0014,
    'l_rta': 0o0015,
    'l_sam': 0o0100,
    'l_dis': 0o0140,
    'l_dsc': 0o1740,
    'l_pdp': 0o0002,
    'l_rsw': 0o0516,
    'l_lsw': 0o0517,
    'l_iob': 0o0500,

    # Memory
    'l_lif': 0o0600,
    'l_ldf': 0o0640,

    # LINC Tape
    'l_rde': 0o0702,
    'l_rdc': 0o0700,
    'l_rcg': 0o0701,
    'l_wri': 0o0706,
    'l_wrc': 0o0704,
    'l_wcg': 0o0705,
    'l_chk': 0o0707,
    'l_mtb': 0o0703,
    'l_xoa': 0o0021,

    # Extended Operations
    'l_esf': 0o0004,
    'l_tac': 0o0003,
    'l_tma': 0o0023,
    'l_axo': 0o0001,
    'l_djr': 0o0006,
    'l_msc': 0o0000,
    'l_sfa': 0o0024,
}
