def calculate(a, b, action):
    while True:
        if action == '*':
            res = (a * b)
        elif action == '-':
            res = (a - b)
        elif action == '+':
            res = (a + b)
        elif action == '/':
            res = (a / b)
        else:
            res = ('You have not typed a valid action, please run the program again.')
        return res

a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
action = input('''Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
 ''')
print(calculate(a, b, action))
