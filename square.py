import random


class Square(set):
    min, max = 1, 9

    def __init__(self, values=range(min, max+1)):
        super(Square, self).update(values)

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
        Square([5])
        """

        if value == None:
            value = random.choice(list(self))
        self.clear()
        self.add(value)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

