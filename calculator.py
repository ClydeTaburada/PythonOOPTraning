def calculate(a, b):
    add = a + b
    sub = a - b
    multiply = a * b
    divide = a / b 
    return add, sub, multiply, divide

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

add, sub, multiply, divide = calculate(num1, num2)

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", multiply)
print("Division:", divide)
