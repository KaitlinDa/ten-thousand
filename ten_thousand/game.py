from .game_logic import GameLogic

def play(roller=GameLogic.roll_dice):
    total_score = 0

    print("Welcome to Ten Thousand")
    start_game = input("(y)es to play or (n)o to decline\n> ").strip().lower()
    if start_game != 'y':
        print("OK. Maybe another time")
        return

    current_round = 1
    while True:
        print(f"Starting round {current_round}")
        dice = roller(6)
        print(f"Rolling 6 dice...\n*** {' '.join(map(str, dice))} ***")

        round_score = 0  # Score for the current round

        while True:
            kept_dice_input = input("Enter dice to keep, or (q)uit:\n> ").strip().lower()
            if kept_dice_input == 'q':
                print(f"Thanks for playing. You earned {total_score} points")
                return

            kept_dice = tuple(int(d) for d in kept_dice_input if d.isdigit())
            if not GameLogic.validate_keepers(dice, kept_dice):
                print("Cheater!!! Or possibly made a typo...")
                print(f"*** {' '.join(map(str, dice))} ***")
                continue

            score_for_kept_dice = GameLogic.calculate_score(kept_dice)
            if score_for_kept_dice == 0 and not kept_dice:
                print("****************************************\n**        Zilch!!! Round over         **\n****************************************")
                break

            round_score += score_for_kept_dice
            remaining_dice = 6 - len(kept_dice)
            print(f"You have {round_score} unbanked points and {remaining_dice} dice remaining")

            decision = input("(r)oll again, (b)ank your points or (q)uit:\n> ").strip().lower()
            if decision == 'b':
                total_score += round_score
                print(f"You banked {round_score} points in round {current_round}")
                print(f"Total score is {total_score} points")
                break
            elif decision == 'r':
                if remaining_dice == 0:  # Hot dice scenario
                    print("Rolling 6 dice again...")
                    dice = roller(6)
                else:
                    print(f"Rolling {remaining_dice} dice...")
                    dice = roller(remaining_dice)
                print(f"*** {' '.join(map(str, dice))} ***")
                if GameLogic.calculate_score(dice) == 0:
                    print("****************************************\n**        Zilch!!! Round over         **\n****************************************")
                    break

        current_round += 1

if __name__ == "__main__":
    play()
