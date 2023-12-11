import random
import pandas as pd
import seaborn as sns

class Bossfight(Character):
    def __init__(self, boss_name="Finale Projectus", boss_health=25):
        super().__init__()
        self.boss_name = boss_name
        self.boss_health = boss_health

    def attack_boss(self):
        """
        Attack the boss and calculate damage. Generates random number between 1 and 7 for # of damage dealt
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
                    viz_input = input("Are you ready to visualize the scroll? (yes/no): ")
                    while viz_input not in ["yes", "no"]:
                        print("Invalid input! Please enter 'yes' or 'no'.")
                    if viz_input == "yes":
                        df = pd.read_csv("FPscroll.csv")
                        plot = sns.scatterplot(x='col1', y='col2', data=df, color='red')
                        plot.set_title('Great Job!')
                        plot.set_ylabel('You Win!')
                        plot.set_xlabel('You have defeated the enemies and escaped the computer!')

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


