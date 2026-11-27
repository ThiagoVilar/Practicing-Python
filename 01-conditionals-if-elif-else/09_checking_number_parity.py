# Activity 09: Checking number parity
# Reads an integer and shows whether it is even or odd.

number = int(input('Enter an integer: '))

if number % 2 == 0:
    print(f'The number {number} is even.')
else:
    print(f'The number {number} is odd.')