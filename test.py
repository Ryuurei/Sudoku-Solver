import numpy as np
import sudoku_grid as grid
import solver

# An example
g = np.array([[5, 3, None, None, 7, None, None, None, None],
              [6, None, None, 1, 9, 5, None, None, None],
              [None, 9, 8, None, None, None, None, 6, None],
              [8, None, None, None, 6, None, None, None, 3],
              [4, None, None, 8, None, 3, None, None, 1],
              [7, None, None, None, 2, None, None, None, 6],
              [None, 6, None, None, None, None, 2, 8, None],
              [None, None, None, 4, 1, 9, None, None, 5],
              [None, None, None, None, 8, None, None, 7, 9]])

gr = grid.Grid(g)
s = solver.Solver(gr)
print(s.solve_grid())
m = s.get_grid()
print(m)
