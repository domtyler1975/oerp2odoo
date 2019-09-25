
import os
from os import path


def replace_text(content, replacements):
    for r_name in replacements.keys():
        replacement = replacements[r_name]
        if isinstance(replacement, list):
            # simple [search, replacement] item
            search_str, replace_str = replacement
            exists = content.find(search_str)
            if exists > -1:
                print("    - replace", r_name)
                content = content.replace(search_str, replace_str)
    return content
