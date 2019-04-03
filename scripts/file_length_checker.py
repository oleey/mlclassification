
# Python 3.6.7
# Ubuntu 18.04

import os
import json
from pathlib import Path

file_name = 'invalid_names.json'  # the file name


def file_name_checker(folder_path, max_length):
    """ 
    Checks that each file in folder_path (and its subfolders) has a length of 
    at most max_length. Creates a json file in each folder and (subfolder) containing
    the list of files with length greater than max_length. 

    To be used as boilerplate for creating json results in each folder that the 
    ML model will use for predicting which image is which. (Hotels or Non-hotels)

    """

    invalid_names = [] # list of file names greater than max_length

    if not (os.path.isdir(folder_path)): # verify that it's a valid folder path that was given as input. Quit if not.
        print("You didn't supply a valid path. Exiting...")
        exit()

    for folder_name, folder, files in os.walk(folder_path):  

        for file in files:
            filename = file.split('.')[0] # get the file name
            if len(filename) > max_length:
                invalid_names.append((file))

        with open(os.path.join(folder_name, file_name), 'w') as f: # After each iteration in a folder,
            json.dump({'invalid_file_names': invalid_names}, f)    # write all the invalid names to a json file in the folder

        invalid_names.clear() # clear the list containing the invalid names for use in the next iterated folder

    
    return 

def main():
    """ The main script """

    length_is_int = False

    while not length_is_int:
        try:
            max_length = int(input('What should be the maximum length of the file name? (An Integer): '))
            length_is_int = True
        except ValueError:
            print("Error: The maximum length should be an integer\n")
            continue
        
    folder_path = input('Type in an absolute folder path: ')
    file_name_checker(folder_path, max_length)
    
    print(f"Done! The '{file_name}' file has been written to respective folders in {folder_path}")



if __name__ == '__main__':
    main()


