from functools import reduce
from typing import Tuple

"""A robot has been given a list of movement instructions. Each instruction
is either left, right, up or down, followed by a distance to move. The
robot starts at 0, 0. You want to calculate where the robot will end up
and return its final position as a list. For example, if the robot is given
the instructions ["right 10", "up 50", "left 30", "down 10"], it will end
up 20 left and 40 up from where it started, so you should return [-20, 40].
"""

def mr_roboto(instructions) -> Tuple[int, int]:
    """I would consider this a slightly more advanced functional solution to
    this problem. It uses the reduce funciton provided by the functools
    library, which although not imported by default, is a library that is
    included in the standard Python library with any Python3+ installation.
    As with the "niave" functional implementation (and any funcitonal
    algoritm) the return value can be expressed as a direct definition, or
    "truth." To be explicit, the return value here is the final accumulator
    value after calling add_val() on each value in instructions, whith the
    initial starting value of (0,0). In other words:
    add_val(add_val(add_val((0, 0), instructions[0]), instructions[1]), ...).
    Note that this implementation also makes use of immutable tuples to hold
    all of our values, indicating that there is never any value being changed
    in the processing of the solution.
    """
    return reduce(add_val, instructions, (0, 0))

def add_val(acc, d_val) -> Tuple[int, int]:
    """Note how the values are never being mutated, but rather we are simply
    using a series of definitions to come to our solution. Rather than
    changing our initial values we are simply retuning new values. This adds
    an additional layer of "safty" to our code because it removes the possibly
    of  accidently or unknowingly changing values. Simply put, you can't
    accidently change a value if you never mutate it.
    """
    acc_left, acc_right = acc
    cur_left, cur_right = map_dir_to_pair(d_val)
    return (acc_left + cur_left, acc_right + cur_right)

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
        # Silently ignore cases where the direction is invalid.
        res = (0, 0)

    return res

def main():
    test_1 = mr_roboto(["right 10", "up 50", "left 30", "down 10"])
    print(f"test1: {test_1}")
    test_2 = mr_roboto(["right 100", "right 100", "up 500", "up 10000"])
    print(f"test2: {test_2}")
    test_3 = mr_roboto([])
    print(f"test3: {test_3}")

