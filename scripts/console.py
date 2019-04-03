
# python 3.6.7

import os
import json
from pathlib import Path

file_name = 'invalid_names.json'
root_dir = Path(os.path.abspath(os.path.dirname(__file__))).parent
file_path = os.path.join(root_dir, file_name)


def file_name_checker(folder_path):

    invalid_names = [] # list of file names greater than six

    if not (os.path.isdir(folder_path)):
        print("You didn't supply a path. Exiting...")
        exit()

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            filename = file.split('.')[0]
            if len(filename) > 6:
                invalid_names.append(file)

    
    return invalid_names




if __name__ == '__main__':
    folder_path = input('Type in an absolute folder path: ')
    names = file_name_checker(folder_path)
    result = {'invalid_file_names': names}

    with open(file_path, 'w') as f:
        json.dump(result, f)

    print(f"Done! Invalid filenames have been written to {file_path}")
