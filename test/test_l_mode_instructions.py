import unittest

import asm_parse


# class BasicClassTests(unittest.TestCase):
#     def test_alone(self):
#         for instruction in filter(lambda i: pdp12_perm_sym.pmode_instructions[i]['class'] == 'L_BASIC',
#                                   pdp12_perm_sym.pmode_instructions):
#             test_string = 'PMODE\n' + instruction
#             expected = pdp12_perm_sym.pmode_instructions[instruction]['opcode']
#             self.assertEqual([expected], asm_parse.parse(test_string))
#
#     def test_with_label(self):
#         for instruction in filter(lambda i: pdp12_perm_sym.pmode_instructions[i]['class'] == 'P_BASIC',
#                                   pdp12_perm_sym.pmode_instructions):
#             test_string = 'PMODE\n' + 'TEST, ' + instruction
#             expected = pdp12_perm_sym.pmode_instructions[instruction]['opcode']
#             self.assertEqual([expected], asm_parse.parse(test_string))


class FileTests(unittest.TestCase):
    def test_kalleidoscope(self):
        with open('./KALEIDOSCOPE') as listing:
            result = asm_parse.parse(listing.read())

        expected = []
        with open('./KALEIDOSCOPE.output') as assembly:
            for line in assembly:
                expected.append('{:0>4o}'.format(int(line.strip().split(' ')[1], 8)))
        self.assertEqual(expected, result)

    def test_moon(self):
        with open('./MOON') as listing:
            result = asm_parse.parse(listing.read())

        expected = []
        with open('./MOON.output') as assembly:
            for line in assembly:
                expected.append('{:0>4o}'.format(int(line.strip().split(' ')[1], 8)))
        self.assertEqual(expected, result)

    def test_music(self):
        with open('./MUSIC') as listing:
            result = asm_parse.parse(listing.read())

        expected = []
        with open('./MUSIC.output') as assembly:
            for line in assembly:
                expected.append('{:0>4o}'.format(int(line.strip().split(' ')[1], 8)))
        self.assertEqual(expected, result)
