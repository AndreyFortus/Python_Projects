import re


def find_year():
    with open('C:/Users/Andrii/Desktop/lab_11/text_with_dates.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    pattern = r'\b\d{3,4}\b'
    years_list = []

    for i, line in enumerate(lines):
        matches = re.findall(pattern, line)
        for year in matches:
            years_list.append((int(year), i + 1))

    for year, line_number in years_list:
        print(f'Year: {year}, row: {line_number}')


find_year()
