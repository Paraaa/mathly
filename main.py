import sys

from cli_parser import parser
from Math.Difficulty import Difficulty


def main():

    args = vars(parser.parse_args())
    # Base case if no difficulty is specified
    generator = Difficulty.L1.value

    if args['difficulty']:
        try:
            generator = Difficulty[args['difficulty']].value
        except KeyError:
            print(f"The level \"{args['difficulty']}\" does not exist.")
            sys.exit()

    while (True):
        solution = generator.create_problem()
        user_input = input(": ")
        generator.check_solution(user_input, solution)


if __name__ == "__main__":
    main()
