from square import Square


class Group(list):
    min, max = 1, 9


    def __init__(self):
        s = super(Group, self)
        for i in range(self.min, self.max+1):
            s.append(Square())


    def isdone(self):
        return all(self.value())


    def value(self):
        return [sq.value() for sq in self]


    def eliminate(self, value):
        """Remove value from all squares.

        >>> r=Group()
        >>> r.eliminate(1)
        [Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9]), Square([2, 3, 4, 5, 6, 7, 8, 9])]
        """

        for square in self:
            square.eliminate(value)
        return self


    def fix(self, index, value):
        """Fix value at index, remove it from other squares.

        >>> r=Group()
        >>> r.fix(4, 5)
        [Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([5]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9])]
        """

        for square in self:
            square.eliminate(value)
        self[index].fix(value)
        return self


if __name__ == "__main__":
    import doctest
    doctest.testmod()
