from character import Character

def test_get_name():
    c = Character("Bill")
    assert c.name == "Bill"

def test_set_name():
    d = Character("Bob")
    d.set_name("Bob")
    assert d.name == 'Bob'

def test_set_name2():
    d = Character("Joe")
    d.set_name("Joe")
    assert d.name == "Joe"