class square(set):
    min, max = 1, 9
    
    def __init__(self, values=range(min, max+1)):
        super(square, self).update(values)
        status, msg = self.invariant()
        assert status, msg

    def invariant(self):
        s = self
        a, b = s.min, s.max
        n = len(s)
        if n < a or n > b:
            return False, 'invalid candidate set size: %d, %s' % (n, s)
        for x in s:
            if a <= x <= b:
                continue
            return False, '%d out of range [%d, %d]' % (x, a, b)
        return True, None

    def isdone(self):
        return self.value() != None

    def value(self):
        s = self
        status, msg = s.invariant()
        assert status, msg
        if len(s) == 1:
            return list(s)[0]
        return None


print square()
