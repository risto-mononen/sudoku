import random


class Square(set):


    def __init__(self, n=9):
        """Create square with all valid candidate values.
        >>> Square()
        Square({1, 2, 3, 4, 5, 6, 7, 8, 9})
        >>> Square(6)
        Square({1, 2, 3, 4, 5, 6})
        """
        super(Square, self).__init__(range(1,n+1))


    def isdone(self):
        return self.value() != None

    def value(self):
        if len(self) == 1:
            return list(self)[0]


    def eliminate(self, value):
        if value in self:
            self.remove(value)

    def fix(self, value=None):
        """Fix to single value, remove others from set.
        Choose a random value if not given.
        >>> s=Square()
        >>> s.fix(5)
        >>> s
        Square({5})
        """
        if value == None:
            value = random.choice(list(self))
        self.clear()
        self.add(value)


    def __str__(self):
        """
        >>> s=Square()
        >>> print (s)
        [9]
        >>> s.fix(5)
        >>> print (s)
         5 
        """
        if self.isdone():
            return ' %d ' % self.value()
        return '[%d]' % len(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

