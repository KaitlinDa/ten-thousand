# Assignment
I worked with ChatGPT in order to make a game known as Ten Thousand. 

## Prompts I asked ChatGPT with their answer
1. "Can you show me how to add a calculate_score static method to the GameLogic class? This will be for a game known as Ten Thousand"
* class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        """
        Calculate the score for a given dice roll.

        Parameters:
        dice_roll (tuple): A tuple of integers representing the dice roll.

        Returns:
        int: The score calculated from the dice roll.
        """
        # Initialize the score
        score = 0

        # Implement scoring logic here
        # Example: Add 10 points for each dice showing 1
        for dice in dice_roll:
            if dice == 1:
                score += 10

        # Return the calculated score
        return score

2.  "Can you guide me in writing the calculate_score method according to the game's rules?"
* class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        """
        Calculate the score for a given dice roll based on game rules.

        Parameters:
        dice_roll (tuple): A tuple of integers representing the dice roll.

        Returns:
        int: The score calculated from the dice roll.
        """
        score = 0
        counts = {x: dice_roll.count(x) for x in set(dice_roll)}

        # Scoring for straights
        if len(counts) == 6:
            return 1500

        # Scoring for three of a kind or more
        for num, count in counts.items():
            if count >= 3:
                if num == 1:
                    score += 1000
                else:
                    score += num * 100
                counts[num] -= 3

        # Scoring for single 1's and 5's
        score += counts.get(1, 0) * 100
        score += counts.get(5, 0) * 50

        return score

3. "Can you help me in adding a roll_dice static method to the GameLogic class?"
* import random

class GameLogic:
    # ... [Other methods of the class]

    @staticmethod
    def roll_dice(number_of_dice):
        """
        Roll the dice a specified number of times and return the results.

        Parameters:
        number_of_dice (int): The number of dice to roll.

        Returns:
        tuple: A tuple of integers representing the result of each dice roll.
        """
        return tuple(random.randint(1, 6) for _ in range(number_of_dice))


4. "Can you show me how to implement tthe roll_dice method so that it accepts an integer between 1 and 6 and returns a tuple of random values between 1 and 6?"
* import random

class GameLogic:
    # ... [Other methods of the class]

    @staticmethod
    def roll_dice(number_of_dice):
        """
        Roll the dice a specified number of times and return the results.

        Parameters:
        number_of_dice (int): The number of dice to roll, should be between 1 and 6.

        Returns:
        tuple: A tuple of integers representing the result of each dice roll.
        """
        if 1 <= number_of_dice <= 6:
            return tuple(random.randint(1, 6) for _ in range(number_of_dice))
        else:
            raise ValueError("Number of dice must be between 1 and 6")
