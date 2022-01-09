import utils
import os
from os import path

def test_function():
    print("test_function")
    pass

def main():
    from platform import python_version

    print(python_version())
    NOTEBOOK_PATH = r"C:\Users\René\Documents\Rene\IA\IA297\Jupyter\420-A62-BB_ProjetSynthese\A62-EquipeCV\notebook"
    file_info = NOTEBOOK_PATH + r"\pickeled_function.plkz"
    print(path.exists(file_info))
    test_value=10
    utils.pickle_save(test_value, "test_value.pklz")
    test_1 = utils.pickle_read("test_value.pklz")
    print(test_1)

    utils.pickle_save(test_function, "test_function.pklz")
    toto_function = utils.pickle_read("test_function.pklz")
    toto_function()
    #pickled_function = utils.pickle_read(file_info)
    #print(pickled_function(7, 8))

    pickled_test_class = utils.pickle_read(NOTEBOOK_PATH + r"\pickled_test_class.pklz")

if __name__== "__main__":
   main()