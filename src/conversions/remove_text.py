
import os
from os import path

REMOVE_TEXT_PATH = path.abspath(
    path.join(path.dirname(__file__), "../../remove_text"))
REMOVE_TEXTS = []

for file_name in os.listdir(REMOVE_TEXT_PATH):
    with open(path.join(REMOVE_TEXT_PATH, file_name), 'r') as text_file:
        REMOVE_TEXTS.append({
            "name": file_name,
            "content": text_file.read()
        })


def remove_text(content):
    """Looks for text from the remove_text folder and removes it"""
    for text in REMOVE_TEXTS:
        exists = content.find(text["content"])
        if exists > -1:
            print("     removing:", text["name"])
        content = content.replace(text["content"], "")
    return content
