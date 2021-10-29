def calculate():
    while True:
        a = int(input('Enter your first number: '))
        b = int(input('Enter your second number: '))
        action = input('''Please type in the math operation you would like to complete:
            + for addition
            - for subtraction
            * for multiplication
            / for division
''')
        if action == '*':
            print(a * b)
        elif action == '-':
            print(a - b)
        elif action == '+':
            print(a + b)
        elif action == '/':
            print(a / b)
        else:
            print('You have not typed a valid action, please run the program again.')
print(calculate())

