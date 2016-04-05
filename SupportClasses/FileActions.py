####################################################################
# Library of File methods
# Saving object?
#   Use "save_to_pickle"
####################################################################

from os import path, getcwd
from pickle import dump, load

"""Class can be init with a dir but if not, it will assume working directory"""
class FileActions():

    def __init__(self, a_dir = None):
        self.a_dir = a_dir
        self.a_dir = self.change_none_dir_to_cwd()

    """If a_dir is == None, sets the dir to current working dir"""
    def change_none_dir_to_cwd(self):
        if self.a_dir == None:
            return getcwd()
        else:
            return self.a_dir

    """Tests to see if a dir exists"""
    def test_if_dir_exists(self):
        return path.isdir(self.a_dir)

    def create_dir(self):
        pass

    """Save file with data in pickle format. Must pass the data to pickle"""
    def save_to_pickle_file(self, a_data, a_file_name):
        dump(a_data, open(a_file_name+".p", "wb"))


    """Open file with data from pickle format to original data"""
    def retrieve_pickled_file(self):
        #data =
        pass

if __name__ == '__main__':
    f = FileActions()
    print(f.test_if_dir_exists())
