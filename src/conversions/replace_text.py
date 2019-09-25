
import os
import re


def replace_text(content, replacements):
    for r_name in replacements.keys():
        replacement = replacements[r_name]
        if isinstance(replacement, list):
            # simple [search, replacement] item
            search_str, replace_str = replacement

            if isinstance(search_str, re.Pattern):
                exists = re.search(search_str, content)
                if exists:
                    print("    - replace", r_name)
                    content = re.sub(search_str, replace_str, content)
            else:
                exists = content.find(search_str)
                if exists > -1:
                    print("    - replace", r_name)
                    content = content.replace(search_str, replace_str)
    return content
