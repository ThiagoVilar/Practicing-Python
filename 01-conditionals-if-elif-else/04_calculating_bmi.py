# Activity 04: Calculating BMI
# Reads weight and height, calculates the BMI
# and shows the weight category.

weight = float(input('Enter your weight (kg): '))
height = float(input('Enter your height (m): '))
bmi = weight / (height ** 2)

print(f'Your BMI is {bmi:.2f}')

if bmi < 18.5:
    print('You are underweight.')
elif bmi < 25:
    print('You are at a normal weight.')
else:
    print('You are overweight.')