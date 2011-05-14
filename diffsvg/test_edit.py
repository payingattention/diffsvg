from .edit import editpath
def test_editpath():
    assert editpath('aa','aa')  == ('mama', 0)
    assert editpath('aa','bb')  == ('abraabra', 2)
    assert editpath('aa','aabb')  == ('mamaabab', 2)
    assert editpath('aabb','aa')  == ('mamarbrb', 2)
    assert editpath('123','23')  == ('r1m2m3', 1)

