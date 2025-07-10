# Input
monthlyIncome = int(input('Enter your monthly income: '))
monthlyExpenses = int(input('Enter your total monthly expenses: '))

# calcuations
monthlySavings = monthlyIncome - monthlyExpenses
ProjectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)

# Output
print(f'Your monthly savings are Your monthly savings are ${monthlySavings}')
print(f'Projected savings after one year, with interest, is: ${ProjectedSavings}')
