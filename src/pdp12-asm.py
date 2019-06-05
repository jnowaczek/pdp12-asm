import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PDP-12 LAP6-DIAL Assembler')
    parser.add_argument('in_file')
    parser.add_argument('out_file')
    args = parser.parse_args()