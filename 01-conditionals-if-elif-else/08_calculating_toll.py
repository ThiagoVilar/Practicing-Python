# Activity 08: Calculating toll
# Reads the distance traveled and shows the toll value:
# up to 100 km = R$ 10.00, up to 200 km = R$ 20.00, above 200 km = R$ 30.00.

distance_traveled = int(input('Enter the distance traveled (in km): '))

if distance_traveled <= 100:
    print('Toll value: R$ 10.00')
elif distance_traveled <= 200:
    print('Toll value: R$ 20.00')
else:
    print('Toll value: R$ 30.00')