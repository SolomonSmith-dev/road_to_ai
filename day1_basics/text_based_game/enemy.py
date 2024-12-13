class Enemy:
    """Class for enemies."""
    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def take_damage(self, damage):
        self.health -= damage
        self.notify_observers(f"{self.name} took {damage} damage! (Health: {self.health})")
