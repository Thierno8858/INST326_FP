import random

class Character:
    def __init__(self, difficulty="normal"):
        """
        Initialize a Character instance based on the selected difficulty.

        Parameters:
        - difficulty (str): The difficulty level for determining the starting number of lives.
          Options: "easy", "normal", "hard".
        """
        self.difficulty = difficulty.lower()
        self.lives = self._set_starting_lives()

    def _set_starting_lives(self):
        """
        Set the starting number of lives based on the selected difficulty.

        Returns:
        - int: The starting number of lives.
        """
        if self.difficulty == "easy":
            return 5
        elif self.difficulty == "hard":
            return 1
        else:  # Default to "normal" difficulty
            return 3

    def display_stats(self, critical_threshold=2):
        """
        Display the character's lives.

        If the number of lives is below the specified critical threshold,
        the lives message will include '(Critical)'.

        Parameters:
        - critical_threshold (int): The lives threshold for considering the character in critical condition.
          Default is set to 2.
        """
        # Display lives
        lives_message = f"Lives: {self.lives}{' (Critical)' if self.lives < critical_threshold else ''}"

        # Print the final message
        print(lives_message)

    def gain_life(self, amount=1):
        """
        Gain lives by the specified amount.

        Parameters:
        - amount (int): The amount of lives to gain. Default is set to 1.
        """
        self.lives += amount

    def lose_life(self, amount=1):
        """
        Lose lives by the specified amount.

        Parameters:
        - amount (int): The amount of lives to lose. Default is set to 1.
        """
        self.lives -= amount
        if self.lives < 0:
            self.lives = 0  # Ensure lives do not go below zero



    def attack(self):
        """
        Simulate an attack. Generates a random number between 1 and 6.
        A roll of 4 or above is a successful attack; otherwise, it's a fail.

        Returns:
        - bool: True if the attack is successful, False otherwise.
        """
        attack_result = random.randint(1, 6)
        success = attack_result >= 4
        if success:
            print("Successful attack!")
        else:
            print("Attack failed!")
        return success

# Example usage:
player = Character(difficulty="hard")
player.display_stats()


# Simulate an attack
attack_success = player.attack()
print(f"Attack successful: {attack_success}")


