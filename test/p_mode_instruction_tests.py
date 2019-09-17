import unittest

import lap6_parse
import pdp12_perm_sym


class BasicClassTests(unittest.TestCase):
    def test_alone(self):
        for instruction in filter(lambda i: pdp12_perm_sym.pmode_instructions[i]['class'] == 'P_BASIC',
                                  pdp12_perm_sym.pmode_instructions):
            test_string = 'PMODE\n' + instruction
            expected = pdp12_perm_sym.pmode_instructions[instruction]['opcode']
            print(expected)
            self.assertEqual(lap6_parse.parse(test_string), expected)

    def test_with_label(self):
        for instruction in filter(lambda i: pdp12_perm_sym.pmode_instructions[i]['class'] == 'P_BASIC',
                                  pdp12_perm_sym.pmode_instructions):
            test_string = 'PMODE\n' + 'TEST, ' + instruction
            expected = pdp12_perm_sym.pmode_instructions[instruction]['opcode']
            self.assertEqual(lap6_parse.parse(test_string), expected)
