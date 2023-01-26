import random
import operator
from Difficulty import Difficulty


class MathGenerator:

    def __init__(self):
        self.ops = {'+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/': operator.truediv}

    def create_problem(self, difficulty: Difficulty):
        problem_range = Difficulty(difficulty).value
        num1 = random.randint(*problem_range)
        num2 = random.randint(*problem_range)

        # Select random operator
        random_operator = random.choice(list(self.ops.keys()))
        # Extract function math function from list
        op = self.ops.get(random_operator)

        solution = op(num1, num2)

        # If the number is float only use two decimal places
        if isinstance(solution, float):
            solution = float("{:.2f}".format(solution))

        print(f"What is {num1} {random_operator} {num2}?")
        return solution

    # TODO: Check solution of floating points with some tolarance
    def check_solution(self, user_solution, true_solution):
        if user_solution == true_solution:
            print("Correct!\n")
        else:
            print(f"Solution was: {true_solution}\n")
