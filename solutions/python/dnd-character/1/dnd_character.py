import random
class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence =self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
        
    def ability(self):
        roll_value = []
        for i in range(4):
            roll_value.append(random.randint(1, 6))

        top_three = sorted(roll_value)[1:]
        return sum(top_three) 

def modifier(value):
    return (value - 10) // 2
