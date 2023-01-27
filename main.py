from Difficulty import Difficulty


def main():

    # TODO: Make this decidable by the user

    # This gets an instance based on the chosen difficulty
    generator = Difficulty.L1.value

    while (True):
        # create a math problem
        solution = generator.create_problem()

        user_input = input(": ")

        generator.check_solution(user_input, solution)


if __name__ == "__main__":
    main()
