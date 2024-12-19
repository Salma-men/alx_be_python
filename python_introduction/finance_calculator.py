# Ask for the user's monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask for the user's total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate the projected savings after one year, with interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Output the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
