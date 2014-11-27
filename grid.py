from group import Group

class Row(Group): pass
class Col(Group): pass
class Box(Group): pass

class Grid(list):
    min, max = 1, 9
    
    def __init__(self):
        for x in range(self.max):
            self.append(Row())
        # TODO: view grid through rows, cols and boxes
        rows = self
        cols = [rows[i] for i in range(len(self))]
        print cols[0]
        self.assert_invariant()
        
    def assert_invariant(self):
        n = len(self)
        assert self.min <= n <= self.max, 'invalid Grid size: %d, %s' % (n, self)
        for row in self:
            row.assert_invariant()

    def isdone(self):
        return all(self.value())

    def value(self):
        return [sq.value() for sq in self]

    def eliminate(self, value):
        for row in self:
            row.eliminate(value)

    def add(self, value):
        for row in self:
            row.add(value)
        

print Grid()
