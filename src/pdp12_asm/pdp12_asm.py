import argparse
from contextlib import nullcontext
import sys
import textwrap
import traceback
from typing import Optional

import pdp12_asm.model
from output_format import rim_formatter
from pdp12_asm import asm_parse


def main():
    parser = argparse.ArgumentParser(description="PDP-12 LAP6-DIAL Assembler",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-v", "--version", help="print the version number and exit", action="version",
                        version=f"%(prog)s not good enough")
    parser.add_argument("-f", metavar="FORMAT",
                        dest="format",
                        help=textwrap.dedent(
                            """\
                            select output file format
                              simple [default]
                              lst    program listing (not implemented)
                              rim    RIM tape format
                              bin    BIN tape format (not implemented)
                            """),
                        choices=["simple", "lst", "rim", "bin"],
                        default="simple")
    parser.add_argument("filename")
    parser.add_argument("-o", dest="outfile", help="write output to file, defaults to stdout")
    args = parser.parse_args()

    program: Optional[pdp12_asm.model.Program] = None

    try:
        with open(args.filename, "r") as listing:
            asm_parse.reset_parser()
            program = asm_parse.parse(listing.read())
    except Exception as e:
        traceback.print_exc()

    try:
        with open(args.outfile, "w") if args.outfile else nullcontext(sys.stdout) as f:
            if args.format == "simple":
                result = str(program)
            elif args.format == "lst":
                raise NotImplementedError("Program listing output is not currently supported, sorry ☹️")
            elif args.format == "rim":
                result = rim_formatter.encode_and_pad(program).decode("ascii")
            elif args.format == "bin":
                raise NotImplementedError("BIN output is not currently supported, sorry ☹️")
            f.write(result)
    except Exception as e:
        print("output panic: ", e)


if __name__ == "__main__":
    main()
