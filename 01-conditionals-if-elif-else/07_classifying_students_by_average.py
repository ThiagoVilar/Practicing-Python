# Activity 07: Classifying students by average
# Reads three grades, calculates the average and shows
# whether the student passed, is in recovery or failed.

first_grade = float(input('Enter the first grade: '))
second_grade = float(input('Enter the second grade: '))
third_grade = float(input('Enter the third grade: '))

average = (first_grade + second_grade + third_grade) / 3

if average >= 7:
    print('Passed!')
elif average >= 5:
    print('Recovery!')
else:
    print('Failed!')