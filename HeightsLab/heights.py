class HeightMap:

    # constructor - uses self to reference member variables
    def __init__(self, r, c):
        self.rows = r
        self.cols = c
        # Use a list of lists to represent the heights in the grid

    def isPeak(self, r, c):
        """
        r -- a valid row index in heights
        c --  a valid column index in heights

        return -> true if the height at row r, column c is not at the edge of the two-dimensional array heights, and is greater in value than all 8 surrounding values; false otherwise.
        """
        return True

# Example
hm = HeightMap(3, 3) # invoke constructor
print(hm.isPeak(2, 2))