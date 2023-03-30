import ply.yacc as yacc

from pdp12_asm import model
from pdp12_asm import pdp12_perm_sym
from pdp12_asm.asm_lexer import lap6_lex

# Initial settings ref. Chapter 3 of "PDP-12 LAP6-DIAL Programmer"s Reference Manual"
# Start in LINC mode with octal radix at address 0o4020
mode = "lmode"
radix = 8
mem_origin = 0o4020

current_location = 0
user_symbols = {}
need_second_pass = False

precedence = (
)


def symbol_lookup(name):
    global mode
    lower_name = name.lower()
    if name == ".":
        return current_location
    if mode == "lmode":
        if lower_name in pdp12_perm_sym.lmode_instructions:
            return pdp12_perm_sym.lmode_instructions[lower_name]
    if mode == "pmode":
        if lower_name in pdp12_perm_sym.pmode_instructions:
            return pdp12_perm_sym.pmode_instructions[lower_name]
    if name in user_symbols:
        return user_symbols[name]
    else:
        global need_second_pass
        need_second_pass = True
        return 0o0000


def p_program(p):
    """program : empty
               | program empty
               | program machine_code"""
    if len(p) == 3:
        if p[2] is not None:
            global current_location
            p[1].append(model.ProgramEntry(current_location, p[2]))
            current_location += 1
        p[0] = p[1]
    if len(p) == 2:
        p[0] = model.Program()


def p_pseudo_op(p):
    """empty : pseudo_no_args STATEMENT_END
             | pseudo_with_args STATEMENT_END"""


def p_pseudo_with_args(p):
    """pseudo_with_args : SEGMNT expression"""
    global current_location
    if p[1] == "SEGMNT":
        if 0 > p[2] < 7:
            current_location = 0o2000 * p[2]
        else:
            raise SyntaxError


def p_pseudo_no_args(p):
    """pseudo_no_args : OCTAL
                      | DECIMAL
                      | PMODE
                      | LMODE"""
    global radix, mode, current_location
    if p[1] == "OCTAL":
        radix = 8
    elif p[1] == "DECIMAL":
        radix = 10
    elif p[1] == "LMODE":
        mode = "lmode"
    elif p[1] == "PMODE":
        mode = "pmode"
    elif p[1] == "SEGMNT":
        current_location = (current_location + 0o1777) & 0o6000
    p[0] = None


def p_machine_code(p):
    """machine_code : INSTRUCTION STATEMENT_END
                    | INSTRUCTION I STATEMENT_END
                    | INSTRUCTION expression STATEMENT_END
                    | INSTRUCTION I expression STATEMENT_END"""
    if mode == "pmode":
        if len(p) == 3:
            p[0] = symbol_lookup(p[1])["opcode"]
        elif len(p) == 4:
            if p[1] == "i" or p[2] == "I":
                s = symbol_lookup(p[2])
                p[0] = s["opcode"] | 0o400
            else:
                s = symbol_lookup(p[1])
                p[0] = s["opcode"] + (p[2] & s["mask"])
        elif len(p) == 5:
            s = symbol_lookup(p[1])
            p[0] = s["opcode"] + (p[3] & s["mask"]) | 0o400
    elif mode == "lmode":
        if len(p) == 3:
            p[0] = symbol_lookup(p[1])["opcode"]
        elif len(p) == 4:
            if p[2] == "i" or p[2] == "I":
                p[0] = symbol_lookup(p[1])["opcode"] + 0o20
            else:
                p[0] = symbol_lookup(p[1])["opcode"] + p[2]
        elif len(p) == 5:
            p[0] = symbol_lookup(p[1])["opcode"] + 0o20 + p[3]


def p_pmode_operate_groups(p):
    """machine_code : grouped_operate_1 STATEMENT_END
                    | grouped_operate_2 STATEMENT_END"""
    p[0] = p[1]


def p_grouped_operate_1(p):
    """grouped_operate_1 : P_OPERATE_1
                         | grouped_operate_1 P_OPERATE_1"""
    if len(p) == 2:
        p[0] = 0o7000 | symbol_lookup(p[1])["opcode"]
    else:
        p[0] = p[1] | symbol_lookup(p[2])["opcode"]


def p_grouped_operate_2(p):
    """grouped_operate_2 : P_OPERATE_2
                         | grouped_operate_2 P_OPERATE_2"""
    if len(p) == 2:
        p[0] = 0o7400 | symbol_lookup(p[1])["opcode"]
    else:
        p[0] = p[1] | symbol_lookup(p[2])["opcode"]


def p_expression_literal(p):
    """machine_code : expression STATEMENT_END"""
    p[0] = p[1]


def p_set_origin(p):
    """empty : ASTERISK NUMBER STATEMENT_END"""
    global current_location
    current_location = int(p[2], base=radix)


def p_assignment(p):
    """empty : SYMBOL COMMA
             | SYMBOL EQUALS expression"""
    global current_location
    if p[1] not in user_symbols:
        if p[2] == ",":
            user_symbols.update({p[1]: current_location})
        elif p[2] == "=":
            user_symbols.update({p[1]: p[3]})


def p_expression_plus(p):
    """expression : expression PLUS term"""
    if mode == "lmode":
        p[0] = (p[1] + p[3]) & 0o1777
    if mode == "pmode":
        p[0] = (p[1] + p[3]) & 0o7777


def p_expression_minus(p):
    """expression : expression MINUS term
                  | MINUS expression"""
    # Refer to page 3-5 in "LAP6-DIAL Programmer"s Reference Manual"
    if mode == "lmode":  # One"s Complement
        if len(p) == 3:
            p[0] = 0 - p[2] & 0o1777 - 1
        else:
            p[0] = (p[1] - p[3]) & 0o1777 - 1
    if mode == "pmode":  # Two"s Complement
        if len(p) == 3:
            p[0] = 0 - p[2] & 0o7777
        else:
            p[0] = (p[1] - p[3]) & 0o7777


def p_expression_and(p):
    """expression : expression AMPERSAND term"""
    p[0] = p[1] & p[3]


def p_expression_or(p):
    """expression : expression EXCLAMATION term"""
    p[0] = p[1] | p[3]


def p_expression_term(p):
    """expression : term"""
    p[0] = p[1]


def p_term(p):
    """term : NUMBER
            | DOT"""
    if p[1] == ".":
        p[0] = current_location
    else:
        p[0] = int(p[1], radix)


def p_term_symbol(p):
    """term : SYMBOL"""
    p[0] = symbol_lookup(p[1])


def p_blank_lines(p):
    """empty : STATEMENT_END"""


def p_error(p):
    print("Illegal symbol "%s"" % p)


def parse(file, debug=False) -> model.Program:
    global need_second_pass, user_symbols
    l = lap6_lex()
    l.input(file)
    tokens = list(l.lextokens)
    p = yacc.yacc()
    program = p.parse(file, debug=debug)
    if need_second_pass:
        reset_parser()
        program = p.parse(file, debug=debug)
    return program


def reset_parser():
    global mode, radix, current_location, need_second_pass
    mode = "lmode"
    radix = 8
    current_location = 0o4020
    need_second_pass = False


if __name__ == "__main__":
    lexer = lap6_lex()
    with open("../../test/resources/listings/bootloader") as file:
        listing = file.read()
        lexer.input(listing)
        output = parse(listing)
        print(output)
        print(f"User Symbols: {user_symbols}")
