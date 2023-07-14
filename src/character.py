#Creates class named "Character"
class Character:
    #-------------------------------------
    #Name, armor, HP, abilities
    #sets initals values for attributes for the class
    def __init__(self):
        self.name = "NightMan"
        self.alignment = "Neutral"
        self.armor_class = 10 
        self.hit_points = 5
        self.experience_points = 0
        self.level = 1
        #A dictionary holding all the characters abilities and modifiers (key value pairs)
        self.abilities = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "wisdom": 10,
            "intellegence": 10,
            "charisma": 10
        }

    #getter and setter for the name attribute
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    #-------------------------------------
    #Alignment

    #getter and setter for the alignment attribute
    def get_alignment(self):
        return self.alignment 

    def set_alignment(self, alignment):
        self.alignment = alignment 
    
    #-------------------------------------
    #Armor and HP
    #getter and setter for the armor attribute
    def get_armor_class(self):
        #calculates the armor class and dex modifier by adding together
        dexterity_modifier = self.get_dexterity_modifier()
        return self.armor_class + dexterity_modifier

    def set_armor_class(self, armor_class):
        self.armor_class = armor_class

    #getter and setter for the HP attribute
    def get_hit_points(self):
        #calculates HP by adding constitution modifier and HP
        constitution_modifier = self.get_constitution_modifier()
        #maxes the HP out at 1 to prevent character being alive with negative HP
        return max(1, self.hit_points + constitution_modifier)

    def set_hit_points(self, hit_points):
        self.hit_points = max(1, hit_points)

    #-------------------------------------
    #Attack

    #defines attack method
    #takes roll and enemy as parameters
    def attack(self, roll, enemy):
        #if the roll is a 20 then you can attack
        if roll == 20:
            self.gain_experience(10)
            return True
        #adds the roll and strength modifiers
        attack_roll = roll + self.get_strength_modifier()
        #takes the level and checks how much you get added to the attack roll
        if self.level % 2 == 0:
            attack_roll += 1
        #if the attack roll is above the enemy armor class then you can attack
        if attack_roll >= enemy.get_armor_class():
            self.gain_experience(10)
            return True
        #if nothing is true you cannot attack
        return False

    #-------------------------------------
    #Damage
    
    #defines damage
    #takes damage as a parameter
    def damage_taken(self, damage):
        #checks if damage is greater than 0
        if damage > 0:
            #takes damage and adds strength modifier
            modified_damage = max(1, damage + self.get_strength_modifier())
            #subtracts damage from HP
            self.hit_points -= modified_damage
        #sets HP to 0 if it falls below
        if self.hit_points <= 0:
            self.hit_points = 0

    #checks if character is alive, returns True is it is, False if not
    def is_alive(self):
        return self.hit_points > 0

    #-------------------------------------
    #Abilities

    #getter methods for each attribute
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

    #setter methods for changing the abilities
    #can change the abilities by setting new scores for them
    def set_ability_score(self, ability, score):
        if ability in self.abilities:
            #gets the score of an ability
            self.abilities[ability] = score

    #takes ability and modifier as parameters
    def change_ability_score(self, ability, modifier):
        if ability in self.abilities:
            #modifies the ability (dex -2)
            self.abilities[ability] += modifier

    #calculates modified scores for abilities
    def get_strength_modifier(self):
        #gets strength score
        strength = self.get_strength()
        #calculates new score by subracting 10 and dividing 2 (like in DND)
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

    def gain_experience(self,points):
        self.experience_points += points
        #if EXP goes over what is needed to level up, level up method is called
        if self.experience_points >= self.get_experience_needed_for_level_up():
            self.level_up()

    #getter for EXP
    def get_experience_points(self):
        return self.experience_points

    #getter for level
    def get_level(self):
        return self.level

    #setter for level (level can be set directly)
    def set_level(self, level):
        self.level = level

    #calculates how much EXP is needed to level up
    def get_experience_needed_for_level_up(self):
        #multiplies current level with 1000 to figure out much is needed
        return 1000 * self.level

    #levels up the character
    def level_up(self):
        #adds one to character level
        self.level += 1
        #adds 5 more HP on level up
        self.hit_points += 5

