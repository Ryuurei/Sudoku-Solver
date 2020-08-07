import numpy as np
import modification as modif
import modification_list as modif_list


# Methods are declared outside of class for clarity

# Print grid
def print_grid(self):
    print('-------------------------')
    for i in range(0, self.grid.shape[0]):
        print('| ', end='')
        for j in range(0, self.grid.shape[1] - 1):
            # Print blank if None
            if self.grid[i, j] is None:
                print('  ', end='')
            else:
                print(str(self.grid[i, j]) + ' ', end='')
            # Separate grid in blocks
            if (j + 1) % 3 == 0:
                print('| ', end='')
        if self.grid[i, 8] is None:
            print('  |')
        else:
            print(str(self.grid[i, 8]) + ' |')
        if (i + 1) % 3 == 0:
            print('-------------------------')


# Add or replace a number on the grid
def add_number(self, row, column, nb):
    # Check indexes
    if not 0 <= row <= 8:
        print('row index must be between 0 and 8')
    if not 0 <= column <= 8:
        print('column index must be between 0 and 8')
    # Keep track of modifications to revert changes/reset the grid
    modification = modif.Modification(row, column, self.grid[row, column])
    self.modif_list.add_modification(modification)
    if nb == 0:
        self.grid[row, column] = None
    else:
        self.grid[row, column] = nb


# Remove last modification madeon the grid
def undo_move(self):
    modification = self.modif_list.last_modification()
    row = modification.get_row()
    column = modification.get_column()
    old_nb = modification.get_old_nb()
    self.grid[row, column] = old_nb
    self.modif_list.pop_modification()


# Reset every modification made on the grid
def reset(self):
    while self.modif_list.get_modif_history().size != 0:
        undo_move(self)


# Check if the grid is filled, not if it is correct
# If not filled, return the first empty cell encountered
def is_filled(self):
    for idx, i in enumerate(self.grid.flatten()):
        if i is None:
            row = int(idx / 9)
            column = idx % 9
            return False, row, column
    return True, -1, -1


class Grid:
    def __init__(self, grid = None):
        # 2D numpy array
        self.modif_list = modif_list.ModificationList()
        if grid is None:
            self.grid = np.empty((9, 9), dtype=object)
        else:
            self.grid = grid

    def get_grid(self):
        return self.grid

    def get_modification_list(self):
        return self.modif_list

    # Assign functions written above as class methods
    print_grid = print_grid
    add_number = add_number
    undo_move = undo_move
    reset = reset
    is_filled = is_filled
