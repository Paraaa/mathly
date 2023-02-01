import operator


class MathGenerator():

    def __init__(self):
        """
        A list of usable operators shared among the subclasses
        which inherit this class.
        """
        self.ops = {'+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul,
                    '/': operator.truediv}

    def create_problem(self):
        """
        Implements the logic to generate a math problem based on a
        difficulty level
        """
        pass

    def check_solution(self, user_solution, true_solution):
        """
        Check whether the user correctly answered the question.
        If the input is not valid (i. e. contains letter or special
        characters) the method will catch a value error from the float()
        method.

        Args:
            user_solution (string): Input gathered from the user.
                                    Will be converted to a string
            true_solution (float): Correct answer to the question.
        """
        try:
            user_solution = float(user_solution)
            if user_solution == true_solution:
                print("Correct!\n")
            else:
                print(f"Solution was: {true_solution}\n")
        except ValueError:
            print("Input was not valid")
