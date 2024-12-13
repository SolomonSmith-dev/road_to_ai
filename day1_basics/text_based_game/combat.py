class CombatStrategy:
    def attack(self, attacker, defender):
        raise NotImplementedError("This method should be overridden by subclasses.")

class MeleeCombat(CombatStrategy):
    def attack(self, attacker, defender):
        damage = 10  # Example melee damage
        defender.health -= damage
        print(f"{attacker.name} attacks {defender.name} with melee for {damage} damage!")

class MagicCombat(CombatStrategy):
    def attack(self, attacker, defender):
        damage = 20  # Example magic damage
        defender.health -= damage
        print(f"{attacker.name} casts a spell on {defender.name} for {damage} damage!")
