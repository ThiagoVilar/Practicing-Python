# Activity 10: Approving loan
# Reads the monthly income and the desired installment.
# The loan is approved if the income is above 2000 and the installment
# is at most 30% of the income.

monthly_income = float(input('Enter your monthly income: '))
desired_installment = float(input('Enter the desired installment value: '))

if monthly_income > 2000 and desired_installment <= (monthly_income * 0.3):
    print('Loan approved!')
elif monthly_income <= 2000:
    print('Loan denied: insufficient income.')
else:
    print('Loan denied: installment above 30% of income.')