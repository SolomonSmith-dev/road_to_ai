class Observer:
    """Observer base class."""
    def update(self, message):
        raise NotImplementedError("This method should be overridden by subclasses.")

class UI(Observer):
    """UI class that observes game changes."""
    def update(self, message):
        print(f"UI Update: {message}")
