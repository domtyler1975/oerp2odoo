import os
from os import path


def oerp2odoo(mod_path):
    print(f"Converting module in {mod_path} ...")

    for dir_name, subdir_list, file_list in os.walk(mod_path):
        print(f"Directory: {dir_name}")

        for file_name in file_list:
            file_ext = path.splitext(file_name)[1]

            if file_ext.lower() == ".pyc":
                print(f" - Deleting: {file_name}")
                os.remove(path.join(dir_name, file_name))
            else:
                print(f" - Unchanged: {file_name}")
