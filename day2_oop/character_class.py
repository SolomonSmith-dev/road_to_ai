# Define a class for Character that has name, health, and attack_power
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage and now has {self.health} health.")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed by {amount} and now has {self.health} health.")

    def attack(self, other_character):
        print(f"{self.name} attacks {other_character.name} for {self.attack_power} damage!")
        other_character.take_damage(self.attack_power)
        
# Example usage
hero = Character("Hero", 100, 20)
enemy = Character("Goblin", 50, 10)

hero.attack(enemy)
enemy.attack(hero)

#class inheritance
class Mage(Character):
    def __init__(self, name, health, attack_power, magic_power):
        super().__init__(name, health, attack_power)
        self.magic_power = magic_power

    def magic_attack(self, other_character):
        print(f"{self.name} casts a magic attack on {other_character.name} for {self.magic_power} damage!")
        other_character.take_damage(self.magic_power)

# Example usage
mage = Mage("Mage", 80, 15, 30)

mage.attack(enemy)  # Normal attack
mage.magic_attack(enemy)  # Magic attack
