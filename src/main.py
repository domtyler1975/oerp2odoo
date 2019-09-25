import os
from os import path
from . import util
from .conversions.remove_text import remove_text


def oerp2odoo(mod_path):
    print(f"Converting module in {mod_path} ...")

    for dir_name, subdir_list, file_list in os.walk(mod_path):
        print(f"Directory: {dir_name}")

        for file_name in file_list:
            ext = path.splitext(file_name)[1].lower()
            file_full_path = path.join(dir_name, file_name)

            if file_name == "__openerp__.py":
                print(f" - Renaming: {file_name}")
                new_name = "__manifest__.py"
                new_path = path.join(dir_name, new_name)
                os.rename(file_full_path, new_path)
                file_name = new_name
                file_full_path = new_path

            if ext == ".pyc":
                print(f" - Deleting: {file_name}")
                os.remove(file_full_path)
            elif ext == ".py":
                print(f" - Converting: {file_name}")
                content = util.get_content(file_full_path)
                content = remove_text(content)
                util.set_content(file_full_path, content)
            else:
                print(f" - Unchanged: {file_name}")
