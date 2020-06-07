"""
Try the Monty Hall problem yourself!
Different number of doors (>=3) can be used to further exaggerate the problem.

Author: Max K Burton
"""

import random


# Selects the correct door if it exists in iter_doors, otherwise picks a random door.
# NOTE: Written as such to make clear the reason why switching doors is the better choice.
def remove_incorrect_doors(iter_doors, correct_door):
    if correct_door in iter_doors:
        return correct_door
    else:
        return random.choice(iter_doors)


# Randomly choose the door with the prize
def choose_correct_door(iter_doors):
    return random.choice(iter_doors)


# Number of user plays and wins
victories = 0
plays = 0
num_doors = 3

try:
    num_doors = int(input("Enter the number of doors to test with (must be >= 3).\n"))
except ValueError:
    print("ValueError: Ensure arguments are integers.\n")
    exit(1)

# Loop until player exits
while True:
    doors = list(range(1, num_doors + 1))
    correct_door = choose_correct_door(doors)
    # Initialise door
    picked_door = 1
    try:
        picked_door = int(input("\nPick a door (Between 1 and %d).\n" % num_doors))
        if picked_door < 1 or picked_door > num_doors:
            print("Door out of range!\n")
            continue
        doors.remove(picked_door)
    except ValueError:
        print("ValueError: Ensure arguments are integers.\n")
        continue
    remaining_door = remove_incorrect_doors(doors, correct_door)
    print("I have opened %d incorrect door(s), leaving only your door and door #%d unopened." %
          (num_doors - 2, remaining_door))
    while True:
        swap = input("Do you want to swap doors? (y/n)\n")
        if swap == "y":
            picked_door = remaining_door
            break
        elif swap == "n":
            break
        else:
            print("Unrecognised command, please enter y or n\n")

    print("The prize is behind...\nDoor #%d!" % correct_door)
    if picked_door == correct_door:
        print("Congratulations, you've won the prize! Did you make the right choice?\n")
        victories += 1
    else:
        print("Unlucky! Did you make the right choice?\n")
    plays += 1
    print("So far, you've won %d times, giving you a win percentage of %.2f%%\n" % (victories, victories/plays*100))

    restart = input("Type r to play again. Type anything else to exit.\n")
    if restart != "r":
        break
