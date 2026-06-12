def calculate_tax(salary):
    if salary > 5000000:
        return salary * 0.20
    else:
        return salary * 0.13

def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    return salary - tax


salary = float(input("Maoshingizni kiriting: "))

tax = calculate_tax(salary)
net_salary = calculate_net_salary(salary)

print("Soliq:", tax)
print("Qo‘lga tegadigan maosh:", net_salary)