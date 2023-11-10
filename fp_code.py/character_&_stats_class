class Character:
    def __init__(self, health, inventory):
        """
        Initialize a Character instance with the given health and inventory.

        Parameters:
        - health (int): The initial health of the character.
        - inventory (list): The initial items in the character's inventory.
        """
        self.health = health
        self.inventory = inventory

    def display_stats(self, critical_threshold=20):
        """
        Display the character's health and inventory.

        If the health is below the specified critical threshold,
        the health message will include '(Critical)'.

        If the inventory is empty, the inventory message will indicate that there are no items.

        Parameters:
        - critical_threshold (int): The health threshold for considering the character in critical condition.
          Default is set to 20.
        """
        # Display health
        health_message = f"Health: {self.health}{' (Critical)' if self.health < critical_threshold else ''}"

        # Display inventory
        inventory_message = (
            "Inventory: " + ', '.join(self.inventory) if self.inventory else "No items in inventory"
        )

        # Combine messages
        stats_message = f"{health_message}\n{inventory_message}"

        # Print the final message
        print(stats_message)

    def update_health(self, amount):
        """
        Update the character's health by the specified amount.

        Parameters:
        - amount (int): The amount by which to update the character's health.
        """
        self.health += amount

    def update_inventory(self, item):
        """
        Add an item to the character's inventory.

        Parameters:
        - item (str): The item to add to the inventory.
        """
        self.inventory.append(item)