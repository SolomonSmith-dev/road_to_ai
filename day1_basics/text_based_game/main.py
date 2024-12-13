import random

# Room class
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

# Combat Strategy Base Class
class CombatStrategy:
    def attack(self, attacker, defender):
        raise NotImplementedError("This method should be overridden by subclasses.")

# Melee Combat Strategy
class MeleeCombat(CombatStrategy):
    def attack(self, attacker, defender):
        damage = 10  # Example melee damage
        defender.health -= damage
        print(f"{attacker.name} attacks {defender.name} with melee for {damage} damage!")

# Magic Combat Strategy
class MagicCombat(CombatStrategy):
    def __init__(self):
        self.mana = 50

    def attack(self, attacker, defender):
        if self.mana >= 10:
            damage = 20  # Example magic damage
            self.mana -= 10
            defender.health -= damage
            print(f"{attacker.name} casts a spell on {defender.name} for {damage} damage!")
        else:
            print("Not enough mana to cast magic!")

# Enemy class
class Enemy:
    def __init__(self, name, health, attack_damage):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

# Player class
class Player:
    def __init__(self, name, combat_strategy):
        self.name = name
        self.health = 100
        self.combat_strategy = combat_strategy
        self.inventory = []

    def attack(self, enemy):
        self.combat_strategy.attack(self, enemy)

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")

    def use_item(self, item):
        if item in self.inventory:
            if item == "Health Potion":
                self.health += 20
                self.inventory.remove(item)
                print(f"You used a Health Potion! Health is now", self.health)
        else:
            print(f"You don't have that item.")

# GameState class to manage the current room
class GameState:
    def __init__(self):
        self.current_room = None

    def set_current_room(self, room):
        self.current_room = room

    def get_current_room(self):
        return self.current_room

# Setup rooms
entrance = Room(name="Entrance", description="You are at the entrance of a dark castle.", items=["Torch", "Map"])
hallway = Room(name="Hallway", description="A narrow, dark hallway.", items=["Health Potion"])

# Add exits to rooms
entrance.add_exit("north", hallway)
hallway.add_exit("south", entrance)

# Setup player and combat system
combat_strategy = MeleeCombat()  # Choose MeleeCombat or MagicCombat
player = Player(name="Hero", combat_strategy=combat_strategy)

# Setup enemy
enemy = Enemy(name="Goblin", health=30, attack_damage=10)

# Create game state and set initial room
game_state = GameState()
game_state.set_current_room(entrance)

# Game loop
goblins_defeated = 0
while True:
    current_room = game_state.get_current_room()
    print(f"\nCurrent room: {current_room.name}\n{current_room.description}")
    print(f"Items in this room: {', '.join(current_room.items)}")
    print(f"Hero's Health: {player.health}")
    print(f"Inventory: {', '.join(player.inventory)}")

    action = input("\nWhat will you do? (Move [north/south]/Take [item]/Use [item]/Attack): ").lower()

    if action.startswith("move"):
        direction = action.split()[1]
        if direction in current_room.exits:
            game_state.set_current_room(current_room.exits[direction])
            print(f"You moved {direction}.")
        else:
            print(f"You can't go that way.")
    elif action.startswith("take"):
        item = action.split()[1]
        if item in current_room.items:
            player.add_to_inventory(item)
            current_room.items.remove(item)
        else:
            print("Item not in this room.")
    elif action.startswith("use"):
        item = action.split()[1]
        player.use_item(item)
    elif action == "attack":
        if enemy.health > 0:
            player.attack(enemy)
            if enemy.health <= 0:
                goblins_defeated += 1
                print(f"You defeated a Goblin! Goblins defeated: {goblins_defeated}")
                if goblins_defeated >= 3:
                    print("You defeated 3 goblins! You win!")
                    break
        else:
            print("No enemy to attack.")
    else:
        print("Invalid action.")
