from functools import reduce
from typing import Tuple

"""A robot has been given a list of movement instructions. Each instruction
is either left, right, up or down, followed by a distance to move. The
robot starts at 0, 0. You want to calculate where the robot will end up
and return its final position as a list. For example, if the robot is given
the instructions ["right 10", "up 50", "left 30", "down 10"], it will end
up 20 left and 40 up from where it started, so you should return [-20, 40].
"""

def map_dir_to_pair(d_val_str) -> Tuple[int, int]:
    direction, v_str = d_val_str.split(' ')
    val = int(v_str)

    if direction == "up":
        res = (0, val)
    elif direction == "down":
        res = (0, -val)
    elif direction == "right":
        res = (val, 0)
    elif direction == "left":
        res = (-val, 0)
    else:
        # This should never happen but will catch cases where the direction
        # is invalid.
        res = (0, 0)

    return res

def add_val(acc, d_val) -> Tuple[int, int]:
    acc_left, acc_right = acc
    cur_left, cur_right = map_dir_to_pair(d_val)
    return (acc_left + cur_left, acc_right + cur_right)

def mr_roboto(instructions) -> Tuple[int, int]:
    return reduce(add_val, instructions, (0, 0))

def main():
    test_1 = mr_roboto(["right 10", "up 50", "left 30", "down 10"])
    print(f"test1: {test_1}")
    test_2 = mr_roboto(["right 100", "right 100", "up 500", "up 10000"])
    print(f"test2: {test_2}")
    test_3 = mr_roboto([])
    print(f"test3: {test_3}")

