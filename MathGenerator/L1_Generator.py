import random

from MathGenerator.MathGenerator import MathGenerator


class L1_Generator(MathGenerator):

    def __init__(self):
        MathGenerator.__init__(self)
        self.problem_range = (1, 9)

    def create_problem(self):
        """Generator for basic math problems.

        TODO: Maybe return a dataclass with the math problem?

        Returns:
            solution(float): the solution to the generated problem
        """
        num1 = random.randint(*self.problem_range)
        num2 = random.randint(*self.problem_range)

        # Select random operator
        random_operator = random.choice(list(self.ops.keys()))
        # Extract function math function from list
        op = self.ops.get(random_operator)

        solution = op(num1, num2)

        solution = float("{:.2f}".format(solution))

        print(f"What is {num1} {random_operator} {num2}?")
        return solution
