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