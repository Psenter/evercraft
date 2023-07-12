from character import Character
from morals import Alignment 
from HP import Armor_Hitpoints

#Name
def test_get_name():
    c = Character("Bill")
    assert c.name == "Bill"

def test_set_name():
    d = Character("Bob")
    d.set_name("Bob")
    assert d.name == "Bob"

def test_set_name2():
    d = Character("Joe")
    d.set_name("Joe")
    assert d.name == "Joe"

#----------------------------------------------
#Alignment

def test_get_alignment():
    a = Alignment("Good")
    assert a.alignment == "Good"

def test_get_alignment():
    a = Alignment("Neutral")
    assert a.alignment == "Neutral"

def test_get_alignment():
    a = Alignment("Evil")
    assert a.alignment == "Evil"


def test_set_alignment():
    a = Alignment("Evil")
    a.set_alignment("Evil")
    assert a.alignment == "Evil"

def test_set_alignment():
    a = Alignment("Neutral")
    a.set_alignment("Neutral")
    assert a.alignment == "Neutral"

def test_set_alignment():
    a = Alignment("Good")
    a.set_alignment("Good")
    assert a.alignment == "Good"

#----------------------------------------------
#HP and armor

def test_get_armor_hitpoints():
    armor = 10
    hitpoints = 5
    x = Armor_Hitpoints(armor, hitpoints)
    assert x.armor == armor
    assert x.hitpoints == hitpoints