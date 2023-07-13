class Character:

    #-------------------------------------
    #Name, armor, HP, abilities
    def __init__(self):
        self.name = "NightMan"
        self.alignment = "Neutral"
        self.armor_class = 10 
        self.hit_points = 5
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
        return self.armor_class

    def set_armor_class(self, armor_class):
        self.armor_class = armor_class

    def get_hit_points(self):
        return self.hit_points

    def set_hit_points(self, hit_points):
        self.hit_points = hit_points

    #-------------------------------------
    #Attack

    def attack(self,roll, enemy):
        if roll == 20:
            return True
        return roll >= enemy.get_armor_class()

    #-------------------------------------
    #Damage
    
    def damage_taken(self, damage):
        if damage > 0:
            self.hit_points -= damage
        if self.hit_points <= 0:
            self.hit_points = 0

    def is_alive(self):
        return self.hit_points > 0

    #-------------------------------------
    #Abilities

    def get_strength(self, ability):
        return self.abilities[ability]

    def get_dexterity(self, ability):
        return self.abilities[ability]

    def get_constitution(self, ability):
        return self.abilities[ability]

    def get_wisdom(self, ability):
        return self.abilities[ability]

    def get_intellegence(self, ability):
        return self.abilities[ability]

    def get_charisma(self, ability):
        return self.abilities[ability]