import unittest

import asm_parse
import pdp12_perm_sym


class BasicClassTests(unittest.TestCase):
    def test_alone(self):
        for instruction in filter(lambda i: pdp12_perm_sym.lmode_instructions[i]['class'] == 'L_BASIC',
                                  pdp12_perm_sym.lmode_instructions):
            test_string = 'LMODE\n' + instruction + '\n'
            expected = pdp12_perm_sym.lmode_instructions[instruction]['opcode']
            asm_parse.reset_parser()
            self.assertEqual(['4020 {:0>4o}'.format(expected)], asm_parse.parse(test_string))

    def test_with_label(self):
        for instruction in filter(lambda i: pdp12_perm_sym.lmode_instructions[i]['class'] == 'L_BASIC',
                                  pdp12_perm_sym.lmode_instructions):
            test_string = 'LMODE\n' + 'TEST, ' + instruction + '\n'
            expected = pdp12_perm_sym.lmode_instructions[instruction]['opcode']
            asm_parse.reset_parser()
            self.assertEqual(['4020 {:0>4o}'.format(expected)], asm_parse.parse(test_string))
