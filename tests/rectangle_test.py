def test_rectangle():
    from src.rectangle import Rectangle

    r = Rectangle(2, 4)
    assert r.area == 8
    assert r.perimeter == 12