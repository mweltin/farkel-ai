from player import Player
from play import roll, show_roll
from roll_eval import RollEval


def main(number_of_players=2):
    player_lst = []
    for x in range(number_of_players):
        player_lst.append(Player('player ' + str(x + 1)))

    for player in player_lst:
        print(player)
        dice_in_play = 6
        while not player.done:
            current_roll = roll(dice_in_play)
            show_roll(current_roll)
            roll_eval = RollEval(current_roll)
            if roll_eval.is_farkel:
                print("Farkeled!")
                player.done = True
                break
            else:
                roll_eval.show_scoring_choices()
            player.done = True


if __name__ == "__main__":
    main()
