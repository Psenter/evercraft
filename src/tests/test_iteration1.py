from character import Character
from morals import Alignment 
from HP import Armor_Hitpoints
from attack import Attack
from maincharacter import MainCharacter

def test_create_character():
    character = MainCharacter("Bob")
    assert character.get_name() == "Bob"