monthly_income = input ("Enter your monthly income:")
monthly_expenses = input ("Enter your monthly expenses:")

monthly_saving = float(monthly_income) - float(monthly_expenses)

projected_saving = (monthly_saving * 12 + (monthly_saving * 12 * 0.05))

print (f"Your monthly savings are: {monthly_saving}")
print (f"Your projected savings after one year, is : {projected_saving}")
