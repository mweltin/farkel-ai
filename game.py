from player import Player

def main():
    player1 = Player()
    player2 = Player()
    dice_in_play = 6

    while player1.score < 10000 or player2.score < 10000:
        player1.roll_dice(dice_in_play)
        player1.show_scoring_choices()
        choice = input("make a choice: ")
        player1.pick_scoring_option(choice)
        choice = input("roll again: ")
        return

if __name__ == "__main__":
    main()