# Activity 02: Calculating total project time
# Adds the days of three activities and shows the total project time.
# Shows an error if any of the values is negative.

activity_a = int(input('Enter the days for activity A: '))
activity_b = int(input('Enter the days for activity B: '))
activity_c = int(input('Enter the days for activity C: '))

if activity_a < 0 or activity_b < 0 or activity_c < 0:
    print('Error: The days cannot be negative.')
else:
    total_days = activity_a + activity_b + activity_c
    print(f'The activities will be completed in {total_days} days.')