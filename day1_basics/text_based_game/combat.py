class CombatStrategy:
    def attack(self, attacker, defender):
        raise NotImplementedError("This method should be overridden by subclasses.")

class MeleeCombat(CombatStrategy):
    def attack(self, attacker, defender):
        damage = 10  # Example melee damage
        defender.health -= damage
        print(f"{attacker.name} attacks {defender.name} with melee for {damage} damage!")

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
