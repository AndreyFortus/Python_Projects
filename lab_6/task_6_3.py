import constants


def create_list():
    with open(constants.PATH + 'learning_python.txt', 'r', encoding='utf-8') as file:
        return file.readlines()


if __name__ == '__main__':
    print(create_list())
