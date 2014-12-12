class Square(set):
    min, max = 1, 9

    def __init__(self, values=range(min, max+1)):
        super(Square, self).update(values)

    def isdone(self):
        return self.value() != None

    def value(self):
        self.assert_invariant()
        if len(self) == 1:
            return list(self)[0]
        return None

    def eliminate(self, value):
        if value in self:
            self.remove(value)

    def fix(self, value):
        """Single value found, remove others from set.

        >>> s=Square()
        >>> s.fix(5)
        Square([5])
        """

        self.clear()
        self.add(value)
        return self

if __name__ == "__main__":
    import doctest
    doctest.testmod()

