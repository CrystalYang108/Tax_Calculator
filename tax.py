income = input("how much do you mke a week?")
income = float(income)
annual_income = income * 52
print(income)
print(annual_income)

if annual_income > 8500:
    tax = 0.045 * annual_income
    print(tax)
    
elif annual_income > 1077550:
    tax = annual_income * 8.82
    print(tax)

elif annual_income > 215401:
    tax = annual_income * 6.85
    print(tax)

elif annual_income > 80651:
    tax = annual_income * 6.57
    print(tax)

elif annual_income > 21401:
    tax = annual_income * 6.33
    print(tax)

elif annual_income > 13901:
    tax = annual_income * 5.9
    print(tax)

elif annual_income > 8501:
    tax = annual_income * 4.5
    print(tax)