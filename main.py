import argparse
from lexer import Lexer

parser = argparse.ArgumentParser(description="MiniC files interpreter.")
parser.add_argument("filename", help="Name of MiniC file.", type=str)
args = parser.parse_args()

program = Lexer(args.filename)
program.get_next_token()