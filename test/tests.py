from my.package import myModule

def test_top_n():
    """
        make sure top_n works correctly
    """
    assert myModule.top_n([8, 3, 2, 4, 7]) == [8, 7, 4], 'incorrect'