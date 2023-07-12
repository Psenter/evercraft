from character import Character

def test_get_name():
    c = Character('Bill')
    assert c.name == "Bill"