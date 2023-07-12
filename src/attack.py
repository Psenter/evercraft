class Attack: 
    def __init__(self, roll, armor):
        self.roll = 20
        self.armor = armor

    def can_attack(self):
        self.roll >= self.armor