from player import Player

player1 = Player('player 1')
player2 = Player('player 2')


def main():
    current_player = player1

    while player1.score < 10000 or player2.score < 10000:
        dice_in_play = 6
        print(current_player.name+"'s turn")
        choice = 'y'
        while choice == 'y':
            current_player.roll_dice(dice_in_play)
            if current_player.farkeled:
                break
            current_player.show_scoring_choices()
            print("or 'e' to end your turn")
            choice = input("make a choice: ")
            current_player.pick_scoring_option(choice)
            choice = input("roll again [y/n]: ")
        current_player = toggle_current_player(current_player)


def toggle_current_player(_current_player):
    if _current_player == player1:
        return player2
    else:
        return player1


if __name__ == "__main__":
    main()
