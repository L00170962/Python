'''
Script: mybudget.py
By: AV
Purpose: Calculate a simple budget.
Tested: on Python v3.10.7 under Windows 11

'''
print("This is a simple budget calculator")
# Total income
income=42000
percent_20_tax=income * .2
income_after_tax=income - percent_20_tax

# Cola expense for 4 days a week , 4 weeks per month
cola=1.5 * 4 * 4

# Beer expense for 2 days a week, 4 weeks per month
beer=2 * 2 * 4

# Petrol Expense for 4 weeks per month
petrol=60 * 4

# Total Expense
total_expense=cola+petrol+beer

# Print the results after formatting
print("Total income is €{i}".format(i=income))
print("Total income after tax is €{i}".format(i=income_after_tax))
print("Total expense for month is €{e:1.2f}".format(e=total_expense))
budget=income_after_tax - total_expense
print("Budget for a month is €{b:1.2f}".format(b=budget))

