class Square(set):
    min, max = 1, 9
    id = 0

    def __init__(self, values=range(min, max+1)):
        super(Square, self).update(values)
        Square.id += 1
        self.id = Square.id
        #self.assert_invariant()

    def assert_invariant(self):
        n = len(self)
        assert self.min <= n <= self.max, 'invalid candidate set size: %d, %s' % (n, self)
        for x in self:
            assert self.min <= x <= self.max, '%d out of range [%d, %d]' % (x, a, b)

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

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)
