from square import Square

class Group(list):
    min, max = 1, 9
    
    def __init__(self):
        s = super(Group, self)
        for i in range(self.min, self.max+1):
            s.append(Square())
        self.assert_invariant()
        
    def assert_invariant(self):
        n = len(self)
        assert self.min <= n <= self.max, 'invalid Group size: %d, %s' % (n, self)
        i = 0
        for square in self:
            i += 1
            value = square.value()
            for other in self[i:]:
                assert value not in other, 'duplicate value: %s, %s' % (square, other)

    def isdone(self):
        return all(self.value())

    def value(self):
        return [sq.value() for sq in self]

    def eliminate(self, value):
        for square in self:
            square.eliminate(value)

    def add(self, value):
        for square in self:
            square.add(value)
        

print Group()
