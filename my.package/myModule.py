def top_n(items, n):
    """Return the top n items in a list in desc order

        Parameters:
            items(array) : list or array-like object
            n (int) : Number of items to return

        Return:
            array : top n items in descending order

        Egs:
            >>> top_n ([8, 3, 2, 7, 4], 3)
            [8, 7, 4]
        
    """
    new_items = sorted(items, reverse = True)
    return new_items[:3]
     