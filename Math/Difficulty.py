from Math.BasicGenerator import BasicGenerator

from enum import Enum


class Difficulty(Enum):
    L1 = BasicGenerator((1, 9))
    L2 = BasicGenerator((1, 19))
