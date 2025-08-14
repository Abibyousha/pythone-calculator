import math

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    if y == 0:
        return "Division by zero error"
    return x/y
def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def tan(x):
    return math.tan(x)
def sqrt(x):
    return math.sqrt(x)
def log(x):
    return math.log(x)
def exp(x):
    return math.exp(x)
def pow(x,y):
    return math.pow(x,y)
def factorial(x):
    return math.factorial(x)
def mod(x,y):
    return x % y
def menu():
    print("\nScientific Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Sine")
    print("6. Cosine")
    print("7. Tangent")
    print("8. Square Root")
    print("9. Logarithm")
    print("10. Exponential")
    print("11. Power")
    print("12. Factorial")
    print("13. Modulus")
    print("0. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "0":
        print("Goodbye!")
        break
    if choice in ["1", "2", "3", "4", "11","13"]:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", sub(num1, num2))
        elif choice == "3":
            print("Result:", multi(num1, num2))
        elif choice == "4":
            print("Result:", div(num1, num2))
        elif choice == "13":
            print("Result:", mod(num1, num2))
        elif choice == "11":
            print("Result:", pow(num1, num2))
    elif choice in ["5", "6", "7"]:
        num1 = int(input("Enter angle in radians: "))
        rad = math.radians(num1)
        if choice == "5":
            print("Result:", sin(rad))
        elif choice == "6":
            print("Result:", cos(rad))
        elif choice == "7":
            print("Result:", tan(rad))
    elif choice in ["8", "9", "10", "12"]:
        num1 = int(input("Enter a number: "))
        if choice == "8":
            print("Result:", sqrt(num1))
        elif choice == "9":
            print("Result:", log(num1))
        elif choice == "10":
            print("Result:", exp(num1))
        elif choice == "12":
            print("Result:", factorial(num1))
    else:
        print("Invalid choice")
