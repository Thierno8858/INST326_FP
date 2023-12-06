import random

class Character:
    def __init__(self, difficulty="normal"):
        """
        Initialize a Character instance based on the selected difficulty.

        Parameters:
        - difficulty (str): The difficulty level for determining the starting number of lives.
          Options: "easy", "normal", "hard".
        """
        self.difficulty = self._get_valid_difficulty(difficulty)
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

    def _get_valid_difficulty(self, difficulty_input):
        """
        Get a valid difficulty level from user input.

        Parameters:
        - difficulty_input (str): The user input for the difficulty level.

        Returns:
        - str: The valid difficulty level.
        """
        tries = 3
        while tries > 0:
            if difficulty_input.lower() in ["easy", "normal", "hard"]:
                return difficulty_input.lower()
            else:
                print(f"Invalid input! You have {tries} {'tries' if tries > 1 else 'try'} remaining.")
                difficulty_input = input("Choose difficulty (easy, normal, hard): ")
                tries -= 1
        print("Defaulting to normal difficulty.")
        return "normal"

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

# ObstacleCourse definition here (empty for now)

class ObstacleCourse(Character):
    def __init__(self):
        # Initialize the ObstacleCourse by calling the parent class constructor
        super().__init__()

    def run_obstacle_course(self):
        """
        Simulate running an obstacle course. This method should be implemented by your groupmate.
        """
        # Placeholder code, replace with the actual obstacle course logic
        print("Running the obstacle course... (Replace this with the actual obstacle course code)")
        self.successful_challenge = True  # Placeholder, update based on the actual success or failure


# class (ObstacleCourse) definition ends here




class ChallengePanda(Character):
    def __init__(self):
        # Initialize the ChallengePanda by calling the parent class constructor
        super().__init__()

    def battle_panda(self):
        """
        Start the battle with a panda. Prompt the user to input difficulty and attack the panda.
        """
        print("You encounter a fierce panda! Get ready for battle.")

        # Prompt user to choose difficulty with error handling
        difficulty_input = input("Choose difficulty (easy, normal, hard): ")
        self.difficulty = self._get_valid_difficulty(difficulty_input)
        self.lives = self._set_starting_lives()

        print(f"You chose {self.difficulty} difficulty. Starting with {self.lives} lives.")

        # Battle the panda
        while self.lives > 0:
            print("\n--- Round Start ---")
            self.display_stats()

            # Prompt user to attack with error handling
            while True:
                attack_input = input("Do you want to attack? (yes/no): ").lower()
                if attack_input in ["yes", "no"]:
                    break
                else:
                    print("Invalid input! Please enter 'yes' or 'no'.")

            if attack_input == "yes":
                if self.attack():
                    print("You defeated the panda!")
                    challenge_choice = input("Do you want to take on another challenge? (yes/no): ").lower()
                    while challenge_choice not in ["yes", "no"]:
                        print("Invalid input! Please enter 'yes' or 'no'.")
                        challenge_choice = input("Do you want to take on another challenge? (yes/no): ").lower()

                    if challenge_choice == "yes":
                        # Assuming ObstacleCourse is defined and implemented 
                        obstacle_course_challenge = ObstacleCourse()
                        obstacle_course_challenge.run_obstacle_course()
                        
                        
                        # Check if the challenge is successful and update lives
                        #if obstacle_course_challenge.successful_challenge:
                            #self.gain_life()
                        #else:
                            #self.lose_life()
                            
                            
                    else:
                        print("You decided not to take on another challenge.")
                        break
                else:
                    print("The panda counterattacks! You lose a life.")
                    self.lose_life()
            else:
                print("You decide not to attack. The panda is unimpressed.")
                break

            if self.lives == 0:
                print("Game Over! The panda has defeated you.")
            else:
                print(f"You have {self.lives} lives remaining.")
                
                

# Example usage:
if __name__ == "__main__":
    # Create an instance of ChallengePanda
    challenge_panda = ChallengePanda()

    # Start the battle with the panda
    challenge_panda.battle_panda()