class Room:
    """Class representing a room in the game."""
    def __init__(self, name, description, items=None, exits=None):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.exits = exits if exits else {}

    def add_exit(self, direction, room):
        """Add an exit to another room."""
        self.exits[direction] = room