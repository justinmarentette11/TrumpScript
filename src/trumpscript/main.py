import argparse

from src.trumpscript.compiler import *
from src.trumpscript.utils import *

__author__ = 'github.com/samshadwell'


def start():
    parser = argparse.ArgumentParser(prog='TRUMP', description='Make programming great again')
    parser.add_argument('--Wall', action='store_true', help='If set, prevents running program from Mexican locales')
    parser.add_argument('--Brainwash', action='store_true', help='If set, exposes Trump to a small amount of education.'
                        'Disables lie/fact flip-flopping')
    parser.add_argument('--shut-up', action='store_true', help='If set, ignore all system warnings and run program. '
                                                               'Overrides --Wall')
    parser.add_argument('program', nargs=1, help='TrumpScript program to run')
    args = parser.parse_args()

    if not os.path.isfile(args.program[0]):
        print("Invalid file specified,")
        return

    # Decide whether to ignore system warnings
    if not args.shut_up:
        Utils.verify_system(args.Wall)
    flip_flopping = not args.Brainwash
    # Compile and go
    Compiler().compile(sys.argv[-1], flip_flopping, {})


if __name__ == "__main__":
    start()
