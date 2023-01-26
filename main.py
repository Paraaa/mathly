from Generator import MathGenerator
from Difficulty import Difficulty


def main():
    mathGenerator = MathGenerator()
    while (True):
        solution = mathGenerator.create_problem(Difficulty.L1)

        user_input = input(": ")
        try:
            user_input = float(user_input)
        except ValueError:
            print("Input was not valid")
            continue
        mathGenerator.check_solution(user_input, solution)


if __name__ == "__main__":
    main()
