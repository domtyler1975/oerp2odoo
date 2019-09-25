
import re


def get_content(file_name):
    with open(file_name, 'r') as text_file:
        return text_file.read()


def set_content(file_name, content):
    with open(file_name, 'w') as text_file:
        text_file.write(content)


def load_replacements(replacements_file):

    def regex(pattern):
        return re.compile(
            pattern,
            flags=re.MULTILINE
        )

    rep_content = get_content(replacements_file)
    replacements = eval(rep_content, {
        "regex": regex
    })
    return replacements
