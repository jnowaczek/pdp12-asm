import unittest

import lap6_parse
import pdp12_perm_sym


class BasicClassTests(unittest.TestCase):
    def test_alone(self):
        for instruction in filter(lambda i: pdp12_perm_sym.pmode_instructions[i]['class'] == 'P_BASIC',
                                  pdp12_perm_sym.pmode_instructions):
            test_string = 'PMODE\n' + instruction
            expected = pdp12_perm_sym.pmode_instructions[instruction]['opcode']
            self.assertEqual([expected], lap6_parse.parse(test_string))

    def test_with_label(self):
        for instruction in filter(lambda i: pdp12_perm_sym.pmode_instructions[i]['class'] == 'P_BASIC',
                                  pdp12_perm_sym.pmode_instructions):
            test_string = 'PMODE\n' + 'TEST, ' + instruction
            expected = pdp12_perm_sym.pmode_instructions[instruction]['opcode']
            self.assertEqual([expected], lap6_parse.parse(test_string))


class MemoryReferenceTests(unittest.TestCase):
    def test_alone(self):
        for instruction in filter(lambda i: pdp12_perm_sym.pmode_instructions[i]['class'] == 'P_MEMORY_REFERENCE',
                                  pdp12_perm_sym.pmode_instructions):
            test_string = 'PMODE\n' + instruction
            expected = pdp12_perm_sym.pmode_instructions[instruction]['opcode']
            self.assertEqual([expected], lap6_parse.parse(test_string))

    def test_argument(self):
        for instruction in filter(lambda i: pdp12_perm_sym.pmode_instructions[i]['class'] == 'P_MEMORY_REFERENCE',
                                  pdp12_perm_sym.pmode_instructions):
            test_string = 'PMODE\n' + instruction + ' 300'
            expected = pdp12_perm_sym.pmode_instructions[instruction]['opcode'] + 0o300
            self.assertEqual([expected], lap6_parse.parse(test_string))

    def test_argument_indirect(self):
        for instruction in filter(lambda i: pdp12_perm_sym.pmode_instructions[i]['class'] == 'P_MEMORY_REFERENCE',
                                  pdp12_perm_sym.pmode_instructions):
            test_string = 'PMODE\n' + instruction + ' I 300'
            expected = 0o400 + pdp12_perm_sym.pmode_instructions[instruction]['opcode'] + 0o300
            self.assertEqual([expected], lap6_parse.parse(test_string))
