from square import Square
from group import Group

class Row(Group): pass
class Col(Group): pass
class Box(Group): pass


class Sudoku(list):


    def __init__(self, box_height=3, box_width=3):
        """Create NxN sudoku where N equals box_height times
        box_width, i.e. number of squares in the box.

        >>> Sudoku(2,2)
        [Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9]), Square([1, 2, 3, 4, 5, 6, 7, 8, 9])]
        """

        self.box_height, self.box_width = box_height, box_width
        self.n = n = box_height * box_width
        for i in range(n*n):
            self.append(Square())


    def i2row(self, index):
        """Return row number and position on the row for the square at index.

        >>> Sudoku().i2row(32)
        (3, 5)
        """
        return index / self.n, index % self.n

    def i2col(self, index):
        """Return column number and position on the column for the square at
        index.

        >>> Sudoku().i2col(32)
        (5, 3)
        """
        r = self.i2row(index)
        return r[1], r[0]

    def i2box(self, index):
        """Return box number and position in the box of the square at index.
        >>> s=Sudoku()
        >>> s.i2box(41)
        4, 4
        >>> s.i2box(60)
        4, 4
        """
        h, w = self.box_height, self.box_width
        r, c = self.i2row(index), self.i2col(index)
        print r,c
        print r[0],h,r[0]/h
        print c[0],w,c[0]%w
        return r[0]/h*h + c[0]%w, r[1]%h*h + c[1]/w


    # def eliminate(self, value):
    #     for row in self:
    #         row.eliminate(value)


    def fix(self, index=None, value=None):
        """Fix value at index, remove it from other squares on the
        row, column and the box.
        Random index and/or value if not given.
        Note: no changes if (random) index points to a solved square.

        >>> r=Sudoku()
        >>> r.fix(4, 5)
        [Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([5]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9])]
        """

        if not index:
            index = random.randrange(len(self))
        if not value:
            value = random.choice(self[index])
        r, c, b = self.i2row(index), self.i2col(index), self.i2box(index)
        row.eliminate(value=value)
        col.eliminate(value=value)
        box.eliminate(value=value)
        self[index].fix(value)
        return self



if __name__ == "__main__":
    import doctest
    doctest.testmod()
