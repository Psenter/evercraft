from character import Character

class Fighter(Character):
    def __init__(self):
        super().__init__()
        self.hit_points = 10
        self.attack_bonus_per_level = 1
        self.hit_points_per_level = 10

    def attack(self, roll, enemy):
        if roll == 20:
            self.gain_experience(10)
            return True
        attack_roll = roll + self.get_strength_modifier() + self.attack_bonus_per_level * (self.level // 2)
        if attack_roll >= enemy.get_armor_class():
            self.gain_experience(10)
            return True
        return False

    def get_hit_points(self):
        constitution_modifier = self.get_constitution_modifier()
        return max(1, self.hit_points + constitution_modifier + self.hit_points_per_level * (self.level - 1))

    def level_up(self):
        super().level_up()
        constitution_modifier = self.get_constitution_modifier()
        self.hit_points += self.hit_points_per_level + constitution_modifier