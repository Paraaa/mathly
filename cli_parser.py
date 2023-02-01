import argparse


parser = argparse.ArgumentParser(
    prog="Mathly",
    description="Program to train you math skills."
)

parser.add_argument("-d", "--difficulty",
                    help="Specify the difficulty level (default: L1)")

# TODO: Add option for adding/subtracting/multiplication/division/log/sin/cos etc.
# TODO: Add option for only positive solution/negative solutions
