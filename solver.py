class Solver:
    def __init__(self, grid):
        self.grid = grid

    def get_grid(self):
        return self.grid.get_grid()

    # Check if value can be inserted in line, following sudoku rules
    def check_insert_in_line(self, row, value):
        g = self.grid.get_grid()
        for i in g[row, :]:
            if i == value:
                return False
        return True

    # Check if value can be inserted in column, following sudoku rules
    def check_insert_in_column(self, column, value):
        g = self.grid.get_grid()
        for i in g[:, column]:
            if i == value:
                return False
        return True

    # Check if value can be inserted in square, following sudoku rules
    def check_insert_in_square(self, row, column, value):
        g = self.grid.get_grid()
        row_coef = int(row/3) * 3
        column_coef = int(column/3) * 3

        for i in g[row_coef:row_coef + 3, column_coef:column_coef + 3]:
            for j in i:
                if j == value:
                    return False
        return True

    # Use the three methods above to check if a value can be inserted
    # at a given cell in the sudoku grid
    def check_insert_value(self, row, column, value):
        if (self.check_insert_in_line(row, value) and
            self.check_insert_in_column(column, value) and
            self.check_insert_in_square(row, column, value)):
            return True
        return False

    # Solve the sudoku grid using backtracking
    # The grid is assumed to be solvable
    def solve_grid(self):
        check, row, column = self.grid.is_filled()
        if check:
            # Grid is filled, therefore the algorithm solved the sudoku grid
            return True
        # Tries every value from 1 to 9
        for i in range(1, 10):
            if self.check_insert_value(row, column, i):
                self.grid.add_number(row, column, i)
                if self.solve_grid():
                    return True
                # Value is not suitable for the current empty cell,
                # Backtrack
                self.grid.undo_move()
        # No value is suitable for the current empty cell, therefore the sudoku is not solvable
        # (That, or my algorithm does not work)
        return False



