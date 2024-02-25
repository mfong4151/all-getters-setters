import argparse

parser = argparse.ArgumentParser(description="Description here")

# Creates positional arguments for n number of arguments, if not needed then comment out or remove
parser.add_argument('args', nargs='*', help="Description here")

# Interpreataion for flags
parser.add_argument('--example', '-e', action='store_true', help='Description here')
