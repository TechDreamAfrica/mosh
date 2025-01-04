employees = [
    ("John Doe", 70000, "Software Developer", 3),
    ("Jane Smith", 75000, "Software Developer", 4),
    ("Alice Johnson", 80000, "Senior Software Developer", 6),
    ("Bob Brown", 65000, "Junior Software Developer", 1),
    ("Charlie Davis", 90000, "Lead Software Developer", 8),
    ("Diana Green", 78000, "Software Developer", 4),
    ("Ethan White", 72000, "Software Developer", 3),
    ("Fiona Black", 85000, "Senior Software Developer", 7),
    ("George King", 93000, "Lead Software Developer", 10),
    ("Hannah Lewis", 76000, "Junior Software Developer", 2),
    ("Ian Walker", 68000, "Software Developer", 3),
    ("Jackie Adams", 74000, "Software Developer", 4),
    ("Kelly Moore", 77000, "Senior Software Developer", 6),
    ("Liam Scott", 82000, "Software Developer", 5),
    ("Mia Baker", 86000, "Lead Software Developer", 9),
    ("Oliver King", 95000, "Principal Software Engineer", 12),
    ("Rachel Clark", 78000, "Software Developer", 4),
    ("Steve Hall", 68000, "Junior Software Developer", 1),
    ("Tina Collins", 79000, "Software Developer", 3)
]

def tax_employees_with_salary_above_50000():
    tax_percentage = 12.45
    taxed_salary = [employee[1] - (employee[1] * tax_percentage) for employee in employees if employee[1] >= 50000]
    return taxed_salary

def sort_employees_with_salary_above_50000():
    employee = [employee for employee in employees if employee[1] >= 500000]
    return employee

def sort_employees_with_salary_below_50000():
    employee = [employee for employee in employees if employee[1] <= 500000]
    return employee

def promote_employees():
    is_promoted = False
    experience_criteria = 3

    employees_not_promoted = [employee for employee in employees if employee[3] >= experience_criteria and not is_promoted]
    for employee in employees_not_promoted:
        if employee[2] == "Software Developer":
            new_position = "Senior Software Developer"
            new_salary = 80000
            print(f"{employee[0]} has been promoted to {new_position} with a salary of {new_salary}")

promote_employees()