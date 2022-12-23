
#Simple user input Calculator

firstNumber = int(input("first number: "))
secondNumber = int(input("second number: "))
operation = input("operation: ")

if '+' in operation:
    print(firstNumber + secondNumber)
elif '-' in operation:
    print(firstNumber - secondNumber)
elif '*' in operation:
    print(firstNumber * secondNumber)
elif '/' in operation:
    print(firstNumber / secondNumber)
