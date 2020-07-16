from typing import Tuple

"""A robot has been given a list of movement instructions. Each instruction
is either left, right, up or down, followed by a distance to move. The
robot starts at 0, 0. You want to calculate where the robot will end up
and return its final position as a list. For example, if the robot is given
the instructions ["right 10", "up 50", "left 30", "down 10"], it will end
up 20 left and 40 up from where it started, so you should return [-20, 40].
"""

def mr_roboto(instructions) -> Tuple[int, int]:
    # If the list is empty then the result will be (0, 0).
    # The solution to this algorithm can be understood as:
    # instr[0] + instr[1] + ... + (0, 0)
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
        # This should never happen but will silently ignore cases where the
        # direction is invalid.
        cur_left, cur_right = (0, 0)

    acc_left, acc_right = mr_roboto(instructions[1:])

    return (acc_left + cur_left, acc_right + cur_right)

def main():
    test_1 = mr_roboto(["right 10", "up 50", "left 30", "down 10"])
    print(f"test1: {test_1}")
    test_2 = mr_roboto(["right 100", "right 100", "up 500", "up 10000"])
    print(f"test2: {test_2}")
    test_3 = mr_roboto([])
    print(f"test3: {test_3}")

