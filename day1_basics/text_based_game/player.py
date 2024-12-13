from combat import CombatStrategy

class Player:
    def __init__(self, name, combat_strategy: CombatStrategy):
        self.name = name
        self.health = 100
        self.combat_strategy = combat_strategy
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")

    def use_item(self, item):
        if item in self.inventory:
            if item == "Health Potion":
                self.health += 20
                self.inventory.remove(item)
                print("You used a Health Potion! Health is now", self.health)
        else:
            print("You don't have that item.")
