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
        print("Rolling 6 dice...")
        dice = roller(6)
        print(f"*** {' '.join(map(str, dice))} ***")

        kept_dice = input("Enter dice to keep, or (q)uit:\n> ").strip().lower()
        if kept_dice == 'q':
            print(f"Thanks for playing. You earned {total_score} points")
            break

        kept_dice = tuple(int(d) for d in kept_dice if d.isdigit())
        num_kept_dice = len(kept_dice)

        score_for_kept_dice = GameLogic.calculate_score(kept_dice)
        print(f"You have {score_for_kept_dice} unbanked points and {6 - num_kept_dice} dice remaining")

        decision = input("(r)oll again, (b)ank your points or (q)uit:\n> ").strip().lower()
        if decision == 'b':
            total_score += score_for_kept_dice
            print(f"You banked {score_for_kept_dice} points in round {current_round}")
            print(f"Total score is {total_score} points")
            current_round += 1
        elif decision == 'q':
            print(f"Thanks for playing. You earned {total_score} points")
            break
        elif decision == 'r':
            # Handles the logic for re-rolling the dice
            dice = roller(6 - num_kept_dice)
        else:
            print("Invalid choice. Please choose 'r' to roll again, 'b' to bank, or 'q' to quit.")

# Runs script
if __name__ == "__main__":
    play()
