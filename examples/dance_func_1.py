from typing import Tuple

"""A robot has been given a list of movement instructions. Each instruction
is either left, right, up or down, followed by a distance to move. The
robot starts at 0, 0. You want to calculate where the robot will end up
and return its final position as a list. For example, if the robot is given
the instructions ["right 10", "up 50", "left 30", "down 10"], it will end
up 20 left and 40 up from where it started, so you should return [-20, 40].
"""

def mr_roboto(instructions) -> Tuple[int, int]:
    """This sort of niave functional algoritm relies on recursion to solve the
    problem. And thus the "truth" or result of this algoritm is that the
    solution is the sum of the parsed value of each instruction in addition to
    the value of an empty set of instructions, or
    instr[0] + instr[1] + ... + (0, 0).
    Note how in this implementation we are using immutable tuples to store all
    of our values, indication that we are never performing any side-effects
    (e.g., changing values) in our functions. These could just as easily be
    held in lists like they are in the imperative implementation, but I'm using
    tuples in order to make it abundently clear that no value is ever mutated.
    """
    # If the list is empty then the result will be (0, 0). This will also work
    # as the base case for the recursive call of the function. This is the
    # starting value that all later values will be added onto.
    if not instructions:
        return (0, 0)

    current = instructions[0]
    direction, v_str = current.split(' ')
    val = int(v_str)

    if direction == "up":
        cur_left, cur_right = (0, val)
    elif direction == "down":
        cur_left, cur_right = (0, -val)
    elif direction == "right":
        cur_left, cur_right = (val, 0)
    elif direction == "left":
        cur_left, cur_right = (-val, 0)
    else:
        # Silently ignore cases where the direction is invalid.
        cur_left, cur_right = (0, 0)

    # Calculate the result of the rest of the instructions
    acc_left, acc_right = mr_roboto(instructions[1:])

    # Declare that the result strictly is the sum of the current value added to
    # the sum of all of the values in the rest of the list.
    return (acc_left + cur_left, acc_right + cur_right)

def main():
    test_1 = mr_roboto(["right 10", "up 50", "left 30", "down 10"])
    print(f"test1: {test_1}")
    test_2 = mr_roboto(["right 100", "right 100", "up 500", "up 10000"])
    print(f"test2: {test_2}")
    test_3 = mr_roboto([])
    print(f"test3: {test_3}")

