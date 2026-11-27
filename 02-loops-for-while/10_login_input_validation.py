# Activity 10: Login input validation
# Keeps asking for a username and a password until both are valid:
# username with at least 5 characters and password with at least 8.

while True:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if len(username) < 5:
        print('The username must have at least 5 characters.')
        continue

    if len(password) < 8:
        print('The password must have at least 8 characters.')
        continue

    print('Registration completed successfully!')
    break