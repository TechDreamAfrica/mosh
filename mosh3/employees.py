employees = [
    ("John Doe", 50000),
    ("Jane Smith", 55000),
    ("Alice Johnson", 60000),
    ("Bob Brown", 45000),
    ("Charlie Davis", 48000),
    ("Diana Green", 52000),
    ("Ethan White", 47000),
    ("Fiona Black", 53000),
    ("George King", 58000),
    ("Hannah Lewis", 62000),
    ("Ian Walker", 49000),
    ("Jackie Adams", 51000),
    ("Kelly Moore", 57000),
    ("Liam Scott", 59000),
    ("Mia Baker", 61000)
]

def tax_employees_with_salary_above_50000():
    tax_percentage = 12.45
    taxes = [employee[1] - (employee[1] * tax_percentage) for employee in employees if employee[1] >= 50000]
    return taxes

def sort_employees_with_salary_above_50000():
    employee = [employee for employee in employees if employee[1] >= 500000]
    return employee

def sort_employees_with_salary_below_30000():
    employee = [employee for employee in employees if employee[1] <= 500000]
    return employee

def promote_employees():
    pass