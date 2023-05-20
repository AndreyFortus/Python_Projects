import re

from const_file import PATH


def replace_date(match):

    date = match.group()
    parts = re.split('[./]', date)

    if len(parts[0]) == 4:
        new_date = parts[2] + '.' + parts[1] + '.' + parts[0]
    else:
        new_date = parts[0].zfill(2) + '.' + parts[1].zfill(2) + '.' + parts[2].zfill(4)

    return new_date


def main():
    with open(PATH + 'date.txt', 'r', encoding='utf-8') as file_date:
        text = file_date.read()

    pattern = r'\b((0?[1-9]|[12]\d|3[01])[./]' \
              r'(0?[1-9]|1[012])[./](\d{4}))|((\d{4})[./](' \
              r'0?[1-9]|1[012])[./](0?[1-9]|[12]\d|3[01]))\b'

    new_text = re.sub(pattern, replace_date, text)

    with open(PATH + 'sorted_date.txt', 'w', encoding='utf-8') as file_sort:
        file_sort.write(new_text)


main()
