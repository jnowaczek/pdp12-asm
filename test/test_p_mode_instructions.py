import unittest

import pdp12_asm.asm_parse as asm_parse
import pdp12_asm.model as model
import pdp12_asm.pdp12_perm_sym as pdp12_perm_sym


class BasicClassTests(unittest.TestCase):
    def test_alone(self):
        for instruction in filter(lambda i: pdp12_perm_sym.pmode_instructions[i]["class"] == "P_BASIC",
                                  pdp12_perm_sym.pmode_instructions):
            test_string = "PMODE\n" + instruction + "\n"
            expected_opcode = pdp12_perm_sym.pmode_instructions[instruction]["opcode"]
            expected = model.Program()
            expected.append(model.ProgramEntry(0o4020, expected_opcode))
            asm_parse.reset_parser()
            self.assertEqual(expected, asm_parse.parse(test_string))

    def test_with_label(self):
        for instruction in filter(lambda i: pdp12_perm_sym.pmode_instructions[i]["class"] == "P_BASIC",
                                  pdp12_perm_sym.pmode_instructions):
            test_string = "PMODE\n" + "TEST, " + instruction + "\n"
            expected_opcode = pdp12_perm_sym.pmode_instructions[instruction]["opcode"]
            expected = model.Program()
            expected.append(model.ProgramEntry(0o4020, expected_opcode))
            asm_parse.reset_parser()
            self.assertEqual(expected, asm_parse.parse(test_string))


class MemoryReferenceTests(unittest.TestCase):
    def test_alone(self):
        for instruction in filter(lambda i: pdp12_perm_sym.pmode_instructions[i]["class"] == "P_MEMORY_REFERENCE",
                                  pdp12_perm_sym.pmode_instructions):
            test_string = "PMODE\n" + instruction + "\n"
            expected_opcode = pdp12_perm_sym.pmode_instructions[instruction]["opcode"]
            expected = model.Program()
            expected.append(model.ProgramEntry(0o4020, expected_opcode))
            asm_parse.reset_parser()
            self.assertEqual(expected, asm_parse.parse(test_string))

    def test_argument(self):
        for instruction in filter(lambda i: pdp12_perm_sym.pmode_instructions[i]["class"] == "P_MEMORY_REFERENCE",
                                  pdp12_perm_sym.pmode_instructions):
            test_string = "PMODE\n" + instruction + " 300" + "\n"
            expected_opcode = pdp12_perm_sym.pmode_instructions[instruction]["opcode"] + 0o300
            expected = model.Program()
            expected.append(model.ProgramEntry(0o4020, expected_opcode))
            asm_parse.reset_parser()
            self.assertEqual(expected, asm_parse.parse(test_string))

    def test_argument_indirect(self):
        for instruction in filter(lambda i: pdp12_perm_sym.pmode_instructions[i]["class"] == "P_MEMORY_REFERENCE",
                                  pdp12_perm_sym.pmode_instructions):
            test_string = "PMODE\n" + instruction + " I 300" + "\n"
            expected_opcode = 0o400 + pdp12_perm_sym.pmode_instructions[instruction]["opcode"] + 0o300
            expected = model.Program()
            expected.append(model.ProgramEntry(0o4020, expected_opcode))
            asm_parse.reset_parser()
            self.assertEqual(expected, asm_parse.parse(test_string))
