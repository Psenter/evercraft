from character import Character

def test_get_name():
    d = Character()
    assert d.name == "NightMan"

def test_set_name():
    d = Character()
    d.set_name("Bob")
    assert d.name == "Bob"

def test_get_alignment():
    d = Character()
    assert d.alignment == "Neutral"

def test_set_alignment():
    d = Character()
    d.set_alignment("Good")
    assert d.alignment == "Good"

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

# Don't know, check this later
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

