#imports character to this file
from character import Character

#creates a subclass
class Fighter(Character):
    def __init__(self):
        #overrides the inital attributes to set specific ones to this class
        super().__init__()
        self.hit_points = 10
        self.attack_bonus_per_level = 1
        self.hit_points_per_level = 10

    #overrides original attack method
    def attack(self, roll, enemy):
        #if the roll is 20, 10 EXP is gained
        if roll == 20:
            self.gain_experience(10)
            return True
        #adds roll, strength modifier, and the bouns this class gets per level
        attack_roll = roll + self.get_strength_modifier() + self.attack_bonus_per_level * (self.level // 2)
        #checks if is attack if more than enemy armor
        if attack_roll >= enemy.get_armor_class():
            self.gain_experience(10)
            return True
        return False

    #overrides original HP method
    def get_hit_points(self):
        #brings const modifier into the method
        constitution_modifier = self.get_constitution_modifier()
        #calculates by adding HP, const modifier, and the HP gained from levels
        return max(1, self.hit_points + constitution_modifier + self.hit_points_per_level * (self.level))

    #overrides original level up method
    def level_up(self):
        #calls in original level up method so the generic level up is still added into this
        super().level_up()
        #increases HP when leveling up
        self.hit_points += self.hit_points_per_level