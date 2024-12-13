class GameState:
    """Singleton class for managing the game state."""
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.reset()
        return cls._instance

    def reset(self):
        """Reset the game state."""
        self.player = None
        self.current_room = None

    def set_player(self, player):
        """Set the player in the game state."""
        self.player = player

    def set_current_room(self, room):
        """Set the current room in the game state."""
        self.current_room = room

    def get_player(self):
        return self.player

    def get_current_room(self):
        return self.current_room
