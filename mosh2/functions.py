from openpyxl.styles.builtins import title


def multiply(total, *numbers):
    for number in numbers:
        total *= number
    return total

print(multiply(1, 2, 3, 4, 5))

def save_user(**user):
    print(user)

save_user(id=1, name="Godfred")
