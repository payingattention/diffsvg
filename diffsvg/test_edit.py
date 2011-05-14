from .edit import editpath
def test_editpath():
    assert editpath('aa','aa')  == ('mm', 0)
    assert editpath('aa','bb')  == ('xx', 2)
    assert editpath('aa','aabb')  == ('mmabab', 2)
    assert editpath('aabb','aa')  == ('mmrbrb', 2)

