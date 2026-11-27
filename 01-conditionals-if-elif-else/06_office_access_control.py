# Activity 06: Office access control
# Reads the current hour (24-hour format) and allows access
# only between 8:00 and 17:59.

current_hour = int(input('Enter the current hour (24-hour format): '))

if 8 <= current_hour < 18:
    print('Access granted!')
else:
    print('Access denied!')