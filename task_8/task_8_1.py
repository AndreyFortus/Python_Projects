def users(users_list):
    if len(users_list) == 0:
        print('We need to find some users!')
    else:
        for user in users_list:
            print('Hello Admin, I hope you\'re well.') if user == 'Admin' else\
                print(f'Hello {user} thank you for logging in again.')


def main():
    name_list = ['Alex', 'John', 'Dan', 'Admin', '123_TeSt_321']
    users(name_list)


main()
