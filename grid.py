from square import Square
from group import Group

class Row(Group): pass
class Col(Group): pass
class Box(Group): pass

class Grid(list):
    box_height = box_width = 3
    min, max = 1, box_height * box_width

    def __init__(self):
        m = self.max
        n = self.box_height
        assert self.box_height == self.box_width
        for i in range(m * m):
            self.append(Square())
        self.row = [self[i*m:(i+1)*m] for i in range(m)]
        self.col = [self[i:m*m:m] for i in range(m)]
        self.box = [[] for i in range(m)]
        b=[x/n+n*(y/n) for y in range(m) for x in range(m)]
        for s,i in zip(self,b):
            self.box[i].append(s)
        
    # def assert_invariant(self):
    #     n = len(self)
    #     assert self.min <= n <= self.max, 'invalid Grid size: %d, %s' % (n, self)
    #     for row in self:
    #         row.assert_invariant()

    # def isdone(self):
    #     return all(self.value())

    # def value(self):
    #     return [sq.value() for sq in self]

    # def eliminate(self, value):
    #     for row in self:
    #         row.eliminate(value)

    # def add(self, value):
    #     for row in self:
    #         row.add(value)
        
