class Character:

    #-------------------------------------
    #Name, armor, HP, abilities
    def __init__(self):
        self.name = "NightMan"
        self.alignment = "Neutral"
        self.armor_class = 10 
        self.hit_points = 5
        self.experience_points = 0
        self.level = 1
        self.abilities = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "wisdom": 10,
            "intellegence": 10,
            "charisma": 10
        }

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    #-------------------------------------
    #Alignment

    def get_alignment(self):
        return self.alignment 

    def set_alignment(self, alignment):
        self.alignment = alignment 
    
    #-------------------------------------
    #Armor and HP

    def get_armor_class(self):
        dexterity_modifier = self.get_dexterity_modifier()
        return self.armor_class + dexterity_modifier

    def set_armor_class(self, armor_class):
        self.armor_class = armor_class

    def get_hit_points(self):
        constitution_modifier = self.get_constitution_modifier()
        return max(1, self.hit_points + constitution_modifier)

    def set_hit_points(self, hit_points):
        self.hit_points = max(1, hit_points)

    #-------------------------------------
    #Attack

    def attack(self, roll, enemy):
        if roll == 20:
            self.gain_experience(10)
            return True
        attack_roll = roll + self.get_strength_modifier()
        if self.level % 2 == 0:
            attack_roll += 1
        if attack_roll >= enemy.get_armor_class():
            self.gain_experience(10)
            return True
        return False

    #-------------------------------------
    #Damage
    
    def damage_taken(self, damage):
        if damage > 0:
            modified_damage = max(1, damage + self.get_strength_modifier())
            self.hit_points -= modified_damage
        if self.hit_points <= 0:
            self.hit_points = 0

    def is_alive(self):
        return self.hit_points > 0

    #-------------------------------------
    #Abilities

    def get_strength(self):
        return self.abilities["strength"]

    def get_dexterity(self):
        return self.abilities["dexterity"]

    def get_constitution(self):
        return self.abilities["constitution"]

    def get_wisdom(self):
        return self.abilities["wisdom"]

    def get_intellegence(self):
        return self.abilities["intellegence"]

    def get_charisma(self):
        return self.abilities["charisma"]

    def set_ability_score(self, ability, score):
        if ability in self.abilities:
            self.abilities[ability] = score

    def change_ability_score(self, ability, modifier):
        if ability in self.abilities:
            self.abilities[ability] += modifier

    def get_strength_modifier(self):
        strength = self.get_strength()
        modifier = (strength - 10) // 2
        return modifier

    def get_dexterity_modifier(self):
        dexterity = self.get_dexterity()
        modifier = (dexterity - 10) // 2
        return modifier

    def get_constitution_modifier(self):
        constitution = self.get_constitution()
        modifier = (constitution - 10) // 2
        return modifier

    #-------------------------------------
    #Experience and levels
    
    def gain_experience(self, points):
        self.experience_points += points

    def gain_experience(self,points):
        self.experience_points += points
        if self.experience_points >= self.get_experience_needed_for_level_up():
            self.level_up()

    def get_experience_points(self):
        return self.experience_points

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def get_experience_needed_for_level_up(self):
        return 1000 * self.level

    def level_up(self):
        self.level += 1
        constitution_modifier = self.get_constitution_modifier()
        self.hit_points += 5 + constitution_modifier

