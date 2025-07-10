# Input
monthly_income = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your total monthly expenses: '))

# calcuations
monthly_savings = monthly_income - monthly_expenses
Projected_savings = monthly_income * 12 + (monthly_expenses * 12 * 0.05)

# Output
print(f'Your monthly savings are Your monthly savings are ${monthly_savings}')
print(f'Projected savings after one year, with interest, is: ${Projected_savings}')
