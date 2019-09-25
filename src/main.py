import os
from os import path
from . import util
from .conversions.replace_text import replace_text

REPLACEMENTS_FILE = path.abspath(
    path.join(path.dirname(__file__), "./replacements.py"))
REPLACEMENTS = eval(util.get_content(REPLACEMENTS_FILE))


def oerp2odoo(mod_path, custom_replacements=None):
    print(f"Converting module in {mod_path} ...")

    for dir_name, subdir_list, file_list in os.walk(mod_path):
        print(f"Directory: {dir_name}")

        for file_name in file_list:
            ext = path.splitext(file_name)[1].lower()
            file_full_path = path.join(dir_name, file_name)

            print(f"   {file_name}")

            if file_name == "__openerp__.py":
                new_name = "__manifest__.py"
                new_path = path.join(dir_name, new_name)
                print(f"    - rename to {new_name}")
                os.rename(file_full_path, new_path)
                file_name = new_name
                file_full_path = new_path

            if ext == ".pyc":
                print(f"    - delete")
                os.remove(file_full_path)

            if ext in REPLACEMENTS.keys():
                content = util.get_content(file_full_path)
                content = replace_text(content, REPLACEMENTS[ext])
                util.set_content(file_full_path, content)

            if custom_replacements and ext in custom_replacements.keys():
                content = util.get_content(file_full_path)
                content = replace_text(content, custom_replacements[ext])
                util.set_content(file_full_path, content)
