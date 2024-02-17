import random
from square import Square
from group import Group


class Sudoku(list):


    def __init__(self, box_height=3, box_width=3):
        """Create NxN sudoku where N equals box_height times
        box_width, i.e. number of squares in the box.
        >>> s=Sudoku(2,2)
        >>> s
        [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]
        >>> s.col
        [[Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]]
        >>> s.row
        [[Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]]
        >>> s[9].eliminate(1)
        >>> s
        [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]
        >>> s.col
        [[Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]]
        >>> s.row
        [[Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]]
        >>> s.box
        [[Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]]
        """
        s = self
        s.box_height, s.box_width = box_height, box_width
        h,w = box_height, box_width
        s.n = n = box_height * box_width
        s.col,s.row,s.box = list(),list(),list()
        for i in range(n):
            s.col.append(Group(0))
            s.row.append(Group(0))
            s.box.append(Group(0))
        for y in range(n):
            for x in range(n):
                sq = Square(n)
                s.append(sq)
                s.col[x].append(sq)
                s.row[y].append(sq)
                s.box[self.xy2box(x,y)].append(sq)


    def i2xy(self, index):
        """Return (x,y) coordinates for the square at index.
        >>> s=Sudoku()
        >>> for i in range(0,81,7):
        ... 	print (i, s.i2xy(i))
        ... 
        0 (0, 0)
        7 (7, 0)
        14 (5, 1)
        21 (3, 2)
        28 (1, 3)
        35 (8, 3)
        42 (6, 4)
        49 (4, 5)
        56 (2, 6)
        63 (0, 7)
        70 (7, 7)
        77 (5, 8)
        """
        return int(index%self.n), int(index/self.n)


    def i2box(self, index):
        """Return box number for the square at index.
        >>> s=Sudoku(2,2)
        >>> for i in range(len(s)):
        ... 	print (i, s.i2box(i))
        ...
        0 0
        1 0
        2 1
        3 1
        4 0
        5 0
        6 1
        7 1
        8 2
        9 2
        10 3
        11 3
        12 2
        13 2
        14 3
        15 3
        """
        x,y = self.i2xy(index)  # Normal coordinates
        return self.xy2box(x,y)


    def xy2box(self, x, y):
        h,w = self.box_height, self.box_width
        bx,by = int(x/h),int(y/w)         # Outer box
        ix,iy = x%h,y%w         # Inner box
        return bx+by*h


    def eliminate(self, index, value):
        """Remove value all squares on the row, column and the box defined by
        the index.
        >>> s=Sudoku(2,2)
        >>> s.eliminate(0,1)
        >>> s
        [Square({2, 3, 4}), Square({2, 3, 4}), Square({2, 3, 4}), Square({2, 3, 4}), Square({2, 3, 4}), Square({2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]
        >>> s.col
        [[Square({2, 3, 4}), Square({2, 3, 4}), Square({2, 3, 4}), Square({2, 3, 4})], [Square({2, 3, 4}), Square({2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]]
        >>> s.row
        [[Square({2, 3, 4}), Square({2, 3, 4}), Square({2, 3, 4}), Square({2, 3, 4})], [Square({2, 3, 4}), Square({2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]]
        >>> s.box
        [[Square({2, 3, 4}), Square({2, 3, 4}), Square({2, 3, 4}), Square({2, 3, 4})], [Square({2, 3, 4}), Square({2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({2, 3, 4}), Square({1, 2, 3, 4}), Square({2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]]
        """
        x,y = self.i2xy(index)
        b = self.xy2box(x,y)
        self.col[x].eliminate(value)
        self.row[y].eliminate(value)
        self.box[b].eliminate(value)


    def fix(self, index=None, value=None):
        """Fix value at index, remove it from other squares on the
        row, column and the box.
        Random index and/or value if not given.
        Return (index, value) tuple.
        Note: no changes if (random) index points to a solved square.
        >>> s=Sudoku(2,2)
        >>> s.fix(1,2)
        ((1, 0), 2)
        >>> s
        [Square({1, 3, 4}), Square({2}), Square({1, 3, 4}), Square({1, 3, 4}), Square({1, 3, 4}), Square({1, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]
        >>> s.col
        [[Square({1, 3, 4}), Square({1, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({2}), Square({1, 3, 4}), Square({1, 3, 4}), Square({1, 3, 4})], [Square({1, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]]
        >>> s.row
        [[Square({1, 3, 4}), Square({2}), Square({1, 3, 4}), Square({1, 3, 4})], [Square({1, 3, 4}), Square({1, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]]
        >>> s.box
        [[Square({1, 3, 4}), Square({2}), Square({1, 3, 4}), Square({1, 3, 4})], [Square({1, 3, 4}), Square({1, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 3, 4}), Square({1, 2, 3, 4}), Square({1, 3, 4})], [Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4}), Square({1, 2, 3, 4})]]
        """
        if index == None:
            index = random.randrange(len(self))
        if value == None:
            value = random.choice(list(self[index]))
        self.eliminate(index, value)
        self[index].fix(value)
        return self.i2xy(index), value


    def __str__(self):
        return '\n'.join([str(r) for r in self.row])
        return ' '.join([str(sq) for sq in self])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
