import os
import unittest

from pdp12_asm import asm_parse


class SimpleOutputTests(unittest.TestCase):
    LISTINGS_PATH = 'test/resources/listings'
    SIMPLE_OUTPUT_PATH = 'test/resources/simple_output'

    def read_and_assemble(self, program_name):
        with open(os.path.join(self.LISTINGS_PATH, program_name)) as listing:
            with open(os.path.join(self.SIMPLE_OUTPUT_PATH, program_name + '.output')) as assembly:
                expected = []
                for line in assembly:
                    location = int(line.strip().split(' ')[0], 8)
                    instruction = int(line.strip().split(' ')[1], 8)
                    expected.append('{:0>4o} {:0>4o}'.format(location, instruction))

                result = asm_parse.parse(listing.read())

        return result, expected

    def test_kaleidoscope(self):
        result, expected = self.read_and_assemble('KALEIDOSCOPE')
        self.assertEqual(expected, result)

    def test_moon(self):
        result, expected = self.read_and_assemble('MOON')
        self.assertEqual(expected, result)

    def test_music(self):
        result, expected = self.read_and_assemble('MUSIC')
        self.assertEqual(expected, result)

    def test_rim_loader(self):
        result, expected = self.read_and_assemble('RIMLOADER')
        self.assertEqual(expected, result)

    def test_test(self):
        result, expected = self.read_and_assemble('TEST')
        self.assertEqual(expected, result)

    def test_echask(self):
        result, expected = self.read_and_assemble('ECHASK')
        self.assertEqual(expected, result)

    def test_loader(self):
        result, expected = self.read_and_assemble('LOADER')
        self.assertEqual(expected, result)

    def test_stpwch(self):
        result, expected = self.read_and_assemble('STPWCH')
        self.assertEqual(expected, result)

    # Something funky with this one, GETIT1 on line 25 is never defined
    # def test_frqana(self):
    #     result, expected = self.read_and_assemble('FRQANA')
    #     self.assertEqual(expected, result)

    def test_clcmth(self):
        result, expected = self.read_and_assemble('CLCMTH')
        self.assertEqual(expected, result)

    def test_text(self):
        result, expected = self.read_and_assemble('TEXT')
        self.assertEqual(expected, result)

    def test_patterns(self):
        result, expected = self.read_and_assemble('PATTERNS')
        self.assertEqual(expected, result)
