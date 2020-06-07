"""
Proving the Monty Hall problem experimentally.
Different number of doors (>=3) can be used to further exaggerate the problem.
Args: filename num_doors num_iters num_epochs

Author: Max K Burton
"""

import sys
import random


# Set parameters from command line args, else use defaults
def read_command_line_args():
    num_doors = 3
    num_iters = 10000
    num_epochs = 10
    try:
        try:
            num_doors = int(sys.argv[1])
            if num_doors < 3:
                print("Too few doors! Please enter an integer >= 3")
        except IndexError:
            print("No custom argument set, default num_doors used.")
        try:
            num_iters = int(sys.argv[2])
            if num_doors < 1:
                print("Too few iterations! Please enter an integer > 0")
        except IndexError:
            print("No custom argument set, default num_iters used.")
        try:
            num_epochs = int(sys.argv[3])
            if num_doors < 1:
                print("Too few epochs! Please enter an integer > 0")
        except IndexError:
            print("No custom argument set, default num_epochs used.")
    except ValueError:
        print("ValueError: Ensure arguments are integers.\n")
        exit(1)

    print("Using %d doors, %d iterations and %d epochs\n" % (num_doors, num_iters, num_epochs))
    return num_doors, num_iters, num_epochs


# Selects the correct door if it exists in iter_doors, otherwise picks a random door.
# NOTE: Written as such to make clear the reason why switching doors is the better choice.
def remove_incorrect_doors(iter_doors, correct_door):
    if correct_door in iter_doors:
        return correct_door
    else:
        return random.choice(iter_doors)


# Randomly pick a door, and remove it from iter_doors
def pick_door(iter_doors):
    picked_door = random.choice(iter_doors)
    iter_doors.remove(picked_door)
    return picked_door, iter_doors


# Randomly choose the door with the prize
def choose_correct_door(iter_doors):
    return random.choice(iter_doors)


def pre_swap(doors):
    iter_doors = doors.copy()
    correct_door = choose_correct_door(iter_doors)
    picked_door, iter_doors = pick_door(iter_doors)
    remaining_door = remove_incorrect_doors(iter_doors, correct_door)
    return correct_door, picked_door, remaining_door


num_doors, num_iters, num_epochs = read_command_line_args()
doors = list(range(1, num_doors + 1))

# Run the experiment num_epochs times to ensure no bias
for i in range(num_epochs):
    print("Epoch %d:" % (i+1))
    victory_tally_no_swap = 0
    victory_tally_swap = 0

    # Run the experiment num_iters times for each action (swap or no swap)
    for j in range(num_iters):
        correct_door, picked_door, remaining_door = pre_swap(doors)
        # No swap
        if picked_door == correct_door:
            victory_tally_no_swap += 1
        # Swap
        if remaining_door == correct_door:
            victory_tally_swap += 1

    # Calculate percentage of winning cases when the door is not swapped
    victory_percentage_no_swap = victory_tally_no_swap / num_iters * 100
    victory_percentage_swap = victory_tally_swap / num_iters * 100
    # NOTE: %% prints a literal % character
    print("No Swap victory %%: %.2f%%\nSwap victory %%: %.2f%%\n" % (victory_percentage_no_swap, victory_percentage_swap))
