# Activity 08: Countdown
# Shows a countdown from 10 to 1 with a different message for even
# and odd numbers, and a final message when the countdown ends.

for count in range(10, 0, -1):
    if count % 2 == 0:
        print(f'Only {count} seconds left - Don\'t miss this opportunity!')
    else:
        print(f'The countdown continues: {count} seconds remaining.')

print('Take advantage of the promotion now!')