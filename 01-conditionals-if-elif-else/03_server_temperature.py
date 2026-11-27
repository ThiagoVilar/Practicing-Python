# Activity 03: Server temperature
# Reads the current temperature and shows an alert
# if it is above the allowed limit (25).

temperature = int(input('Enter the current temperature: '))

if temperature > 25:
    print('Alert! Temperature above the allowed limit.')
else:
    print('Temperature within the safe limit.')