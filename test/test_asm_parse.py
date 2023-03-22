import unittest

from pdp12_asm import asm_parse
from pdp12_asm.asm_lexer import lap6_lex


class AsmParseTest(unittest.TestCase):
    def test_asm_parse(self):
        listings = os.listdir("resources/listings")
        for listing in listings:
            with self.subTest(Listing=listing):
                # noinspection PyBroadException
                try:
                    infile = os.path.join("resources/listings/", listing)
                    outfile = os.path.join("resources/simple_output/", listing + ".output")

                    lexer = lap6_lex()
                    with open('../../test/resources/listings/bootloader') as file:
                        listing = file.read()
                        lexer.input(listing)
                        output = asm_parse.parse(listing)
                        print(output)
                        print(f'User Symbols: {asm_parse.user_symbols}')
                    self.assertEqual(expected, result)
                except AssertionError:
                    raise
                except FileNotFoundError as e:
                    self.skipTest(f"Listing does not exist")
                except:
                    self.fail()
