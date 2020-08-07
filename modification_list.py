import numpy as np


# List that contains every modifications made on the grid
class ModificationList:
    def __init__(self):
        self.modif_list = np.array([])

    def get_modif_history(self):
        return self.modif_list

    def print_modif_history(self):
        for i in self.modif_list:
            i.print_modification()

    def add_modification(self, modification):
        self.modif_list = np.append(self.modif_list, modification)

    def last_modification(self):
        return self.modif_list[-1]

    def pop_modification(self):
        self.modif_list = self.modif_list[:-1]