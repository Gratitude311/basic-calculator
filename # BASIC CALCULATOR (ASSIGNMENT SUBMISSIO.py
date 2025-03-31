# BASIC CALCULATOR (ASSIGNMENT SUBMISSION)
# Takes two numbers and performs +, -, *, /
# Handles division by zero and invalid operators
# Submitted by: Antoniette Kagendo Kariuki
def basic_calculator():
    print("==== BASIC PYTHON CALCULATOR ====")
    
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Can't divide by zero!")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operator! Use +, -, *, or /")
            return
        
        print(f"Result: {num1} {operator} {num2} = {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers!")

# Run the calculator
basic_calculator()
