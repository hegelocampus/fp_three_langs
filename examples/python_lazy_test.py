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
    """While working on this article I learned that Python actually does have
    much better lazy iterators than I had previously thought. I wrote this
    algorithm specifally to show that python won't batch the processing of
    information to reduce the amount of times information needs to actually be
    processes. But, I was proven wrong as this algorithm prints each of the
    data processing steps consequatively just like how they are in the Rust
    implementation. While I will conceed that Python actually does have very
    thoughtfully implemented lazy iterators, this actually saddens and
    frustrates me because Python allows for this sort of breaking up of logic
    into processable bits, but doesn't have the syntax to allow for those
    tangible bits to be displayed in the clearest possible form. I much prefer
    the version of this implemtation that relies on a single reduce() as apposed
    to the map() into the reduce() statement because calling reduce() function
    style on map() for me looks incredibly confusing.
    """
    return reduce(add_val, map(map_dir_to_pair, instructions), (0, 0))

def add_val(acc, d_val) -> Tuple[int, int]:
    print(d_val)
    acc_left, acc_right = acc
    cur_left, cur_right = d_val
    return (acc_left + cur_left, acc_right + cur_right)

def map_dir_to_pair(d_val_str) -> Tuple[int, int]:
    direction, v_str = d_val_str.split(' ')
    val = int(v_str)

    print(d_val_str)
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

main()
