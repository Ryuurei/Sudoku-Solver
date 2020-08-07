# Store modifications made to the grid in an object
# Used to undo moves
class Modification:
    def __init__(self, row, column, old_nb):
        self.row = row
        self.column = column
        self.old_nb = old_nb

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_old_nb(self):
        return self.old_nb

    def print_modification(self):
        print("row: " + str(self.row) + ", column: " + str(self.column) + ", old_nb: " + str(self.old_nb))
