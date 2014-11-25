from square import Square

class Group(list):
    min, max = 1, 9
    
    def __init__(self):
        s = super(Group, self)
        for i in range(self.min, self.max+1):
            s.append(Square())
        status, msg = self.invariant()
        assert status, msg

    def invariant(self):
        a, b = self.min, self.max
        n = len(self)
        if n < a or n > b:
            return False, 'invalid Group size: %d, %s' % (n, self)
        s = self
        for i in range(n):
            sq = s[i]
            v = sq.value()
            if not v:
                continue
            for other in s[i+1:]:
                if v in other:
                    return False, 'duplicate value of Square[%d]: %d in %d' % (i, v, other)
        return True, None

    def isdone(self):
        return all(self.value())

    def value(self):
        return [sq.value() for sq in self]
        

print Group()

class Row(Group): pass
class Col(Group): pass
class Box(Group): pass

print  Row()
print  Col()
print  Box()
