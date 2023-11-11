def play_level(objects, required_objects):
    """Sets the stage for the level where a player needs to collect objects to advance.

    Args:
        objects (list): List of objects present in the level.
        required_objects (list): List of objects the player needs to complete level.
    """
    collected_objects = []

    while True:
        display_level(objects, collected_objects)

        for object in objects:
            if object in required_objects and object not in collected_objects:
                collect_object(collected_objects, object)

        if is_level_completed(collected_objects, required_objects):
            level_completed_event()

def display_level(objects, collected_objects):
    """Displays the current level.
    
    Args:
        objects (list): List of objects present in the level.
        collected_objects (list): List of objects the player has collected.
    
    Side effects:
        Prints both lists of the level.
    """
    print("Objects:", objects)
    print("Collected Objects:", collected_objects)
    print()

def collect_object(collected_objects, object):
    """Action where player collects an object and adds to their collected objects.

    Args:
        collected_objects (list): List of objects the player has collected.
        object (str): The name of the object.
    
    Side Effects:
        Modifies the state of collected_objects list by appending the collected object.
        Prints a message indicating the object has been found.
    """
    print(f" You found {object}!")
    collected_objects.append(object)

def is_level_completed(collected_objects, required_objects):
    """Checks if player acquired all required objects.

    Args:
        collected_objects (list): List of objects the player has collected.
        required_objects (list): List of objects the player needs to complete level.

    Returns:
        bool: True if all required objects are collected and both sets are equal.
    """
    return set(collected_objects) == set(required_objects)

def level_completed_event():
    """Displays a congratulatory message when the player completes the level.

    Side Effects:
        Prints a congratulatory message.
    """
    print("Congratulations! You found all the required items.")
    