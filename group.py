from square import Square
import random


class Group(list):


    def __init__(self, n=9):
        """Initilize to group of n squares, default zero.
        >>> Group()
        [Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9])]
        >>> Group(6)
        [Square([1, 2, 3, 4, 5, 6]), Square([1, 2, 3, 4, 5, 6]), Square([1, 2, 3, 4, 5, 6]), Square([1, 2, 3, 4, 5, 6]), Square([1, 2, 3, 4, 5, 6]), Square([1, 2, 3, 4, 5, 6])]
        """
        s = super(Group, self).__init__([Square(n) for i in range(n)])


    def isdone(self):
        return all(self.value())


    def value(self):
        return [sq.value() for sq in self]


    def eliminate(self, value):
        """Remove value from all squares.
        >>> r=Group(9)
        >>> r.eliminate(1)
        [Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9])]
        """
        for square in self:
            square.eliminate(value)
        return self


    def fix(self, index=None, value=None):
        """Fix value at index, remove it from other squares.
        Random index and/or value if not given.
        Note: no changes if (random) index points to a solved square.
        >>> r=Group()
        >>> r.fix(4, 5)
        [Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([5]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9])]
        """
        if not index:
            index = random.randrange(len(self))
        if not value:
            value = random.choice(list(self[index]))
        self.eliminate(value)
        self[index].fix(value)
        return self


    def __str__(self):
        return ' '.join([str(sq) for sq in self])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
