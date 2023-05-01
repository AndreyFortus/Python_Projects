def users(users_list):
    if len(users_list) == 0:
        print('We need to find some users!')
    else:
        for user in users_list:
            if user == 'Admin':
                print('Hello Admin, I hope you\'re well.')
            else:
                print(f'Hello {user} thank you for logging in again.')


name_list = ['Alex', 'John', 'Dan', 'Admin', '123_TeSt_321']
users(name_list)
