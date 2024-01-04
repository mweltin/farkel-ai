from random import randint


def roll(dice_in_play):
    current_role = []
    for x in range(dice_in_play):
        current_role.append(randint(1, 6))
    return current_role


def show_roll(roll):
    for x in roll:
        print(x, end=" ")
    print()
