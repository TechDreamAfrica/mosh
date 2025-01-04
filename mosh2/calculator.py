all_numbers = []

while True:
    target = int(input("How many numbers do you want to calculate?: "))
    for count in range(target):
        number = float(input("Enter number: "))
        all_numbers.append(number)

    operators = {
        "addition:": "+",
        "subtraction:": "-",
        "multiplication:": "*",
        "division:": "/",
        "clear:": "c",
        "quit:": "q"
    }
    for key, value in operators.items():
        print(key, value)

    operator = input("choose operator: ")

    def clear():
        if operator.lower() == "c":
            all_numbers.clear()

    def addition(total, *numbers):
        for _ in all_numbers:
            total += _
        return total

    def subtraction(total, *numbers):
        for n in all_numbers:
            total += n
        return total

    def multiplication(total, *numbers):
        for n in all_numbers:
            total *= n
        return total

    def division(total, *numbers):
        for n in all_numbers:
            total *= n
        return total

    # addition = first_number + second_number
    # subtraction = first_number - second_number
    # multiplication = first_number * second_number
    # division = first_number / second_number

    if operator.lower() != "q":
        if operator.lower() == "c":
            clear()

        if operator == "+":
            print(addition(0, all_numbers))

        if operator == "-":
            print(subtraction)

        if operator == "*":
            print(multiplication)

        if operator == "/":
            for ns in all_numbers:
                if ns == 0:
                    print("ZERO DIVISION ERROR")
                else:
                    print(division)
    else:
        print("Quitting Calculator")
        break