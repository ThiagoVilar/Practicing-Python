# Activity 05: Controlling monthly budget
# Reads the total expenses of the month and shows a warning
# if it exceeds the budget limit (3000).

total_monthly_expenses = float(input('Enter the total expenses of the month (R$): '))
budget_limit = 3000

if total_monthly_expenses > budget_limit:
    print('Warning! You have exceeded the budget limit.')
else:
    print('You are within the budget.')