from arena.champion import Champion

def test_take_damage():
    ahri = Champion("Ahri")
    ahri.take_damage(300)
    assert ahri.health == 700