from character import Character

#-------------------------------------
#Name

def test_get_name():
    d = Character()
    assert d.name == "NightMan"

def test_set_name():
    d = Character()
    d.set_name("Bob")
    assert d.name == "Bob"

#-------------------------------------
#Alignment

def test_get_alignment():
    d = Character()
    assert d.alignment == "Neutral"

def test_set_alignment():
    d = Character()
    d.set_alignment("Good")
    assert d.alignment == "Good"

#-------------------------------------
#Armor and HP

def test_get_armor_class():
    d = Character()
    assert d.armor_class == 10

def test_set_armor_class():
    d = Character()
    d.set_armor_class(9)
    assert d.armor_class == 9

def test_get_hit_points():
    d = Character()
    assert d.hit_points == 5

def test_set_hit_points():
    d = Character()
    d.set_hit_points(8)
    assert d.hit_points == 8

def test_hit_points_minimum_value():
    character = Character()
    character.set_hit_points(0)
    character.set_ability_score("constitution", 8)

    assert character.get_hit_points() == 1

#-------------------------------------
#Attack

def test_can_attack():
    ourcharacter = Character()
    ourcharacter.set_name("Attacker")
    enemy = Character()
    enemy.set_name("Defender")
    enemy.set_armor_class(9)
    assert ourcharacter.attack(10, enemy) == True

def test_cannot_attack():
    ourcharacter = Character()
    ourcharacter.set_name("Attacker")
    enemy = Character()
    enemy.set_name("Defender")
    enemy.set_armor_class(11)
    assert ourcharacter.attack(10, enemy) == False

def test_can_attack_with_modifier():
    ourcharacter = Character()
    ourcharacter.set_name("Attacker")
    ourcharacter.set_ability_score("strength", 14)
    enemy = Character()
    enemy.set_name("Defender")
    enemy.set_armor_class(9)
    assert ourcharacter.attack(10, enemy) == True

#-------------------------------------
#Damage

def test_damage_taken():
     ourcharacter = Character()
     ourcharacter.set_name("Attacker")
     enemy = Character()
     enemy.set_name("Defender")
     enemyhitpoints = enemy.get_hit_points()
     if ourcharacter.attack(10, enemy):
        enemy.damage_taken(10)
     assert enemy.get_hit_points() < enemyhitpoints

def test_is_alive():
    character = Character()
    assert character.is_alive() == True

def test_damage_taken_with_modifier():
    ourcharacter = Character()
    ourcharacter.set_name("Attacker")
    ourcharacter.set_ability_score("strength", 14)

    enemy = Character()
    enemy.set_name("Defender")
    enemy.set_hit_points(15)

    enemyhitpoints = enemy.get_hit_points()
    damage = 10 + ourcharacter.get_strength_modifier()
    enemy.damage_taken(damage)
    assert enemy.get_hit_points() == enemyhitpoints - max(1, damage)


#-------------------------------------
#Abilities

def test_ability():
    character = Character()
    assert character.get_strength() == 10
    assert character.get_dexterity() == 10
    assert character.get_constitution() == 10
    assert character.get_wisdom() == 10
    assert character.get_intellegence() == 10
    assert character.get_charisma() == 10

def test_set_ability_score():
    character = Character()
    character.set_ability_score("strength", 12)
    assert character.get_strength() == 12

def test_change_ability_score():
    character = Character()
    character.set_ability_score("dexterity", 10)
    character.change_ability_score("dexterity", 0)
    assert character.get_dexterity() == 10

def test_ability_with_modifier():
    character = Character()
    character.set_ability_score("strength", 14)
    assert character.get_strength() == 14
    assert character.get_strength_modifier() == 2

def test_armor_class_with_dexterity_modifier():
    character = Character()
    character.set_armor_class(10)
    character.set_ability_score("dexterity", 14)
    assert character.get_armor_class() == 12

def test_hit_points_with_constitution_modifier():
    character = Character()
    character.set_hit_points(5)
    character.set_ability_score("constitution", 12)

    assert character.get_hit_points() == 6

#-------------------------------------
#Experience and levels

def test_gain_experience():
    Attacker = Character()
    Attacker.set_name("Parker")
    Defender = Character()
    Defender.set_name("Mike_Tyson")
    Defender.set_armor_class(9)
    starting_xp = Attacker.experience_points
    Attacker.attack(10, Defender)
    assert Attacker.experience_points == starting_xp + 10

