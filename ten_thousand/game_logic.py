# Imports the `random` module which provides the function for generating random numbers
import random

# Defines a class which is used to bundle data and functionality
class GameLogic:

#Decorator that indiciates the following method is a static method
    @staticmethod
    def calculate_score(dice):
        """
        Calculate the score for a given dice roll.
        """
        # Checks if the `dice` tuple is empty. If it is the function will return 0 since there is no score
        if not dice:
            return 0

        # Counts the occurrences of each dice value
        counts = {x: dice.count(x) for x in set(dice)}

        # Checks for a straight
        if len(counts) == 6:
            return 1500

        # Checks for three pairs
        if len(counts) == 3 and all(count == 2 for count in counts.values()):
            return 1500

        # Initializes a variable `score` set to 0 and is then used to accumulate the total score
        score = 0
        # Starts a loop
        for num, count in counts.items():
            # Checks the current dice value to see if it appears three or more times in a roll
            if count >= 3:
                # Calculates score for three or more ones
                if num == 1:
                    score += 1000 * (count - 2)  
                # Calculates score of three or more dice values other than one
                else:
                    score += num * 100 * (count - 2) 
            
            # Adds 100 points to the score for each individual one that is not part of a set of three or more
            if num == 1 and count < 3:
                score += count * 100
            # Adds 50 points to the score for each individual five that is not part of a three or more set
            elif num == 5 and count < 3:
                score += count * 50

        # Returns the total calculated score
        return score


    @staticmethod
    # Defines another static method where it adds an integer as an argument representing the number of dice to roll
    def roll_dice(number):
        """
        Roll a specified number of dice and return their values.
        """
        # Returns tuple of random integers between one and six simulating the rolling of dice
        return tuple(random.randint(1, 6) for _ in range(number))
    
    @staticmethod
    def get_scorers(dice):
        """
        Returns a tuple of dice that can be scored.
        """
        if not dice:
            return tuple()

        counts = {x: dice.count(x) for x in set(dice)}
        scoring_dice = []

        for num, count in counts.items():
            if num == 1 or num == 5:
                scoring_dice.extend([num] * count)
            elif count >= 3:
                scoring_dice.extend([num] * count)

        return tuple(scoring_dice)

    @staticmethod
    def validate_keepers(roll, keepers):
        """
        Validates whether keepers are a subset of roll.
        """
        roll_counts = {x: roll.count(x) for x in set(roll)}
        keepers_counts = {x: keepers.count(x) for x in set(keepers)}
        return all(keepers_counts.get(die, 0) <= roll_counts.get(die, 0) for die in keepers_counts)
