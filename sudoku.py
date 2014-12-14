from square import Square
from group import Group


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


    def i2xy(self, index):
        """Return (x,y) coordinates for the square at index.
        >>> s=Sudoku()
        >>> for i in range(0,81,7):
        ... 	print i, s.i2xy(i)
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
        return index%self.n, index/self.n


    def i2box(self, index):
        """Return box number and position in the box of the square at index.
        >>> s=Sudoku()
        >>> for i in range(0,81,7):
        ... 	print i, s.i2box(i)
        ...
        0 (0, 0, 0, 0)
        7 (2, 0, 1, 0)
        14 (1, 0, 2, 1)
        21 (1, 0, 0, 2)
        28 (0, 1, 1, 0)
        35 (2, 1, 2, 0)
        42 (2, 1, 0, 1)
        49 (1, 1, 1, 2)
        56 (0, 2, 2, 0)
        63 (0, 2, 0, 1)
        70 (2, 2, 1, 1)
        77 (1, 2, 2, 2)
        """
        h,w = self.box_height, self.box_width
        x,y = self.i2xy(index)  # Normal coordinates
        bx,by = x/h,y/w         # Outer box
        ix,iy = x%h,y%w         # Inner box
        return bx,by,ix,iy      # TODO: Map tuple to a unique int


    # def eliminate(self, value):
    #     for row in self:
    #         row.eliminate(value)


    # def fix(self, index=None, value=None):
    #     """Fix value at index, remove it from other squares on the
    #     row, column and the box.
    #     Random index and/or value if not given.
    #     Note: no changes if (random) index points to a solved square.

    #     >>> r=Sudoku()
    #     >>> r.fix(4, 5)
    #     [Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([5]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9]), Square([1, 2, 3, 4, 6, 7, 8, 9])]
    #     """

    #     if not index:
    #         index = random.randrange(len(self))
    #     if not value:
    #         value = random.choice(self[index])
    #     r, c, b = self.i2row(index), self.i2col(index), self.i2box(index)
    #     row.eliminate(value=value)
    #     col.eliminate(value=value)
    #     box.eliminate(value=value)
    #     self[index].fix(value)
    #     return self



if __name__ == "__main__":
    import doctest
    doctest.testmod()
