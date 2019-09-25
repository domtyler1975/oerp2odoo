import re
from pprint import pprint

# match _columns = { ... }
COLUMN_MATCH_RE = re.compile(
    r"^(\s{4}_columns\s*=\s*{(.*?)})",
    flags=re.MULTILINE | re.DOTALL
)

# match     'field_name' : fields.
FIELD_START_MATCH_RE = re.compile(
    r"""\s{4}['"](\w+)['"]\s*:\s*fields\."""
)


def replace_columns(content):
    col_blocks = re.findall(COLUMN_MATCH_RE, content)
    for col_block, col_def in col_blocks:
        lines = col_def.splitlines()
        new_col_def = "\n"

        # combine field definitions that span multiple lines into one string
        col_list = []
        for line in lines:
            if line.strip():
                if re.search(FIELD_START_MATCH_RE, line):
                    # start of new field
                    col_list.append(line)
                else:
                    col_list[-1 if len(col_list) else 0] += "\n" + line

        # for each column
        for col in col_list:

            # convert to a class field instead of a dict item
            field_match = re.search(FIELD_START_MATCH_RE, col)
            field_name = field_match.group(1)
            new_field = f"    {field_name} = fields.{col[field_match.end():]}"
            new_field = new_field.rstrip().rstrip(",")

            # add it to the new column definition list
            new_col_def += new_field + "\n"

        print("    - replace _columns block")
        content = content.replace(col_block, new_col_def)

    return content
