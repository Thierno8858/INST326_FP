import random
import pandas as pd
import seaborn as sns

class Character:
    """
    A class representing a character in a game with a set of attributes and actions.
    The class and its methods completed by Thierno, demonstrating custom classes and optional parameters.
    Attributes:
    - difficulty (str): The difficulty level for determining the starting number of lives.
      Options: "easy", "normal", "hard".
    - lives (int): The current number of lives the character has.

    Methods:
    - __init__(self, difficulty="normal"): Initialize a Character instance based on the selected difficulty.
    - display_stats(self, critical_threshold=2): Display the character's lives, indicating if in critical condition.
    - gain_life(self, amount=1): Gain lives by the specified amount.
    - lose_life(self, amount=1): Lose lives by the specified amount.
    - attack(self): Simulate an attack and determine its success.
    - _set_starting_lives(self): Set the starting number of lives based on the selected difficulty.
    - _get_valid_difficulty(self, difficulty_input): Get a valid difficulty level from user input.
    """
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
        else:  
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
        
        lives_message = f"Lives: {self.lives}{' (Critical)' if self.lives < critical_threshold else ''}"

        
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


class Game():
    """
    A class representing a game environment with challenges and a character.
    The class and its methods completed by Srikar.

    Attributes:
    - character (ChallengePanda): The player character in the game.

    Methods:
    - __init__(self): Initialize a Game instance with a ChallengePanda character.
    - start_panda_fight(self): Start a panda battle challenge for the character.
    - start_obstacle_course(self): Start an obstacle course challenge with a difficulty based on the character's level.
    Returns:
      - str: The result of the obstacle course challenge.

    - start_boss_fight(self): Initiate a boss fight challenge with the current lives of the character.
    """
    def __init__(self):
        """
        Initialize a Game instance with a ChallengePanda character.
        """
        self.character = ChallengePanda()

    def start_panda_fight(self):
        """
        Start a panda battle challenge for the character.
        Side Effects:
        - Modifies the state of the character by engaging in a panda battle.
        """
        self.character.battle_panda()

    def start_obstacle_course(self):
        """
        Start an obstacle course challenge with a difficulty based on the character's level.
        Returns:
        - str: The result of the obstacle course challenge.
        Side Effects:
        - May modify the state of the character based on the outcome of the challenge.
        """
        obstacle_course_challenge = ObstacleCourse(difficulty=self.character.difficulty)
        return obstacle_course_challenge.play_game()
        obstacle_course_challenge = ObstacleCourse(difficulty=self.character.difficulty)
        return obstacle_course_challenge.play_game()

    def start_boss_fight(self):
        """
        Initiate a boss fight challenge with the current lives of the character.
        Side Effects:
        - Modifies the state of the character by engaging in a boss fight.
        """
        boss_fight = Bossfight(current_lives=self.character.lives)
        boss_fight.battle_boss()

class ObstacleCourse(Character):
    OPERATIONS = ["intersection", "union", "difference"]
    OBSTACLE_COUNT = 3

    def __init__(self, difficulty="normal"):
        super().__init__(difficulty)
        self.obstacle_count = 0
        
    def play_game(self):
        while True:
            input("Press Enter to navigate to the next platform...")
            challenge_completed = self.handle_platform_challenge()
            if not challenge_completed:
                return False  
        return True  
    
    def generate_random_platform(self):
        platforms = [
            {'A', 'B', 'C'},
            {'C', 'D', 'E'},
            {'B', 'D', 'F'},
            {'A', 'C', 'F'},
            {'B', 'E', 'F'},
            {'C', 'D', 'F'},
            {'A', 'B', 'E'},
            {'D', 'E', 'F'},
            {'A', 'C', 'D'},
        ]
        return random.choice(platforms)

    def generate_random_operation(self):
        return random.choice(self.OPERATIONS)

    def parse_user_guess(self, user_guess_str):
        try:
            elements = [el.strip().upper() for el in user_guess_str.replace('{', '').replace('}', '').split(',') if el.strip()]
            return set(elements)
        except Exception as e:
            print(f"Invalid input format: {e}")
            return None

    def handle_platform_challenge(self):
        set_operation = self.generate_random_operation()
        platform1 = self.generate_random_platform()
        platform2 = self.generate_random_platform()

        print(f"Challenge on platforms {platform1} and {platform2} using operation: {set_operation}")

        if set_operation == "intersection":
            correct_result = platform1.intersection(platform2)
        elif set_operation == "union":
            correct_result = platform1.union(platform2)
        elif set_operation == "difference":
            correct_result = platform1.difference(platform2)

        for attempt in range(3):
            user_guess_str = input(f"Guess the result of the {set_operation} operation: ")
            user_guess = self.parse_user_guess(user_guess_str)

            if user_guess is None:
                print("Please enter a valid set.")
                continue

            if user_guess == correct_result:
                print("Challenge successfully overcome!")
                self.obstacle_count += 1
                print('"Congratulations, excellent work my pupil')
                user_progression = input("'Are you ready to move onwards?', the wise mage Aric asks (yes/no) ")
                if user_progression == "yes":
                    boss_fight = Bossfight()
                    boss_fight.battle_boss()
                else:
                    print("Too bad, my child you must move forward regardless of if you are ready")
                    boss_fight = Bossfight()
                    boss_fight.battle_boss()
                break
            else:
                if attempt == 2:
                    print("Challenge failed three times. Moving to the next platform.")
                    boss_fight = Bossfight()
                    boss_fight.battle_boss()
                    return
                else:
                    print("Challenge failed! Try again.")

        if self.obstacle_count == self.OBSTACLE_COUNT:
            print("Congratulations! You've passed all obstacles and gained an extra life!")
            self.lives = Character.gain_life()
            self.obstacle_count = 0

            return True
        return False



    def play_game(self):
        while True:
            input("Press Enter to navigate to the next platform...")
            if not self.handle_platform_challenge():
                break




#ObstacleCourse ends here




class ChallengePanda(Character):
    def __init__(self):
        """
        Initialize a ChallengePanda instance.

        This class represents the player's character in a battle against a fierce panda in a computer-themed world. The
        character's attributes and progress are tracked during the battle.

        Args:
            None

        Side Effects:
            - Initializes the character's attributes, including lives and difficulty level.
            - Sets the continue_fight flag to True, indicating that the battle is ongoing.

        Returns:
            None
        """
        super().__init__()
        self.continue_fight = True

    def battle_panda(self):
        """
        Start the battle with a panda.

        This method initializes a battle with a fierce panda in a computer-themed world. It prompts the user to choose a
        difficulty level for the battle, then engages the user in a turn-based combat scenario. The user can choose to
        attack or not, and the panda will counterattack if not defeated. After the battle, the user may have the option
        to take on an obstacle course challenge or face a boss fight, depending on the outcome.

        Args:
            None

        Side Effects:
            - Prints messages to the console to narrate the battle.
            - Prompts the user for input and processes user choices.
            - May lead to the creation and execution of an obstacle course challenge or a boss fight.

        Returns:
            None
            
        Start the battle with a panda. Prompt the user to input difficulty and attack the panda.
        """
        print("""
                You are Oop. Oop is an INST326 student with a programming final project that's left him utterly overwhelmed. 
                All of a sudden bugs overrun your computer and you are immersed in the dangerous world of your computer,
                guided only by the things you learned and the wise mage, Aric.
                He warns you of beasts that lurk yet you feel woefully unprepared, when all of a sudden...
              """)
        print("You encounter a fierce panda! Get ready for battle.")

        
        difficulty_input = input("Choose difficulty (easy, normal, hard): ")
        self.difficulty = self._get_valid_difficulty(difficulty_input)
        self.lives = self._set_starting_lives()

        print(f"You chose {self.difficulty} difficulty. Starting with {self.lives} lives.")

        
        while self.lives > 0 and self.continue_fight:
            print("\n--- Round Start ---")
            self.display_stats()

            
            while True:
                attack_input = input("Do you want to attack? (yes/no): ").lower()
                if attack_input in ["yes", "no"]:
                    break
                else:
                    print("Invalid input! Please enter 'yes' or 'no'.")

            if attack_input == "yes":
                if self.attack():
                    print("""You defeated the panda! Having proved yourself, Aric entrusts you to embark on an obstacle course challenge""")
                    challenge_choice = input("Do you want to take on another challenge for a chance to recieve another life? He asks (yes/no): ").lower()
                    while challenge_choice not in ["yes", "no"]:
                        print("Invalid input! Please enter 'yes' or 'no'.")
                        challenge_choice = input("Do you want to take on another challenge for a chance to recieve another life? (yes/no): ").lower()

                    if challenge_choice == "yes":
                        obstacle_course_challenge = ObstacleCourse(difficulty=self.difficulty)
                        obstacle_course_challenge.play_game()
                        self.continue_fight = False  
                        break
                    else:
                        print("You decided not to take on another challenge.")
                        self.continue_fight = False  # Set to False as the fight is over
                        boss_fight = Bossfight()
                        boss_fight.battle_boss()
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
                



class Bossfight(Character):
    """Bilal:
    This class initializes the bossfight class where the player takes on a more challenging opponent.
    When the player

    Args:
        Character (Class): This is the character class bringing in the character specs.
    Returns:
        This will return a scatterplot png file that brings the player out of the computer
    """
    def __init__(self, boss_name="Finale Projectus", boss_health=25):
        super().__init__()
        self.boss_name = boss_name
        self.boss_health = boss_health

    def attack_boss(self):
        """
        Attack the boss and calculate damage. Generates random number between 1 and 7 for # of damage dealt
        Side Effects:
        - Prints information about the attack damage and the boss's remaining health.
        - Modifies the boss's health based on the damage dealt.

        Returns:
        bool: True if the boss is defeated (boss's health <= 0), False otherwise
        """
        damage = random.randint(1, 7)  # Random damage between 1 and 7
        print(f"You attack the boss dealing {damage} damage.")
        self.boss_health -= damage

        if self.boss_health <= 0:
            print(f"You have defeated {self.boss_name}!")
            return True
        else:
            print(f"{self.boss_name} has {self.boss_health} health remaining.")
            return False
    
    def boss_counterattack(self):
        """
        Boss makes a counterattack with a 1 in 3 chance.
        """
        if random.randint(1, 3) == 1:  # 1 in 3 chance
            print(f"The {self.boss_name} counterattacks!")
            self.lose_life()
            if self.lives > 0:
                print(f"You have {self.lives} lives remaining.")
            else:
                print("You have been defeated by the boss!")


    def battle_boss(self):
        """Conducts a battle against a boss character in a game.
        This method manages a turn-based battle between the player and a boss. The player is given an option to attack 
        each turn. If the player attacks, there is a chance the boss might be defeated or counterattack. The battle 
        continues until either the boss is defeated or the player loses all lives. Upon defeating the boss, the player 
        is prompted to visualize a 'scroll' using a scatter plot generated from a CSV file.

    Side Effects:
        - Prints battle status, instructions, and outcomes to the console.
        - Reads data from 'FPscroll.csv' and creates a scatter plot saved as 'scroll_visualization.png' if the boss is defeated.
        - Modifies the instance's state, including updating the boss's health and the player's lives.
        - Waits for and processes user input during the battle.

    Returns:
        None. However, if the boss is defeated, a scatter plot is saved as an image file 'scroll_visualization.png'.
        """
        print("""Prepare yourself Oop, this battle is not for the faint of heart.
              This opponent has a 1 in 3 chance of counterattacking and claiming one of your lives.
              Good luck.""")
        print(f"You have encountered {self.boss_name}, prepare for battle!")
        
        while self.lives > 0 and self.boss_health > 0:
            print("\n--- Round Start ---")
            self.display_stats()

            attack_input = input("Do you want to attack? (yes/no): ").lower()
            while attack_input not in ["yes", "no"]:
                print("Invalid input! Please enter 'yes' or 'no'.")
                attack_input = input("Do you want to attack? (yes/no): ").lower()

            if attack_input == "yes":
                boss_defeated = self.attack_boss()
                if boss_defeated:
                    print("You defeated the Boss and he dropped an indecipherable scroll. \n Aric tells you you must *visualize* the scroll")
                    viz_input = input("Are you ready to visualize the scroll? (yes/no): ")
                    while viz_input not in ["yes", "no"]:
                        print("Invalid input! Please enter 'yes' or 'no'.")
                    if viz_input == "yes":
                        df = pd.read_csv("FPscroll.csv")
                        plot = sns.scatterplot(x='col1', y='col2', data=df, color='red')
                        plot.set_title('Great Job!')
                        plot.set_ylabel('You Win!')
                        plot.set_xlabel('You have defeated the enemies and escaped the computer!')
                        plot.savefig('scroll_visualization.png')

                    break
                else:
                    if random.randint(1, 3) == 1:  # 1 in 3 chance
                        print(f"The {self.boss_name} counterattacks!")
                        self.lose_life()
                    if self.lives > 0:
                        print(f"You have {self.lives} lives remaining.")
                    else:
                        print("You have been defeated by the boss!")
            else:
                print(f"You choose not to attack. {self.boss_name} is waiting.")
    
        if self.lives == 0:
            print("Game Over! You have been defeated.")


import argparse
import sys 


if __name__ == "__main__":
    game = Game()
    if game.start_panda_fight():
        print("Do you want to take on the obstacle course? (yes/no): ")
        if input().lower() == "yes":
            if game.start_obstacle_course():
                print("Do you want to proceed to the boss fight? (yes/no): ")
                if input().lower() == "yes":
                    game.start_boss_fight()
                else:
                    print("Game Over. You chose not to fight the boss.")
            else:
                print("Game Over. You failed the obstacle course.")
        else:
            print("Game Over. You chose not to take on the obstacle course.")

def parse_arguments():
    """
    Bilal:
    Parse command line arguments. This takes the program and allows it to run from the commandline with an optional argument for difficulty.
    Returns: parser
    """
    parser = argparse.ArgumentParser(description='Run the adventure game from the command line.')
    parser.add_argument('-d', '--difficulty', type=str, choices=['easy', 'normal', 'hard'], default='normal',
                        help='Set the difficulty of the game (easy, normal, hard)')
    return parser.parse_args()