
Percentage = float(input("Enter percentage: "))
income = int(input("Enter family income: "))

Percentage_ok = Percentage >= 75
income_ok = income <= 300000

print("Percentage_ok", Percentage_ok)
print("Income ok", income_ok)
print("Scholarship eligible", Percentage_ok and income_ok)
print("At least one condition", Percentage_ok or income_ok)
print("Not percentage ok", not Percentage_ok)
