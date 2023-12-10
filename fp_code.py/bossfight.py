class Bossfight:
    def __init__(self):
        self.boss = boss 
        super().__init__()
    def battle_boss(self):
        """
        Start the boss battle. Prompt the user to attack the boss
        """
        print("You have encountered the biggest enemy of them all, prepare for battle!")
        
        while self.lives > 0:
            print("\n--- Round Start ---")
            self.display_stats()
            
            while True:
                attack_input = input("Do you want to attack? (yes/no): ").lower()
                if attack_input in ["yes", "no"]:
                    break
                else:
                    print("Invalid input! Please enter 'yes' or 'no'.")
        
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
                    challenge_choice = input("Do you want to take on another challenge for a chance to recive another life? (yes/no): ").lower()
                    while challenge_choice not in ["yes", "no"]:
                        print("Invalid input! Please enter 'yes' or 'no'.")
                        challenge_choice = input("Do you want to take on another challenge for a chance to recive another life? (yes/no): ").lower()

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
