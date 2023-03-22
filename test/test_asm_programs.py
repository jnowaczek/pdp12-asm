import os
import unittest

from pdp12_asm import asm_parse
from pdp12_asm import model
from dec_papertape_format import RIMEncoder


def simple_read_and_assemble(listing_path, output_path):
    with open(listing_path) as listing:
        with open(output_path) as output:
            expected = model.Program()
            for line in output:
                location = int(line.strip().split(' ')[0], 8)
                instruction = int(line.strip().split(' ')[1], 8)
                expected.append(model.ProgramEntry(location, instruction))

            asm_parse.reset_parser()
            result = asm_parse.parse(listing.read())

    return result, expected


def rim_read_and_assemble(listing_path, output_path):
    with open(listing_path) as listing:
        with open(output_path, "rb") as output:
            expected = output.read()

            asm_parse.reset_parser()
            program = asm_parse.parse(listing.read())
            result = RIMEncoder.encode_and_pad(program)

    return result, expected


class OutputTests(unittest.TestCase):
    def test_simple_output(self):
        listings = os.listdir("resources/listings")
        for listing in listings:
            with self.subTest(Listing=listing):
                # noinspection PyBroadException
                try:
                    infile = os.path.join("resources/listings/", listing)
                    outfile = os.path.join("resources/simple_output/", listing + ".output")

                    result, expected = simple_read_and_assemble(infile, outfile)
                    self.assertEqual(expected, result)
                except AssertionError:
                    raise
                except FileNotFoundError as e:
                    self.skipTest(f"Listing does not exist")
                except:
                    self.fail()

    def test_rim_output(self):
        listings = os.listdir("resources/listings")
        for listing in listings:
            with self.subTest(Listing=listing):
                # noinspection PyBroadException
                try:
                    infile = os.path.join("resources/listings/", listing)
                    outfile = os.path.join("resources/rim_output/", listing + ".rim")

                    result, expected = rim_read_and_assemble(infile, outfile)
                    self.assertEqual(expected, result)
                except AssertionError:
                    raise
                except FileNotFoundError as e:
                    self.skipTest(f"Listing does not exist")
                except:
                    self.fail()
