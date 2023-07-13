from character import Character
from fighter import Fighter

#Fighter tests

def test_hit_points_gain_per_level():
    fighter = Fighter()
    fighter.set_level(3)
    fighter.gain_experience(3000)
    assert fighter.get_hit_points() == 65

def test_attack_bonus_per_level():
    fighter = Fighter()
    fighter.set_level(4)
    enemy = Character()
    result = fighter.attack(15, enemy)
    assert True