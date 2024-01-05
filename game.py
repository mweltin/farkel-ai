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
                choice_list = roll_eval.get_scoring_choices()
            for idx, choice in enumerate(choice_list):
                print(f"{idx}: {choice['name']} {choice['value']}")
            score_choice = input("Choose a scoring option: ")
            player.score += choice_list[score_choice]['value']
            dice_in_play -= choice_list[score_choice]['num_of_dice']
            if dice_in_play >= 1:
                keep_rolling = input("Continue rolling [y/n]: ")
            else:
                player.done = True
            if keep_rolling == 'n':
                player.done = True
            if player.done:
                print(f"{player} {player.score}")


if __name__ == "__main__":
    main()
