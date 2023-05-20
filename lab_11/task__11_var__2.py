import re


def separate_text():
    with open('C:/Users/Andrii/Desktop/lab_11/text_example.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    pattern = r'(?<=[.!?])\s+'
    return re.split(pattern, text)


def main():
    i = 1
    for sentence in separate_text():
        print(f'Sentence {i}: {sentence}')
        i += 1


main()
