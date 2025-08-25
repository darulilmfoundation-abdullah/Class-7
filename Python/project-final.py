# Final Project: Greeting + Calculator

print("Welcome to Grade 7 Python Project!")

# Step 1: Ask name
name = input("Enter your name: ")
print("Hello", name, "!")

# Step 2: Simple calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose an operation: +, -, *, /")
op = input("Enter operation: ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b == 0:
        print("Error! Cannot divide by zero.")
    else:
        print("Result:", a / b)
else:
    print("Invalid operation")
